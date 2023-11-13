import matplotlib.pyplot as plt
import numpy as np
import cv2
from io import BytesIO


def generate_mood_meter(moods, intensities):
    """
    Generate a bar graph representing mood intensities.

    Parameters:
    - moods (list[str]): List of detected moods.
    - intensities (list[float]): List of intensities for each mood.

    Returns:
    - np.array: Image of the mood meter bar graph.
    """

    # Plotting the bar graph
    plt.figure(figsize=(10, 5))
    plt.bar(moods, intensities, color='skyblue')
    plt.xlabel('Moods', fontsize=14)
    plt.ylabel('Intensity', fontsize=14)
    plt.title('Mood Meter', fontsize=16)
    plt.grid(axis='y')

    # Convert the plot to a memory file
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.5)
    buf.seek(0)

    # Convert memory file (BytesIO) to numpy array
    mood_meter_img = np.asarray(bytearray(buf.read()), dtype=np.uint8)
    mood_meter_img = cv2.imdecode(mood_meter_img, cv2.IMREAD_COLOR)

    buf.close()
    plt.close()

    return mood_meter_img


# Example usage
if __name__ == "__main__":
    sample_moods = ['happy', 'sad', 'excited']
    sample_intensities = [0.5, 0.3, 0.7]

    mood_meter_img = generate_mood_meter(sample_moods, sample_intensities)
    cv2.imshow("Mood Meter", mood_meter_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
