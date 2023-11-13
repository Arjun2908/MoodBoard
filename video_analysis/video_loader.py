import cv2
import os
from .helpers import get_video_duration, get_video_resolution, get_video_codec, get_video_bitrate

SUPPORTED_FORMATS = ["mp4", "avi", "mkv", "flv", "mov"]


def load_video(video_path):
    """
    Load and validate the video from the given path.

    Parameters:
    - video_path (str): Path to the video file.

    Returns:
    - video (cv2.VideoCapture object): Video object if successful.
    - None: If the video loading fails.
    """

    # Check if the file exists
    if not os.path.exists(video_path):
        print("Error: File not found!")
        return None

    # Check if the video format is supported
    file_extension = video_path.split('.')[-1].lower()
    if file_extension not in SUPPORTED_FORMATS:
        print(f"Error: Video format {file_extension} not supported!")
        return None

    # Load the video using OpenCV
    video = cv2.VideoCapture(video_path)

    # Validate that the video was properly loaded
    if not video.isOpened():
        print("Error: Unable to load the video!")
        return None

    return video


# Example usage
if __name__ == "__main__":
    video_path = "../samples/sample-5s.mp4"
    video_obj = load_video(video_path)

    if video_obj:
        duration = get_video_duration(video_obj)
        width, height = get_video_resolution(video_obj)
        codec = get_video_codec(video_obj)
        bitrate = get_video_bitrate(video_obj, video_path)

        print(f"Video loaded successfully with the following metadata:")
        print(f"Duration: {duration:.2f} seconds")
        print(f"Resolution: {width}x{height}")
        print(f"Codec: {codec}")
        print(f"Bitrate: {bitrate:.2f} bits/second")
    else:
        print("Failed to load the video.")
