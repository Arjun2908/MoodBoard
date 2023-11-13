import cv2
import numpy as np


def export_mood_board(palette, mood_meter, output_path="mood_board.png"):
    """
    Combines the provided mood board components and saves the result.

    Parameters:
    - palette (np.array): Image of the color palette.
    - mood_meter (np.array): Image of the mood meter.
    - output_path (str): Path to save the final mood board image.

    Returns:
    - np.array: Image of the mood board.
    """

    # Calculate dimensions
    # Check and handle palette
    palette_width = palette.shape[1] if isinstance(palette, np.ndarray) else max([img.shape[1] for img in palette])

    # Check and handle keyframes
    # keyframes_width = keyframes.shape[1] if isinstance(keyframes, np.ndarray) else max(
    #     [img.shape[1] for img in keyframes])

    # Check and handle mood_meter
    mood_meter_width = mood_meter.shape[1] if isinstance(mood_meter, np.ndarray) else max(
        [img.shape[1] for img in mood_meter])

    total_width = max(palette_width, mood_meter_width)
    total_height = palette.shape[0] + mood_meter.shape[0]

    # Create a blank canvas
    mood_board_img = np.zeros((total_height, total_width, 3), dtype=np.uint8)

    # Place the palette on the mood board
    mood_board_img[:palette.shape[0], :palette.shape[1]] = palette

    # Place the keyframes on the mood board below the palette
    # offset_height = palette.shape[0]
    # mood_board_img[offset_height:offset_height + keyframes.shape[0], :keyframes.shape[1]] = keyframes

    # Place the mood meter below the keyframes
    offset_height = palette.shape[0]
    mood_board_img[offset_height:offset_height + mood_meter.shape[0], :mood_meter.shape[1]] = mood_meter

    # Save the mood board to the specified path
    # cv2.imwrite(output_path, mood_board_img)

    return mood_board_img


# Example usage
if __name__ == "__main__":
    palette = cv2.imread("path_to_palette_img.png")
    keyframes = cv2.imread("path_to_keyframes_img.png")
    mood_meter = cv2.imread("path_to_mood_meter_img.png")

    mood_board_img = export_mood_board(palette, keyframes, mood_meter)
    cv2.imshow("Mood Board", mood_board_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
