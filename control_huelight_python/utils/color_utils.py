import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


HSV_THRESH_VALUES = {
    "red": {
        "h_low": -15,
        "h_high": 30,
        "s_low": 0.60,
        "s_high": 1.0,
        "cool_to_warm": True,
    },
    "orange": {
        "h_low": 30,
        "h_high": 45,
        "s_low": 0.60,
        "s_high": 1.0,
        "cool_to_warm": True,
    },
    "yellow": {
        "h_low": 45,
        "h_high": 90,
        "s_low": 0.60,
        "s_high": 1.0,
        "cool_to_warm": False,
    },
    "green": {
        "h_low": 90,
        "h_high": 150,
        "s_low": 0.60,
        "s_high": 1.0,
        "cool_to_warm": False,
    },
    "cyan": {
        "h_low": 150,
        "h_high": 225,
        "s_low": 0.60,
        "s_high": 1.0,
        "cool_to_warm": False,
    },
    "blue": {
        "h_low": 225,  # 225. Add 20 to get very blue
        "h_high": 270,  # 270. -10 to get very blue
        "s_low": 0.60,
        "s_high": 1.0,
        "cool_to_warm": True,
    },
    "violet": {
        "h_low": 270,
        "h_high": 285,
        "s_low": 0.60,
        "s_high": 1.0,
        "cool_to_warm": True,
    },
    "magenta": {
        "h_low": 285,
        "h_high": 345,
        "s_low": 0.60,
        "s_high": 1.0,
        "cool_to_warm": True,
    },
}


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


def str_to_rgb(color):
    """
    Convert string to RGB color.
    """
    if color in COLOR_RGB_MAP:
        return COLOR_RGB_MAP[color]
    else:
        logger.debug(f"List of available colors: \n {COLOR_RGB_MAP.keys()}")
        logging.debug(f"No valid color is chosen. Return 'white' by default.")
        return COLOR_RGB_MAP["white"]


def get_mood_color(mood):
    """
    Get appropriate color for mood based on the moode description
    @Args:
        mood: mood description
    """
    if mood in MOOD_BOOSTING_COLOR_MAP:
        return MOOD_BOOSTING_COLOR_MAP[mood]
    else:
        logging.debug(f"List of available moods: \n {MOOD_BOOSTING_COLOR_MAP.keys()}")
        logging.debug(f"No valid color mood is chosen. Return 'encourage' by default.")
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
    return {"h": int(h), "s": s, "v": v}


def hsv_to_rgb(*hsv):
    """ Change HSV to RGB
        @Args:
            hsv: hue, saturation, value
    """
    if len(hsv) == 3:
        h, s, v = hsv
    elif len(hsv) == 1:
        h, s, v = hsv[0]
    h = h / 60.0
    i = int(h)
    f = h - i
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))
    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    elif i == 5:
        r, g, b = v, p, q
    return int(r * 255), int(g * 255), int(b * 255)


def pick_hsv_color(
    color: str, warmness_percentage: float = 1, brightness_percentage: float = 1
):
    """
    Pick a color with warmness level from the HSV color space (H is the hue, S is the saturation, V is the value).
    H in [0, 360], S in [0, 1], V in [0, 1]
    @Args:
        color: color name
        warmness_percentage: percentage of warmness in [0, 1]
        brightness_percentage: percentage of brightness in [0, 1]
    """
    if color not in HSV_THRESH_VALUES:
        raise ValueError(f"No HSV threshold values for color {color}")
    if warmness_percentage < 0 or warmness_percentage > 1:
        raise ValueError(f"Warmness percentage should be in [0, 1]")

    h_low = HSV_THRESH_VALUES[color]["h_low"]
    h_high = HSV_THRESH_VALUES[color]["h_high"]
    s_low = HSV_THRESH_VALUES[color]["s_low"]
    s_high = HSV_THRESH_VALUES[color]["s_high"]
    v_low = 0
    v_high = 1

    # Increase s_low by 0.1 to avoid white color
    s_low += 0.1

    # The warmness increases as the hue increases?
    cool_to_warm = HSV_THRESH_VALUES[color]["cool_to_warm"]
    if not cool_to_warm:
        warmness_percentage = 1 - warmness_percentage

    # Calculate v value
    v = v_low + (v_high - v_low) * brightness_percentage

    # Calculate h value
    h = h_low + (h_high - h_low) * warmness_percentage
    h = int(h + 360) % 360  # Make sure h is in [0, 360]

    # Calculate s value
    s = s_low + (s_high - s_low) * warmness_percentage
    return [h, s, v]


def pick_rgb_color_by_name(
    color: str, warmness_percentage: float = 1, brightness_percentage: float = 1
):
    """
    Pick a color with warmness level by name.
    @Args:
        color: color name
        warmness_percentage: percentage of warmness in [0, 1]
        brightness_percentage: percentage of brightness in [0, 1]
    """
    # Use the HSV color space to pick a color
    hsv = pick_hsv_color(color, warmness_percentage, brightness_percentage)
    # Convert HSV to RGB
    rgb = hsv_to_rgb(*hsv)
    return rgb


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
