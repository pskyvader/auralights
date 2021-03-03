class MODES:
    RANDOM = 1
    SCREEN = 2
    SCREEN_RAINBOW_HORIZONTAL = 3


class DIRECTIONS:
    FORWARDS = 1
    BACKWARDS = 2


position = (3840, 720)  # pixel for get color from screen
pause = 0.01  # pause between every update. in seconds
width = 24
height = 8


device_list = [
    {
        "name": "AddressableStrip 1",
        "lights": [
            [0, 0],
            [0, 1],
            [0, 2],
            [0, 3],
            [0, 4],
            [0, 5],
            [0, 6],
            [0, 7],
            [0, 8],
            [0, 9],
            [0, 10],
            [0, 11],
        ],
        "active": True,
    },
    {"name": "Mainboard_Master", "count": 10, "active": True},
    {"name": "Dram 1", "count": 5, "active": True},
    {"name": "Dram 2", "count": 5, "active": True},
    {"name": "AddressableStrip 2", "count": 24, "active": True},
    {"name": "MousePad", "count": 15, "active": True},
]

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


MODE = MODES.SCREEN
DIRECTION = DIRECTIONS.FORWARDS
