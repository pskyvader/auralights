class MODES:
    RANDOM=1
    SCREEN=2
    SCREEN_RAINBOW_HORIZONTAL=3
class DIRECTIONS:
    FORWARDS=1
    BACKWARDS=2

position = (3840, 720)  # pixel for get color from screen
pause=0.01 #pause between every update. in seconds


device_list = [
    {"name": "AddressableStrip 1", "count": 12},
    {"name": "Mainboard_Master", "count": 10},
    {"name": "Dram 1", "count": 5},
    {"name": "Dram 2", "count": 5},
    {"name": "AddressableStrip 2", "count": 24},
    {"name": "MousePad", "count": 15},
]

def get_device(name):
    return next((item for item in device_list if item["name"] == name), None)

def get_device_list(devs):
    devices=[]
    devices_light_count=[]
    for i in range(len(device_list)):
        devices.append(None)
        devices_light_count.append(None)


    for dev in devs:
        position=next((i for i, item in enumerate(device_list) if item["name"] == dev.name), None)
        count=get_device(dev.name)['count']
        if position!=None:
            devices[position]=dev
            devices_light_count[position]=count

    return (devices,devices_light_count)

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


MODE=MODES.SCREEN_RAINBOW_HORIZONTAL
DIRECTION=DIRECTIONS.FORWARDS