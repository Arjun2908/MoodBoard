import cv2
from .helpers import get_fps


def extract_frames(video_path, interval=5):
    """
    Extract frames from the video at the specified interval.

    Parameters:
    - video_path (str): Path to the video file.
    - interval (int): Interval in seconds between frames to extract.

    Returns:
    - frames (list): List of frames extracted from the video.
    - None: If the video loading fails.
    """

    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Error: Unable to load the video!")
        return None

    fps = get_fps(video)
    frames = []

    frame_number = 0  # Frame counter
    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Extract frame if it's an 'interval' second frame
        if frame_number % (fps * interval) == 0:
            frames.append(frame)

        frame_number += 1

    video.release()
    return frames


# Example usage
if __name__ == "__main__":
    video_path = "../samples/sample-5s.mp4"
    frames = extract_frames(video_path, interval=5)
    print(f"Extracted {len(frames)} frames from the video.")
