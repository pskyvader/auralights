import win32com.client
import struct
import time
from colr import color
import sys

auraSdk = win32com.client.Dispatch("aura.sdk.1")

# auraSdk.SwitchMode()

devices = auraSdk.Enumerate(0)   # 0 means ALL

def get_light():
    
    current_light=devices(3).lights(0)
    rgb = (current_light.blue,current_light.green,current_light.red)
    print(rgb,hex(current_light.color))

    for dev in devices:                      # Use enumeration
        # print(dev,dev.Lights.count,dev.name,dev.Type,dev.width,dev.height)
        # bar=dev.name
        bar=""
        for i in range(dev.Lights.Count):    # Use index
            current_light=dev.lights(i)
            # current_light.color = 0x0000FF00
            # print(current_light.name,current_light.color,hex(current_light.color))
            rgb = (current_light.blue,current_light.green,current_light.red)
            # print(rgb)
            # rgb=bytes.hex(struct.pack('BBB',*rgb))
            # rgb=hex(current_light.color)
            bar+=color('|',fore=rgb, back=rgb)
            # current_light.color=hex(0)
            # current_light.color = 0x00ffff00
        # dev.Apply()
        print(bar)


try:
    while(True):
        get_light()
        print("ctrl-c to exit")
        time.sleep(1)
        for i in range(devices.count+2):
            sys.stdout.write("\033[F") # Cursor up one line
except KeyboardInterrupt:
    print("Stopped")
