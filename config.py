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
            [0, 2],
            [0, 4],
            [0, 6],
            [0, 8],
            [0, 10],
            [0, 12],
            [0, 14],
            [0, 16],
            [0, 18],
            [0, 20],
            [0, 22],
        ],
        "active": True,
    },
    {
        "name": "Mainboard_Master",
        "lights": [
            [2, 0],
            [2, 2],
            [3, 4],
            [3, 6],
            [4, 12],
            [4, 14],
            [5, 16],
            [6, 18],
            [3, 23],
            [6, 23],
        ],
        "active": True,
    },
    {
        "name": "Dram 1",
        "lights": [
            [2, 11],
            [3, 11],
            [4, 11],
            [5, 11],
            [6, 11],
        ],
        "active": True,
    },
    {
        "name": "Dram 2",
        "lights": [
            [2, 13],
            [3, 13],
            [4, 13],
            [5, 13],
            [6, 13],
        ],
        "active": True,
    },
    {
        "name": "AddressableStrip 2",
        "lights": [
            [7, 0],
            [7, 1],
            [7, 2],
            [7, 3],
            [7, 4],
            [7, 5],
            [7, 6],
            [7, 7],
            [7, 8],
            [7, 9],
            [7, 10],
            [7, 11],
            [7, 12],
            [7, 13],
            [7, 14],
            [7, 15],
            [7, 16],
            [7, 17],
            [7, 18],
            [7, 19],
            [7, 20],
            [7, 21],
            [7, 22],
            [7, 23],
        ],
        "active": True,
    },
    {
        "name": "MousePad",
        "lights": [
            [7, 0],
            [7, 5],
            [7, 11],
            [7, 17],
            [7, 23],
            [5, 23],
            [3, 23],
            [0, 23],
            [0, 17],
            [0, 13],
            [0, 9],
            [0, 5],
            [0, 0],
            [3, 0],
            [5, 0],
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
DIRECTION = DIRECTIONS.BACKWARDS
