from color import get_random_color
from . import utils

def light_random(board):
    devices=board.devices
    devices_count=board.devices_count

    current_color = get_random_color()
    for i in range(devices_count):
        utils.change_light(devices[i], current_color,board.devices_light_count[i])
    
    for i in range(devices_count):
        utils.apply_device(devices[i], current_color,board.auraSdk)
