from color import get_random_color
from . import utils


def light_random(board):

    board.board = get_random_color(board.board)
    utils.apply_light(board)
