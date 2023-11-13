import tkinter as tk
from tkinter import filedialog


def upload_video(parent_frame, callback):
    """
    Provides an interface to upload a video.

    Parameters:
    - parent_frame (tk.Frame): Parent frame in which the uploader components are placed.
    - callback (function): Function to be called after video selection, passing the video's path.
    """

    # Frame for video upload
    upload_frame = tk.Frame(parent_frame, bg="lightgrey", padx=10, pady=10)
    upload_frame.pack(pady=20, fill=tk.X, expand=True)

    video_path_label = tk.Label(upload_frame, text="No video selected.", bg="lightgrey")
    video_path_label.pack(pady=10, padx=20, anchor=tk.W)

    def handle_upload():
        filetypes = [("All Files", "*.*"), ("MP4 Files", "*.mp4"), ("AVI Files", "*.avi"), ("MKV Files", "*.mkv"),
                     ("MOV Files", "*.mov")]
        file_path = filedialog.askopenfilename(title="Select a Video File", filetypes=filetypes)
        if file_path:
            video_path_label.config(text=file_path)
            callback(file_path)  # Pass the video path back to main application

    upload_button = tk.Button(upload_frame, text="Upload Video", command=handle_upload)
    upload_button.pack(pady=10)

    return upload_frame


# Example usage
if __name__ == "__main__":
    def print_path(path):
        print("Selected video path:", path)


    root = tk.Tk()
    root.title("Video Upload Test")
    app = upload_video(root, print_path)
    root.mainloop()
