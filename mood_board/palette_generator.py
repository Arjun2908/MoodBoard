import cv2
import numpy as np


def generate_palette(colors, width=1000, height=500):
    """
    Generates a color palette from the given list of colors.

    Parameters:
    - colors (list[tuple]): List of RGB color values.
    - width (int): Width of each color swatch in the palette.
    - height (int): Height of the palette.

    Returns:
    - np.array: Image of the generated color palette.
    """

    num_colors = len(colors)
    palette = np.zeros((height, width * num_colors, 3), dtype=np.uint8)

    for idx, color in enumerate(colors):
        for sub_idx, sub_color in enumerate(color):
            palette[:, (idx + sub_idx) * width: (idx + sub_idx + 1) * width] = np.array(sub_color).reshape(1, 1,
                                                                                                           3)
    return palette


# Example usage
if __name__ == "__main__":
    sample_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
    palette_img = generate_palette(sample_colors)
    cv2.imshow("Color Palette", palette_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
