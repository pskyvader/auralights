class MODES:
    RANDOM=1
    SCREEN=2
    SCREEN_RAINBOW_HORIZONTAL=3
class DIRECTIONS:
    FORWARDS=1
    BACKWARDS=2

position = (3840, 720)  # pixel for get color from screen
pause=0.01 #pause between every update. in seconds
width=24
height=8


device_list = [
    {"name": "AddressableStrip 1", "count": 12,"active":True},
    {"name": "Mainboard_Master", "count": 10,"active":True},
    {"name": "Dram 1", "count": 5,"active":True},
    {"name": "Dram 2", "count": 5,"active":True},
    {"name": "AddressableStrip 2", "count": 24,"active":True},
    {"name": "MousePad", "count": 15,"active":True},
]

def get_device(name):
    return next((item for item in device_list if item["name"] == name and item["active"]), None)

def get_device_list(devs):
    devices=[]
    devices_light_count=[]
    for i in range(len(device_list)):
        devices.append(None)
        devices_light_count.append(None)


    for dev in devs:
        position=next((i for i, item in enumerate(device_list) if item["name"] == dev.name and item["active"]), None)
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


MODE=MODES.RANDOM
DIRECTION=DIRECTIONS.FORWARDS