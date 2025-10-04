def get_config_from_file():
    filename = '.player_config'
    with open(filename, "r") as config:
        x, y = config.read().split(",")
        return x, y

def is_player_config_present():
    from pathlib import Path
    my_file = Path(".player_config")
    return my_file.is_file()
