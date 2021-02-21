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
        current_light.color = 0x00ffff00
    dev.Apply()


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()

time.sleep(5)
print("asd")
