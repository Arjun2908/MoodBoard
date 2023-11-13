import webcolors

MOOD_MAP = {
    'red': 'excitement, passion',
    'blue': 'calm, sadness',
    'yellow': 'happiness, energy',
    'green': 'peace, growth',
    'purple': 'luxury, ambition',
    'orange': 'enthusiasm, creativity',
    'black': 'power, mystery',
    'white': 'purity, simplicity',
    'pink': 'romance, playfulness',
    'brown': 'stability, earthiness',
    'gray': 'neutrality, balance'
}


def closest_color(rgb):
    """
    Find the closest named color for a given RGB value.

    Parameters:
    - rgb (tuple): RGB color value.

    Returns:
    - str: Name of the closest color.
    """
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb[0]) ** 2
        gd = (g_c - rgb[1]) ** 2
        bd = (b_c - rgb[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]


def deduce_mood_from_color(color_rgb):
    """
    Deduce mood from a given RGB color.

    Parameters:
    - color_rgb (tuple): RGB color value.

    Returns:
    - str: Mood associated with the color.
    """
    closest_named_color = closest_color(color_rgb)
    mood = MOOD_MAP.get(closest_named_color, 'unknown')
    return mood


# Example usage
if __name__ == "__main__":
    sample_color = (255, 0, 0)  # RGB value for red
    mood = deduce_mood_from_color(sample_color)
    print(f"The mood elicited by the color is: {mood}.")
