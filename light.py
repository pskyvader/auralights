from light_modes import *
import win32com.client
import config


auraSdk = win32com.client.Dispatch("aura.sdk.1")
auraSdk.SwitchMode()
devs = auraSdk.Enumerate(0)  # 0 means ALL
devices, devices_light_count = config.get_device_list(devs)
devices_count = len(devices)
previous_colors = []
for i in range(devices_count):
    previous_colors.append(0)


def update_light():
    if config.MODE == config.MODES.RANDOM:
        light_random.light_random(devices, devices_light_count, auraSdk)
    elif config.MODE == config.MODES.SCREEN:
        light_screen.light_screen(devices, devices_light_count, auraSdk)
    elif config.MODE == config.MODES.SCREEN_RAINBOW_HORIZONTAL:
        light_screen_rainbow_horizontal.light_screen_rainbow_horizontal(
            devices, devices_light_count, previous_colors, auraSdk
        )
