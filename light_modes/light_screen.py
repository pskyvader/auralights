from color import get_color_from_screen_pixel
from . import utils


def light_screen(devices, devices_light_count, auraSdk):
    devices_count = len(devices)
    current_color = get_color_from_screen_pixel()
    for i in range(devices_count):
        utils.change_light(devices[i], current_color, devices_light_count[i])

    for i in range(devices_count):
        utils.apply_device(devices[i], current_color, auraSdk)
