from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QWidget, QLineEdit

from util import get_horizontal_layout_with_widgets_and_alignment, get_main_layout

class ConfigWindowWithSecret(QMainWindow):
    def __init__(self, rest_caller):
        super().__init__()
        self.setWindowTitle("Missing config")
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save)
        self.header_label = QLabel("Enter your secret id")
        self.header_label2 = QLabel("Enter the API url")
        self.secret_id_text = QLineEdit()
        self.secret_id_text.setPlaceholderText("Secret id")
        self.api_text = QLineEdit()
        self.api_text.setPlaceholderText("API URL")
        self.rest_caller = rest_caller
        widget = QWidget()
        widget.setLayout(get_main_layout(
            get_horizontal_layout_with_widgets_and_alignment([self.header_label]),
            get_horizontal_layout_with_widgets_and_alignment([self.secret_id_text]),
            get_horizontal_layout_with_widgets_and_alignment([self.header_label2]),
            get_horizontal_layout_with_widgets_and_alignment([self.api_text]),
            get_horizontal_layout_with_widgets_and_alignment([self.save_button])
        ))
        self.setCentralWidget(widget)

    def save(self):
        save(rest_api=self.api_text.text(), rest_caller=self.rest_caller, secret_id=self.secret_id_text.text())
        self.close()


class ConfigWindowNoSecret(QMainWindow):
    def __init__(self, rest_caller):
        super().__init__()
        self.setWindowTitle("Missing config")
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save)
        self.header_label1 = QLabel("Enter your email address and a username to register")
        self.header_label2 = QLabel("Enter the API url")
        self.username_text = QLineEdit()
        self.username_text.setPlaceholderText("Username")
        self.email_text = QLineEdit()
        self.email_text.setPlaceholderText("Email")
        self.api_text = QLineEdit()
        self.api_text.setPlaceholderText("API URL")
        self.rest_caller = rest_caller
        widget = QWidget()
        widget.setLayout(get_main_layout(
            get_horizontal_layout_with_widgets_and_alignment([self.header_label1]),
            get_horizontal_layout_with_widgets_and_alignment([self.email_text]),
            get_horizontal_layout_with_widgets_and_alignment([self.username_text]),
            get_horizontal_layout_with_widgets_and_alignment([self.header_label2]),
            get_horizontal_layout_with_widgets_and_alignment([self.api_text]),
            get_horizontal_layout_with_widgets_and_alignment([self.save_button])
        ))
        self.setCentralWidget(widget)

    def save(self):
        save(rest_api=self.api_text.text(), rest_caller=self.rest_caller,
             username=self.username_text.text(), email=self.email_text.text()
             )
        self.close()

def save(rest_api, rest_caller, secret_id=None, username=None, email=None):
    rest_caller.set_api_url(rest_api)
    if secret_id:
        if rest_caller.get_score_board():
            write_output_file(rest_api, secret_id)
        else:
            write_error_to_output_file()
    else:
        response_code, response_json = rest_caller.register(username, email)
        if response_code == 201:
            write_output_file(rest_api, response_json.get('secretId'))

def write_output_file(api_url, secret_id):
    with open('.player_config', 'w') as config:
        config.write(f"{api_url},{secret_id}")

def write_error_to_output_file():
    with open('.player_config', 'w') as config:
        config.write("Error, Error")
