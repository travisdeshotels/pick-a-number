def get_config_from_file():
    filename = '.player_config'
    with open(filename, "r") as config:
        x, y = config.read().split(",")
        return x, y
