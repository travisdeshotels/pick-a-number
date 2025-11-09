import json
import requests
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout


API_CONNECTION_ERROR = "Error: unable to connect to the API."

class RestCaller:
    api_url = ""
    secret_id = ""

    def __init__(self, config_tuple):
        self.api_url = config_tuple[0]
        self.secret_id = config_tuple[1]

    def set_api_url(self, api_url):
        self.api_url = api_url

    def get_api_url(self):
        return self.api_url

    def submit_guess(self, guess):
        try:
            return requests.get(headers={'Secret': self.secret_id}, url=f'{self.api_url}?guess={guess}').json()
        except requests.exceptions.ConnectionError:
            return None

    def is_api_healthy(self):
        return self.get_score_board() is not None

    def get_score_board(self):
        response = None
        try:
            res = requests.get(url=f'{self.api_url}/scores')
            if res.status_code == 200:
                response = res.json()
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            pass
        return response

    def register(self, username, email):
        try:
            response = requests.post(url=f'{self.api_url}/register',
                                    headers={'Content-Type': 'application/json'},
                                    data=json.dumps({'userName': f'{username}',
                                                     'email': f'{email}'})
                                    )
            return response.status_code, response.json()
        except requests.exceptions.MissingSchema:
            return None, None


class ConfigUtil:
    filename = ""

    def __init__(self):
        self.filename = '.player_config'

    def get_config_from_file(self):
        with open(self.filename, "r") as config:
            x, y = config.read().split(",")
            return x, y

    def is_player_config_present(self):
        from pathlib import Path
        my_file = Path(self.filename)
        return my_file.is_file()


def get_main_layout(*layouts):
    vertical_layout = QVBoxLayout()
    for layout in layouts:
        vertical_layout.addLayout(layout)

    return vertical_layout

def get_horizontal_layout_with_widgets_and_alignment(widgets, alignment=None):
    layout = QHBoxLayout()
    for widget in widgets:
        layout.addWidget(widget)
    if alignment is not None:
        layout.setAlignment(alignment)

    return layout
