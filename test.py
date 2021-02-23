import time
from os import system
from light import update_light


try:
    while True:
        update_light()
        print("ctrl-c to exit")
        time.sleep(0.05)
        system("cls")


except KeyboardInterrupt:
    print("Stopped")
