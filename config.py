class MODES:
    RANDOM = 1
    SCREEN = 2
    SCREEN_RAINBOW_HORIZONTAL = 3


class DIRECTIONS:
    FORWARDS = 1
    BACKWARDS = 2


position = (3840, 720)  # pixel for get color from screen
pause = 0.10  # pause between every update. in seconds
width = 120
height = 8


device_list = [
    {
        "name": "AddressableStrip 1",
        "lights": [
            [0, 0],
            [0, 9],
            [0, 19],
            [0, 29],
            [0, 39],
            [0, 49],
            [0, 59],
            [0, 69],
            [0, 79],
            [0, 89],
            [0, 99],
            [0, 109],
        ],
        "active": True,
    },
    {
        "name": "Mainboard_Master",
        "lights": [
            [2, 0],
            [2, 15],
            [3, 30],
            [3, 45],

            [4, 60],
            [4, 75],
            [5, 90],
            [6, 115],

            [3, 119],
            [6, 119],
        ],
        "active": True,
    },
    {
        "name": "Dram 1",
        "lights": [
            [2, 40],
            [3, 40],
            [4, 40],
            [5, 40],
            [6, 40],
        ],
        "active": True,
    },
    {
        "name": "Dram 2",
        "lights": [
            [2, 80],
            [3, 80],
            [4, 80],
            [5, 80],
            [6, 80],
        ],
        "active": True,
    },
    {
        "name": "AddressableStrip 2",
        "lights": [
            [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9],
            [7, 10], [7, 11], [7, 12], [7, 13], [7, 14], [7, 15], [7, 16], [7, 17], [7, 18], [7, 19],
            [7, 20], [7, 21], [7, 22], [7, 23], [7, 24], [7, 25], [7, 26], [7, 27], [7, 28], [7, 29],
            [7, 30], [7, 31], [7, 32], [7, 33], [7, 34], [7, 35], [7, 36], [7, 37], [7, 38], [7, 39],

            [7, 40], [7, 41], [7, 42], [7, 43], [7, 44], [7, 45], [7, 46], [7, 47], [7, 48], [7, 49],
            [7, 50], [7, 51], [7, 52], [7, 53], [7, 54], [7, 55], [7, 56], [7, 57], [7, 58], [7, 59],
            [7, 60], [7, 61], [7, 62], [7, 63], [7, 64], [7, 65], [7, 66], [7, 67], [7, 68], [7, 69],
            [7, 70], [7, 71], [7, 72], [7, 73], [7, 74], [7, 75], [7, 76], [7, 77], [7, 78], [7, 79],

            [7, 80], [7, 81], [7, 82], [7, 83], [7, 84], [7, 85], [7, 86], [7, 87], [7, 88], [7, 89],
            [7, 90], [7, 91], [7, 92], [7, 93], [7, 94], [7, 95], [7, 96], [7, 97], [7, 98], [7, 99],
            [7, 100], [7, 101], [7, 102], [7, 103], [7, 104], [7, 105], [7, 106], [7, 107], [7, 108], [7, 109],
            [7, 110], [7, 111], [7, 112], [7, 113], [7, 114], [7, 115], [7, 116], [7, 117], [7, 118], [7, 119],
            

        ],
        "active": True,
    },
    {
        "name": "MousePad",
        "lights": [
            [7, 0],
            [7, 30],
            [7, 60],
            [7, 90],
            
            [7, 119],
            [5, 119],
            [3, 119],
            [0, 119],

            [0, 90],
            [0, 60],
            [0, 30],
            [0, 15],

            [0, 0],
            [3, 0],
            [5, 0],
        ],
        "active": True,
    },
]

# motherboard_list = [
#     "Back IO",
#     "Back IO",
#     "Back IO",
#     "Back IO",
#     "PCH",
#     "PCH",
#     "PCH",
#     "PCH",
#     "RGB HEADER",
#     "RGB HEADER",
# ]


MODE = MODES.SCREEN_RAINBOW_HORIZONTAL
DIRECTION = DIRECTIONS.FORWARDS
