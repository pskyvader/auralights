from color import get_random_color
from . import utils

def light_random(devices,devices_light_count,auraSdk):
    devices_count=len(devices)
    current_color = get_random_color()
    for i in range(devices_count):
        utils.change_light(devices[i], current_color,devices_light_count[i])
    
    for i in range(devices_count):
        utils.apply_device(devices[i], current_color,auraSdk)

def __init__():
    return light_random