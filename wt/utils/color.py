import ast
import re
from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)


def convert_rgb_to_names(str_rgb):
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))

    kdt_db = KDTree(rgb_values)

    rgb_tuple = ast.literal_eval(re.search('rgb(.*)none', str(str_rgb)).group(1).strip())

    distance, index = kdt_db.query(rgb_tuple)
    return names[index]
