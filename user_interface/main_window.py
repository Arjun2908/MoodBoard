import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import threading
from PIL import Image, ImageTk  # For handling and displaying images on the tkinter canvas

# Importing our core functionalities
from video_analysis import video_loader, frame_extractor, color_detector, mood_deducer
from mood_board import palette_generator, keyframe_arranger, mood_meter, board_exporter
from user_interface import video_upload, mood_board_display


class MoodBoardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mood Board Generator")

        # Set up the menu bar
        self.menu_bar = tk.Menu(root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Load Video", command=self.load_video)
        self.file_menu.add_command(label="Analyze Video", command=self.analyze_video)
        self.file_menu.add_command(label="Save Mood Board", command=self.generate_mood_board)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        root.config(menu=self.menu_bar)

        # Set up the main display area (will show mood board)
        self.display_canvas = tk.Canvas(root, bg="white")
        self.display_canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Set up the control panel
        self.control_frame = tk.Frame(root, bg="lightgrey")
        self.control_frame.pack(pady=20, fill=tk.X)
        self.analyze_button = tk.Button(self.control_frame, text="Analyze Video", command=self.analyze_video)
        self.analyze_button.pack(padx=20, side=tk.LEFT)
        self.generate_button = tk.Button(self.control_frame, text="Generate Mood Board",
                                         command=self.generate_mood_board)
        self.generate_button.pack(padx=20, side=tk.LEFT)

        # Initialize the video path and mood board data
        self.video_path = None
        self.mood_board_data = None

        # Add Help & About menus
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="How to Use", command=self.show_help)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        self.about_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="About", menu=self.about_menu)

        # Status Bar
        status_bar_frame = tk.Frame(root, bg="lightgrey", padx=10, pady=10, bd=1, relief=tk.SUNKEN)
        status_bar_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.status_bar = tk.Button(status_bar_frame, text="No video loaded", bg="lightgrey",
                                    relief=tk.FLAT, state=tk.DISABLED, highlightthickness=0, bd=0)
        self.status_bar.pack(fill=tk.BOTH, expand=1)

        # Create video upload section
        self.video_upload_section = video_upload.upload_video(self.root, self.set_video_path)

        # Initialize MoodBoardDisplay
        # self.mood_board_section = tk.Frame(self.root, bg="lightgrey")
        # self.mood_board_section.pack(pady=20, fill=tk.BOTH, expand=True)
        # self.mood_board_display = mood_board_display.MoodBoardDisplay(self.mood_board_section)

    def set_video_path(self, path):
        self.video_path = path
        self.status_bar.config(text=f"Loaded video: {path}")
        messagebox.showinfo("Info", "Video loaded successfully!")

    def load_video(self):
        filetypes = [("All Files", "*.*"), ("MP4 Files", "*.mp4"), ("AVI Files", "*.avi"), ("MKV Files", "*.mkv"),
                     ("MOV Files", "*.mov")]
        file_path = filedialog.askopenfilename(title="Select a Video File", filetypes=filetypes)
        if file_path:
            self.set_video_path(file_path)

    def analyze_video(self):
        if not self.video_path:
            messagebox.showerror("Error", "Please load a video first.")
            return

        # show that the video is being analyzed
        self.status_bar.config(text="Analyzing video...")
        threading.Thread(target=self.perform_video_analysis).start()

    def perform_video_analysis(self):
        # Extract frames
        frames = frame_extractor.extract_frames(self.video_path, interval=5)

        # Detect dominant colors
        colors = [color_detector.detect_dominant_colors(frame, k=3) for frame in frames]

        # Deduce moods
        moods = [mood_deducer.deduce_mood_from_color(color) for sublist in colors for color in sublist]
        moods = [mood for mood in moods if mood != 'unknown']

        # If moods is empty, add 'unknown'
        if not moods:
            moods.append('unknown')

        # Store the extracted data for mood board generation
        self.mood_board_data = {
            "frames": frames,
            "colors": colors,
            "moods": moods
        }
        # use the tkinter's main thread to update the GUI
        self.status_bar.after(0, lambda: self.status_bar.config(text="Video analysis complete!"))
        self.status_bar.after(0, lambda: messagebox.showinfo("Info", "Video analysis complete!"))

    def save_mood_board(self):
        if not self.mood_board_data:
            messagebox.showerror("Error", "Please generate a mood board first!")
            return

        file_path = filedialog.asksaveasfilename(title="Save Mood Board", filetypes=(
        ("PNG Files", "*.png"), ("JPEG Files", "*.jpg;*.jpeg"), ("All Files", "*.*")), defaultextension=".png")

        if not file_path:
            return

        mood_board_img = board_exporter.export_mood_board(self.mood_board_data["frames"],
                                                          self.mood_board_data["colors"], self.mood_board_data["moods"])
        cv2.imwrite(file_path, mood_board_img)
        self.status_bar.config(text="Mood board saved successfully!")

    def generate_mood_board(self):
        if not self.mood_board_data:
            messagebox.showerror("Error", "Please analyze a video first")
            return

        # Generate components for the mood board
        palette_img = palette_generator.generate_palette(self.mood_board_data["colors"])
        # keyframes_img = keyframe_arranger.arrange_keyframes(self.mood_board_data["frames"])
        mood_meter_img = mood_meter.generate_mood_meter(self.mood_board_data["moods"], [1 for _ in self.mood_board_data["moods"]])  # Example intensity

        # Combine components to get the final mood board
        mood_board_img = board_exporter.export_mood_board(palette_img, mood_meter_img)

        # Display the mood board on the canvas
        mood_board_pil_img = Image.fromarray(cv2.cvtColor(mood_board_img, cv2.COLOR_BGR2RGB))
        mood_board_tk_img = ImageTk.PhotoImage(mood_board_pil_img)
        self.display_canvas.create_image(0, 0, anchor=tk.NW, image=mood_board_tk_img)
        self.display_canvas.image = mood_board_tk_img

        # save
        file_path = filedialog.asksaveasfilename(title="Save Mood Board", filetypes=(
            ("PNG Files", "*.png"), ("JPEG Files", "*.jpg;*.jpeg"), ("All Files", "*.*")), defaultextension=".png")

        if not file_path:
            return

        cv2.imwrite(file_path, mood_board_img)
        messagebox.showinfo("Info", "Mood board saved successfully!")
        self.status_bar.config(text="Mood board saved successfully!")

    def show_help(self):
        help_text = """
        1. Load a video using the File menu.
        2. Click 'Analyze Video' to process the video.
        3. Once analysis is complete, click 'Generate Mood Board' to view the mood board.
        4. You can save the mood board using the File menu.
        """
        messagebox.showinfo("How to Use", help_text)

    def show_about(self):
        about_text = """
        Mood Board Generator v1.0
        Created by Arjun Gupta
        """
        messagebox.showinfo("About", about_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = MoodBoardApp(root)
    root.mainloop()
