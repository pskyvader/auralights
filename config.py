class MODES:
    RANDOM=1
    SCREEN_RAINBOW_HORIZONTAL=2
class DIRECTIONS:
    FORWARDS=1
    BACKWARDS=2

position = (3840, 720)  # pixel for get color from screen
pause=0.5 #pause between every update. in seconds





device_list = [
    {"name": "Dram 1", "count": 5},
    {"name": "Dram 2", "count": 5},
    {"name": "MousePad", "count": 15},
    {"name": "Mainboard_Master", "count": 10},
    {"name": "AddressableStrip 1", "count": 12},
    {"name": "AddressableStrip 2", "count": 24},
]

def get_device(name):
    return next((item for item in device_list if item["name"] == name), None)

def get_device_position(name):
    next((i for i, item in enumerate(device_list) if item["name"] == name), None)


motherboard_list = [
    "Back IO",
    "Back IO",
    "Back IO",
    "Back IO",
    "PCH",
    "PCH",
    "PCH",
    "PCH",
    "RGB HEADER",
    "RGB HEADER",
]


MODE=MODES.RANDOM
DIRECTION=DIRECTIONS.BACKWARDS