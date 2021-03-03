from color import get_color_from_screen_pixel
from . import utils


def light_screen(board):
    devices=board.devices
    devices_count = board.devices_count
    current_color = get_color_from_screen_pixel()
    for i in range(devices_count):
        utils.change_light(devices[i], current_color, board.devices_light_count[i])

    for i in range(devices_count):
        utils.apply_device(devices[i], current_color, board.auraSdk)
