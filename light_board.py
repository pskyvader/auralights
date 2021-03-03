import config


def get_device(name):
    return next( ( item for item in config.device_list if item["name"] == name and item["active"] ), None, )


def get_device_list(devs):
    devices = []
    devices_light_count = []
    for i in range(len(config.device_list)):
        devices.append(None)
        devices_light_count.append(None)

    for dev in devs:
        position = next( ( i for i, item in enumerate(config.device_list) if item["name"] == dev.name and item["active"] ), None, )
        count = get_device(dev.name)["count"]
        if position != None:
            devices[position] = dev
            devices_light_count[position] = count

    return (devices, devices_light_count)


class light_board:
    board = []
    devices = None

    def __init__(self, auraSdk) -> None:
        self.auraSdk=auraSdk
        devs = auraSdk.Enumerate(0)  # 0 means ALL
        self.devices, self.devices_light_count = get_device_list(devs)
        self.previous_colors = []
        self.devices_count=len(self.devices)
        for i in range(self.devices_count):
            self.previous_colors.append(0)


        width = config.width
        height = config.height
        
        for i in range(width):
            self.board.append([])
            for j in range(height):
                self.board[i].append(0x00FFFFFF)
