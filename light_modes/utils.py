from colr import color
def change_light(dev, current_color,lights_count):
    bar = ""
    for i in range(lights_count):  # Use index
        current_light = dev.lights(i)
        current_light.color = current_color
        rgb = (current_light.red, current_light.green, current_light.blue)
        bar += color("|", fore=rgb, back=rgb)
    print(bar)


def apply_device(dev, current_color,auraSdk):
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
