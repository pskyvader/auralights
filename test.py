import win32com.client
import random
import time
from colr import color
import sys
from PIL import ImageGrab
from os import system

auraSdk = win32com.client.Dispatch("aura.sdk.1")

auraSdk.SwitchMode()

devices = auraSdk.Enumerate(0)  # 0 means ALL

devices_count = devices.count
current_device = 0
previous_colors = []
for i in range(devices_count):
    previous_colors.append(0)


def get_light():
    current_color = set_color()
    previous_colors.pop()
    previous_colors.insert(0, current_color)

    # current_light=devices(0).lights(0)
    # rgb = (current_light.red,current_light.green,current_light.blue)
    # print(rgb,hex(current_light.color),current_light)

    for i in range(devices_count):                      # Use enumeration
         change_color(devices(i),previous_colors[i])
    # change_color(devices(current_device), current_color)


def change_color(dev, current_color):
    # print(dev,dev.Lights.count,dev.name,dev.Type,dev.width,dev.height)
    # bar=dev.name
    bar = ""
    for i in range(dev.Lights.count):  # Use index
        current_light = dev.lights(i)
        # print(rgb,hex(current_light.color),current_light.color)
        current_light.color = current_color
        rgb = (current_light.red, current_light.green, current_light.blue)
        bar += color("|", fore=rgb, back=rgb)
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
    print(bar)


def set_color(random=False):

    if random:
        selected = int(random.random() * 3)
        r = (
            int(random.random() * 255)
            if selected != 0
            else 255
            if random.random() > 0.5
            else 0
        )
        b = (
            int(random.random() * 255)
            if selected != 1
            else 255
            if random.random() > 0.5
            else 0
        )
        g = (
            int(random.random() * 255)
            if selected != 2
            else 255
            if random.random() > 0.5
            else 0
        )
        rgb = (r, g, b)
    else:
        rgb = get_pixel_colour(3840, 720)
    return formatted_color(rgb)


def formatted_color(color):
    print(color)
    r, g, b = color
    final_color = "0x00%02x%02x%02x" % (b, g, r)
    final_color = int(final_color, 16)
    return final_color


def get_pixel_colour(i_x, i_y):
    image0 = ImageGrab.grab(
        bbox=(i_x - 1, i_y - 1, i_x, i_y),
        include_layered_windows=False,
        all_screens=True,
        xdisplay=None,
    )
    size = image0.size
    # print(size)
    return image0.load()[0, 0]

dev=devices(3)
dev.lights(1).color=0
dev.Apply()

time.sleep(10)

try:
    while False:
        get_light()
        print("ctrl-c to exit")
        time.sleep(0.1)
        system("cls")


except KeyboardInterrupt:
    print("Stopped")
