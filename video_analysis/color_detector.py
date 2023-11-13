import cv2
import numpy as np
from sklearn.cluster import KMeans
from .helpers import convert_BGR_to_RGB


def detect_dominant_colors(image, k=3):
    """
    Detect the dominant colors in an image using KMeans clustering.

    Parameters:
    - image (np.array): Image data.
    - k (int): Number of clusters (dominant colors) to detect.

    Returns:
    - list[tuple]: List of dominant colors in RGB format.
    """

    # Reshape the image to be a list of pixels
    pixels = image.reshape(-1, 3)

    # Apply KMeans clustering to find the most dominant k colors
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)

    # Convert the dominant colors from BGR to RGB
    dominant_colors = [convert_BGR_to_RGB(tuple(map(int, center))) for center in kmeans.cluster_centers_]

    return dominant_colors


# Example usage
if __name__ == "__main__":
    image_path = "path_to_extracted_frame.jpg"  # This would typically be an extracted frame from the previous step
    image = cv2.imread(image_path)
    colors = detect_dominant_colors(image, k=3)
    print(f"Dominant colors: {colors}")
