from PIL import ImageGrab
import random
import config


def get_color_from_screen_pixel():
    position = config.position
    rgb = get_pixel_color(position[0], position[1])
    return formatted_color(rgb)


def get_random_color():
    selected = int(random.random() * 3)
    r = get_random(selected, 0)
    b = get_random(selected, 1)
    g = get_random(selected, 2)
    rgb = (r, g, b)
    return formatted_color(rgb)


def get_random(selected, pos):
    if selected != pos:
        return int(random.random() * 255)
    else:
        return 255 if random.random() > 0.5 else 0


def formatted_color(color):
    print(color)
    r, g, b = color
    final_color = "0x00%02x%02x%02x" % (b, g, r)
    final_color = int(final_color, 16)
    return final_color


def get_pixel_color(i_x, i_y):
    box = (i_x - 1, i_y - 1, i_x, i_y)
    image0 = ImageGrab.grab(
        bbox=box,
        include_layered_windows=False,
        all_screens=True,
        xdisplay=None,
    )
    # size = image0.size
    # print(size)
    return image0.load()[0, 0]


def set_color_board(board, color):
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            board[i][j] = color
    return board


def set_color_board_horizontal(board, color):
    if config.DIRECTION == config.DIRECTIONS.FORWARDS:
        # insert at the begining
        for i in range(len(board)):
            row = board[i]
            row.pop()
            row.insert(0, color)

    elif config.DIRECTION == config.DIRECTIONS.BACKWARDS:
        # insert at the end
        for i in range(len(board)):
            row = board[i]
            row.pop(0)
            row.append(color)
    return board