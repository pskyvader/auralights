from colr import color

def apply_light(board):
    for i in range(board.devices_count):
        change_light(board.devices[i], board.board)

    for i in range(board.devices_count):
        apply_device(board.devices[i], board.auraSdk)


def change_light(device, board):
    bar = ""
    # print(len(device.lights))
    for i in range(len(device.lights)):  # Use index
        current_light = device.lights[i]
        x=current_light['position'][0]
        y=current_light['position'][1]
        current_light['light'].color = board[x][y]
        rgb = (current_light['light'].red, current_light['light'].green, current_light['light'].blue)
        bar += color("|", fore=rgb, back=rgb)
    print(bar)


def apply_device(dev,auraSdk):
    try:
        dev.device.Apply()
    except Exception as e:
        print(e)
        print(dev.name)
        print("-----")
        print("-----")
        print("-----")
        print("-----")
        auraSdk.SwitchMode()
