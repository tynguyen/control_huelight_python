COLOR_RGB_MAP = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "pink": (255, 192, 203),
    "grey": (128, 128, 128),
    "gray": (128, 128, 128),
    "silver": (192, 192, 192),
    "brown": (165, 42, 42),
    "maroon": (128, 0, 0),
    "lime": (0, 255, 0),
    "teal": (0, 128, 128),
    "navy": (0, 0, 128),
    "olive": (128, 128, 0),
    "fuchsia": (255, 0, 255),
    "aqua": (0, 255, 255),
    "violet": (238, 130, 238),
    "indigo": (75, 0, 130),
    "gold": (255, 215, 0),
    "silver": (192, 192, 192),
    "coral": (255, 127, 80),
    "salmon": (250, 128, 114),
    "plum": (221, 160, 221),
    "ivory": (255, 255, 240),
    "honeydew": (240, 255, 240),
    "mint": (245, 255, 250),
    "azure": (240, 255, 255),
    "lavender": (230, 230, 250),
    "beige": (245, 245, 220),
    "mintcream": (245, 255, 250),
    "whitesmoke": (245, 245, 245),
    "ghostwhite": (248, 248, 255),
    "aliceblue": (240, 248, 255),
    "cyan": (0, 255, 255),
    "lightcyan": (224, 255, 255),
    "mintcream": (245, 255, 250),
    "lavenderblush": (255, 240, 245),
}

MOOD_BOOSTING_COLOR_MAP = {
    "force_speedup": "red",
    "force_slowdown": "blue",
    "fresh": "white",
    "modern": "silver",
    "calm": ["blue"],
    "encourage": ["blue"],
}


def get_mood_color(mood):
    """
    Get appropriate color for mood based on the moode description
    @Args:
        mood: mood description
    """
    if mood in MOOD_BOOSTING_COLOR_MAP:
        return MOOD_BOOSTING_COLOR_MAP[mood]
    else:
        print(f"List of available moods: \n {MOOD_BOOSTING_COLOR_MAP.keys()}")
        print(f"No valid color mood is chosen. Return 'encourage' by default.")
        return MOOD_BOOSTING_COLOR_MAP["encourage"]


def rgb_to_hsv(*rgb):
    """
    Convert RGB to HSV.
    """
    if len(rgb) == 3:
        r, g, b = rgb
    elif len(rgb) == 1:
        r, g, b = rgb[0]
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        delta = (g - b) / df
        h = 60 * (delta % 6)
    elif mx == g:
        delta = (b - r) / df
        h = 60 * (delta + 2)
    elif mx == b:
        delta = (r - g) / df
        h = 60 * (delta + 4)
    if mx == 0:
        s = 0
    else:
        s = df / mx
    v = mx
    # Not good yet.
    s = int(s * 100)
    return {"h": int(h), "s": s, "v": v}


def rgb_to_xy(*rgb):
    """ conversion of RGB colors to CIE1931 XY colors
    Formulas implemented from: https://gist.github.com/popcorn245/30afa0f98eea1c2fd34d
    Args:
        rbg (list): a list of 3 numbers representing red, green and blue in the RGB space
    Returns:
        xy (list): x and y
    """
    if len(rgb) == 3:
        r, g, b = rgb
    elif len(rgb) == 1:
        r, g, b = rgb[0]
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    red, green, blue = r, g, b
    # gamma correction
    red = pow((red + 0.055) / (1.0 + 0.055), 2.4) if red > 0.04045 else (red / 12.92)
    green = (
        pow((green + 0.055) / (1.0 + 0.055), 2.4)
        if green > 0.04045
        else (green / 12.92)
    )
    blue = (
        pow((blue + 0.055) / (1.0 + 0.055), 2.4) if blue > 0.04045 else (blue / 12.92)
    )

    # convert rgb to xyz
    x = red * 0.649926 + green * 0.103455 + blue * 0.197109
    y = red * 0.234327 + green * 0.743075 + blue * 0.022598
    z = green * 0.053077 + blue * 1.035763

    # convert xyz to xy
    x = x / (x + y + z)
    y = y / (x + y + z)

    # TODO check color gamut if known
    return [x, y]
