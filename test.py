import win32com.client
import struct
import time
from colr import color

auraSdk = win32com.client.Dispatch("aura.sdk.1")

auraSdk.SwitchMode()

devices = auraSdk.Enumerate(0)   # 0 means ALL

def get_light():
    for dev in devices:                      # Use enumeration
        # print(dev,dev.Lights.count,dev.name,dev.Type,dev.width,dev.height)
        bar=dev.name
        for i in range(dev.Lights.Count):    # Use index
            current_light=dev.lights(i)
            # current_light.color = 0x0000FF00
            # print(current_light.name,current_light.color,hex(current_light.color))
            rgb = (current_light.red,current_light.green,current_light.blue)
            # print(rgb)
            rgb=bytes.hex(struct.pack('BBB',*rgb))
            bar+=color('|',fore=rgb, back=rgb)
            # current_light.color=hex(0)
            # current_light.color = 0x00ffff00
        # dev.Apply()
        print(bar)


try:
    while(True):
        get_light()
        print("ctrl-c")
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped")
