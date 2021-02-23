import time
from os import system
from light import update_light
import config


try:
    while True:
        update_light()
        print("ctrl-c to exit")
        time.sleep(config.pause)
        system("cls")


except KeyboardInterrupt:
    print("Stopped")
