import win32com.client
from colr import color
from color import get_color

auraSdk = win32com.client.Dispatch("aura.sdk.1")
auraSdk.SwitchMode()
devices = auraSdk.Enumerate(0)  # 0 means ALL
devices_count = devices.count
previous_colors = []
for i in range(devices_count):
    previous_colors.append(0)

def update_light():
    current_color = get_color()
    # insert at the begining
    # previous_colors.pop()
    # previous_colors.insert(0, current_color)

    # insert at the end
    previous_colors.pop(0)
    previous_colors.append(current_color)

    for i in range(devices_count):  # Use enumeration
        change_light(devices(i), previous_colors[i])
        apply_device(devices(i), previous_colors[i])




def change_light(dev, current_color):
    bar = ""
    for i in range(dev.Lights.count):  # Use index
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
