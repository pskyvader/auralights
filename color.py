from PIL import ImageGrab
import random
import config


def get_color_from_screen_pixel():
    position=config.position
    rgb = get_pixel_colour(position[0], position[1])
    return formatted_color(rgb)

def get_random_color(board):
    selected = int(random.random() * 3)
    r = get_random(selected, 0)
    b = get_random(selected, 1)
    g = get_random(selected, 2)
    rgb = (r, g, b)
    current_color= formatted_color(rgb)
    for i in range(len(board)):
        row=board[i]
        for j in range(len(row)):
            board[i][j]=current_color
    return board

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


def get_pixel_colour(i_x, i_y):
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
