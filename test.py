import win32com.client

auraSdk = win32com.client.Dispatch("aura.sdk.1")

auraSdk.SwitchMode()

devices = auraSdk.Enumerate(0)   # 0 means ALL
for dev in devices:                      # Use enumeration
    print(dev,dev.Lights.count,dev.name,dev.Type,dev.width,dev.height)
    for i in range(dev.Lights.Count):    # Use index
        current_light=dev.lights(i)
        # current_light.color = 0x0000FF00
        print(current_light.name,hex(current_light.color),current_light.red)

print("asd")