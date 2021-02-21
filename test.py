import win32com.client

auraSdk = win32com.client.Dispatch("aura.sdk.1")

auraSdk.SwitchMode()

devices = auraSdk.Enumerate(0)   # 0 means ALL
for dev in devices:                      # Use enumeration
    value=auraSdk.Enumerate(dev.Type)
    print(value.count,value.item,)
    print(dev,dev.Lights,dev.name,dev.Type)

print("asd")