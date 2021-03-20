color_map = {
    "black": "0",
    "brown": "1",
    "red": "2",
    "orange": "3",
    "yellow": "4",
    "green": "5",
    "blue": "6",
    "violet": "7",
    "grey": "8",
    "white": "9",
}


def value(colors):
    colors = colors[:2]
    return int("".join([color_map[color] for color in colors]))
