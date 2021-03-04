class MODES:
    RANDOM = 1
    SCREEN = 2
    SCREEN_RAINBOW_HORIZONTAL = 3


class DIRECTIONS:
    FORWARDS = 1
    BACKWARDS = 2


position = (3840, 720)  # pixel for get color from screen
pause = 5  # pause between every update. in seconds
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
    {
        "name": "Mainboard_Master",
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
        ],
        "active": True,
    },
    {
        "name": "Dram 1",
        "lights": [
            [0, 0],
            [0, 1],
            [0, 2],
            [0, 3],
            [0, 4],
        ],
        "active": True,
    },
    {
        "name": "Dram 2",
        "lights": [
            [0, 0],
            [0, 1],
            [0, 2],
            [0, 3],
            [0, 4],
        ],
        "active": True,
    },
    {
        "name": "AddressableStrip 2",
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
            [0, 12],
            [0, 13],
            [0, 14],
            [0, 15],
            [0, 16],
            [0, 17],
            [0, 18],
            [0, 19],
            [0, 20],
            [0, 21],
            [0, 22],
            [0, 23],
        ],
        "active": True,
    },
    {
        "name": "MousePad",
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
            [0, 12],
            [0, 13],
            [0, 14],
        ],
        "active": True,
    },
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


MODE = MODES.SCREEN_RAINBOW_HORIZONTAL
DIRECTION = DIRECTIONS.FORWARDS
