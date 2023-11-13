import cv2
import numpy as np


def arrange_keyframes(keyframes, gap=10):
    """
    Arranges a list of keyframes horizontally with a gap.

    Parameters:
    - keyframes (list[np.array]): List of keyframes.
    - gap (int): Gap in pixels between keyframes.

    Returns:
    - np.array: Image of the arranged keyframes.
    """

    total_width = sum([frame.shape[1] for frame in keyframes]) + gap * (len(keyframes) - 1)
    max_height = max([frame.shape[0] for frame in keyframes])

    arranged_image = np.zeros((max_height, total_width, 3), dtype=np.uint8)

    x_offset = 0
    for frame in keyframes:
        arranged_image[: frame.shape[0], x_offset: x_offset + frame.shape[1]] = frame
        x_offset += frame.shape[1] + gap

    return arranged_image


# Example usage
if __name__ == "__main__":
    keyframe1 = cv2.imread("path_to_keyframe1.jpg")
    keyframe2 = cv2.imread("path_to_keyframe2.jpg")
    keyframe3 = cv2.imread("path_to_keyframe3.jpg")

    arranged_img = arrange_keyframes([keyframe1, keyframe2, keyframe3])
    cv2.imshow("Arranged Keyframes", arranged_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
