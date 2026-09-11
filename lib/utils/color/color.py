COLOR_BLACK = (0,0,0)
COLOR_RED = (255,0,0)
COLOR_ORANGE = (255,127,0)
COLOR_YELLOW = (255,255,0)
COLOR_LIGHT_GREEN = (127,255,0)
COLOR_GREEN = (0,255,0)
COLOR_TURQUOISE = (0,255,127)
COLOR_CYAN = (0,255,255)
COLOR_LIGHT_BLUE = (0,127,255)
COLOR_BLUE = (0,0,255)
COLOR_VIOLET = (127,0,255)
COLOR_MAGENTA = (255,0,255)
COLOR_RASPBERRY = (255,0,127)
COLOR_WHITE = (255,255,255)

colors = {
    "black": COLOR_BLACK,
    "red": COLOR_RED,
    "orange": COLOR_ORANGE,
    "yellow": COLOR_YELLOW,
    "light_green": COLOR_LIGHT_GREEN,
    "green": COLOR_GREEN,
    "turquoise": COLOR_TURQUOISE,
    "cyan": COLOR_CYAN,
    "light_blue": COLOR_LIGHT_BLUE,
    "blue": COLOR_BLUE,
    "violet": COLOR_VIOLET,
    "magenta": COLOR_MAGENTA,
    "raspberry": COLOR_RASPBERRY,
    "white": COLOR_WHITE
}

def adjust_color_intensity(color:tuple, intensity:float):
    if intensity < 0 or intensity > 1:
        raise ValueError(f"Invalid intensity: {intensity}. It must be float between 0 and 1.")

    return tuple(map(lambda v: round(v*intensity), color))