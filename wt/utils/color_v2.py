import ast
import re
from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)


def convert_rgb_to_names(hex_color):
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))

    kdt_db = KDTree(rgb_values)
    if re.match('#', hex_color, re.I) is None:
        hex_color_edited = '#' + hex_color
    rgb_tuple = hex_to_rgb(hex_color_edited)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index]
