from color import get_color_from_screen_pixel,set_color_board
from . import utils


def light_screen(board):
    color = get_color_from_screen_pixel()
    set_color_board(board.board,color)
    utils.apply_light(board)