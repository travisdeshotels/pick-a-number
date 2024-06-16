import json
import os
import requests
from ..exception.badinputexception import BadInputException


class PlayerConfig:
    filename = ""
    url = ''

    def __init__(self, filename):
        self.filename = filename

    def register(self):
        user_name = input("Enter user name: ")
        email = input("Enter email address: ")
        response = requests.post(url=f'{self.url}/register',
                                 data=json.dumps({'userName': user_name, 'email': email}))
        return response.json()['secretId']

    def is_player_configured(self):
        return os.path.isfile(self.filename)

    def load_player_from_config(self):
        with open(self.filename, "r") as config:
            return config.read().split(",")

    def get_secret_id(self):
        register_choice = input("(R)egister\n(E)nter secret id: ")
        if register_choice == 'R':
            secret_id = self.register()
        elif register_choice == 'E':
            secret_id = input("Enter your secret_id: ")
        else:
            raise BadInputException("Invalid choice was entered!")
        return secret_id

    def create_config_file(self):
        self.url = input("Enter host url: ")
        secret_id = self.get_secret_id()
        with open(self.filename, "w") as config:
            config.write(f"{self.url},{secret_id}")
            return self.url, secret_id

    def get_config_values(self):
        if self.is_player_configured():
            return self.load_player_from_config()
        else:
            return self.create_config_file()
