import cv2
import os


def get_video_duration(video):
    """
    Returns the duration of the video in seconds.

    Parameters:
    - video (cv2.VideoCapture object): Video object to get duration for.

    Returns:
    - duration (float): Duration of the video in seconds.
    """
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps
    return duration


def get_video_resolution(video):
    """
    Returns the resolution of the video.

    Parameters:
    - video (cv2.VideoCapture object): Video object to get resolution for.

    Returns:
    - (width, height): Tuple containing width and height of the video.
    """
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return width, height


def get_video_codec(video):
    """
    Returns the codec used in the video.

    Parameters:
    - video (cv2.VideoCapture object): Video object to get codec for.

    Returns:
    - codec (str): FourCC codec string.
    """
    fourcc_code = int(video.get(cv2.CAP_PROP_FOURCC))
    codec = "".join([chr((fourcc_code >> 8 * i) & 0xFF) for i in range(4)])
    return codec


def get_video_bitrate(video, video_path):
    """
    Returns the video's bitrate.

    Parameters:
    - video (cv2.VideoCapture object): Video object to get duration for.
    - video_path (str): Path to the video file.

    Returns:
    - bitrate (int): Bitrate of the video.
    """
    duration = get_video_duration(video)
    file_size = os.path.getsize(video_path)
    bitrate = (file_size * 8) / duration  # in bits/second
    return bitrate

def get_fps(video):
    """
    Returns the frames per second (fps) of the video.

    Parameters:
    - video (cv2.VideoCapture object): Video object to get fps for.

    Returns:
    - fps (int): Frames per second of the video.
    """
    return int(video.get(cv2.CAP_PROP_FPS))


def convert_BGR_to_RGB(color):
    """
    Converts a color from BGR format to RGB format.

    Parameters:
    - color (tuple): Color in BGR format.

    Returns:
    - (tuple): Color in RGB format.
    """
    return tuple(reversed(color))