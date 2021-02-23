import win32com.client
from colr import color
from color import get_color_from_screen_pixel,get_random_color
import config

auraSdk = win32com.client.Dispatch("aura.sdk.1")
auraSdk.SwitchMode()
devs = auraSdk.Enumerate(0)  # 0 means ALL
devices,devices_light_count=config.get_device_list(devs)
devices_count = len(devices)
previous_colors = []
for i in range(devices_count):
    previous_colors.append(0)




def update_light():
    if config.MODE==config.MODES.RANDOM:
        update_light_random()
    elif config.MODE==config.MODES.SCREEN:
        update_light_screen()
    elif config.MODE==config.MODES.SCREEN_RAINBOW_HORIZONTAL:
        update_light_screen_rainbow_horizontal()
        

def update_light_random():
    current_color = get_random_color()
    for i in range(devices_count):
        change_light(devices[i], current_color,devices_light_count[i])
    
    for i in range(devices_count):
        apply_device(devices[i], current_color)

def update_light_screen():
    current_color = get_color_from_screen_pixel()
    for i in range(devices_count):
        change_light(devices[i], current_color,devices_light_count[i])
    
    for i in range(devices_count):
        apply_device(devices[i], current_color)


def update_light_screen_rainbow_horizontal():
    current_color = get_color_from_screen_pixel()
    if config.DIRECTION==config.DIRECTIONS.FORWARDS:
        # insert at the begining
        previous_colors.pop()
        previous_colors.insert(0, current_color)
    elif config.DIRECTION==config.DIRECTIONS.BACKWARDS:
        # insert at the end
        previous_colors.pop(0)
        previous_colors.append(current_color)

    for i in range(devices_count):
        change_light(devices[i], previous_colors[i],devices_light_count[i])
    
    for i in range(devices_count):
        apply_device(devices[i], previous_colors[i])



def change_light(dev, current_color,lights_count):
    
    bar = ""
    for i in range(lights_count):  # Use index
        current_light = dev.lights(i)
        current_light.color = current_color
        rgb = (current_light.red, current_light.green, current_light.blue)
        bar += color("|", fore=rgb, back=rgb)
    print(bar)


def apply_device(dev, current_color):
    try:
        dev.Apply()
    except Exception as e:
        print(e)
        print(current_color)
        print(dev.name)
        print("-----")
        print("-----")
        print("-----")
        print("-----")
        auraSdk.SwitchMode()
