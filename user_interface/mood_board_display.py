import tkinter as tk
from PIL import Image, ImageTk


class MoodBoardDisplay:
    def __init__(self, parent_frame):
        self.canvas = tk.Canvas(parent_frame, bg='white', bd=0, highlightthickness=0)
        self.canvas.pack(pady=20, fill=tk.BOTH, expand=True)

        # Scrollbars for the canvas
        self.h_scroll = tk.Scrollbar(parent_frame, orient="horizontal", command=self.canvas.xview)
        self.h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.v_scroll = tk.Scrollbar(parent_frame, orient="vertical", command=self.canvas.yview)
        self.v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(xscrollcommand=self.h_scroll.set, yscrollcommand=self.v_scroll.set)

        self.canvas.bind("<MouseWheel>", self.zoom)

        self.image_id = None

    def display_mood_board(self, image_path):
        """Displays the mood board on the canvas."""

        # Load image using PIL and convert to PhotoImage for tkinter
        mood_board_img = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(mood_board_img)

        # If an image is already displayed, remove it
        if self.image_id:
            self.canvas.delete(self.image_id)

        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

        # Display the mood board
        self.image_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def zoom(self, event):
        """Zooms in or out based on the mousewheel movement."""
        # This can be implemented using PIL to scale the image and then updating the canvas.
        # It will require storing the original image and applying scaling factors iteratively.
        pass


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Mood Board Display Test")

    frame = tk.Frame(root)
    frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    display = MoodBoardDisplay(frame)
    display.display_mood_board("path_to_mood_board.png")

    root.mainloop()
