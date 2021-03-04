from color import get_random_color,set_color_board
from . import utils


def light_random(board):
    color=get_random_color()
    set_color_board(board.board,color)
    utils.apply_light(board)
