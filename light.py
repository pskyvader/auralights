from light_modes import *
import win32com.client
import config
import light_board


auraSdk = win32com.client.Dispatch("aura.sdk.1")
auraSdk.SwitchMode()
board = light_board.light_board(auraSdk)


def update_light():
    if config.MODE == config.MODES.RANDOM:
        light_random.light_random(board)
    elif config.MODE == config.MODES.SCREEN:
        light_screen.light_screen(board)
    elif config.MODE == config.MODES.SCREEN_RAINBOW_HORIZONTAL:
        light_screen_rainbow_horizontal.light_screen_rainbow_horizontal(board)
