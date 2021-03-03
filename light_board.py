import config


class device:
    lights=[]
    def __init__(self, dev,element) -> None:
        self.name=element['name']
        self.device=dev
        for i in range(len(element['lights'])):  # Use index
            current_light = {'light':dev.lights(i),'position':element['lights'][i]}
            if current_light["position"][0]>config.height:
                current_light["position"][0]=config.height

            if current_light["position"][1]>config.width:
                current_light["position"][1]=config.width

            self.lights.append(current_light)
            


def get_device_list(devs):
    devices = []
    for dev in devs:
        element=next( ( item for item in config.device_list if item["name"] == dev.name and item["active"] ), None, )
        position = next( ( i for i, item in enumerate(config.device_list) if item["name"] == dev.name and item["active"] ), None, )
        if position != None:
            devices.append(device(dev,element))

    return devices


class light_board:
    board = []
    devices = None

    def __init__(self, auraSdk) -> None:
        self.auraSdk=auraSdk
        devs = auraSdk.Enumerate(0)  # 0 means ALL
        self.devices = get_device_list(devs)
        self.previous_colors = []
        self.devices_count=len(self.devices)
        for i in range(self.devices_count):
            self.previous_colors.append(0)

        for i in range(config.height):
            self.board.append([])
            for j in range(config.width):
                self.board[i].append(0x00FFFFFF)
