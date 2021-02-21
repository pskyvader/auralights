import win32com.client
import struct
import time

auraSdk = win32com.client.Dispatch("aura.sdk.1")

auraSdk.SwitchMode()

devices = auraSdk.Enumerate(0)   # 0 means ALL
for dev in devices:                      # Use enumeration
    print(dev,dev.Lights.count,dev.name,dev.Type,dev.width,dev.height)
    for i in range(dev.Lights.Count):    # Use index
        current_light=dev.lights(i)
        # current_light.color = 0x0000FF00
        print(current_light.name,current_light.color,hex(current_light.color))
        rgb = (current_light.blue,current_light.green,current_light.red)
        print(bytes.hex(struct.pack('BBB',*rgb)))
        # current_light.color=hex(0)
        dev.Lights(i).color = 0xFFff0000
    dev.Apply()

time.sleep(5)
print("asd")
