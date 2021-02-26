from color import get_color_from_screen_pixel
from . import utils
import config


def light_screen_rainbow_horizontal(devices,devices_light_count,previous_colors,auraSdk):
    devices_count=len(devices)
    current_color = get_color_from_screen_pixel()
    if config.DIRECTION==config.DIRECTIONS.FORWARDS:
        # insert at the begining
        previous_colors.pop()
        previous_colors.insert(0, current_color)
    elif config.DIRECTION==config.DIRECTIONS.BACKWARDS:
        # insert at the end
        previous_colors.pop(0)
        previous_colors.append(current_color)

    for i in range(devices_count):
        utils.change_light(devices[i], previous_colors[i],devices_light_count[i])
    
    for i in range(devices_count):
        utils.apply_device(devices[i], previous_colors[i],auraSdk)

