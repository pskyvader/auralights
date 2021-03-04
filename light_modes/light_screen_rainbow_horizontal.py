from color import get_color_from_screen_pixel,set_color_board_horizontal
from . import utils


def light_screen_rainbow_horizontal(board):
    color = get_color_from_screen_pixel()

    set_color_board_horizontal(board.board,color)
    utils.apply_light(board)