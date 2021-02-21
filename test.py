import win32com.client
import random
import time
from colr import color
import sys

auraSdk = win32com.client.Dispatch("aura.sdk.1")

auraSdk.SwitchMode()

devices = auraSdk.Enumerate(0)   # 0 means ALL

def get_light():
    current_color=set_color()
    
    # current_light=devices(0).lights(0)
    # rgb = (current_light.red,current_light.green,current_light.blue)
    # print(rgb,hex(current_light.color),current_light)

    for dev in devices:                      # Use enumeration
        # print(dev,dev.Lights.count,dev.name,dev.Type,dev.width,dev.height)
        # bar=dev.name
        bar=""
        for i in range(dev.Lights.count):    # Use index
            current_light=dev.lights(i)
            # print(rgb,hex(current_light.color),current_light.color)
            current_light.color = current_color
            rgb = (current_light.red,current_light.green,current_light.blue)
            bar+=color('|',fore=rgb, back=rgb)
        dev.Apply()
        print(bar)


def set_color():
    r =int(random.random()*255)
    b = int(random.random()*255)
    g = int(random.random()*255)

    color='0x00%02x%02x%02x' % (b, g, r)
    return color
    print(color)
    color = int(color, 16)
    color = hex(color)
    print(color)
    return color
    


try:
    while(True):
        get_light()
        print("ctrl-c to exit")
        time.sleep(1)
        for i in range(devices.count+1):
            sys.stdout.write("\033[F") # Cursor up one line
except KeyboardInterrupt:
    print("Stopped")
