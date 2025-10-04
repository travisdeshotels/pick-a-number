import sys

from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QWidget, QLineEdit

from util.layoututil import get_main_layout_for_config_window
from util.layoututil import get_horizontal_layout_with_widgets_and_alignment

class ConfigWindow(QMainWindow):
    def __init__(self, rest_caller):
        super().__init__()
        self.setWindowTitle("Missing config")
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save)
        self.header_label = QLabel("Enter your secret id if you are already registered")
        self.header_label2 = QLabel("Enter a username and your email address to register")
        self.header_label3 = QLabel("Enter the API url")
        self.secret_id_text = QLineEdit()
        self.secret_id_text.setPlaceholderText("Secret id")
        self.username_text = QLineEdit()
        self.username_text.setPlaceholderText("Username")
        self.email_text = QLineEdit()
        self.email_text.setPlaceholderText("Email")
        self.api_text = QLineEdit()
        self.api_text.setPlaceholderText("API URL")
        self.rest_caller = rest_caller
        widget = QWidget()
        widget.setLayout(get_main_layout_for_config_window(
            get_horizontal_layout_with_widgets_and_alignment([self.header_label]),
            get_horizontal_layout_with_widgets_and_alignment([self.secret_id_text]),
            get_horizontal_layout_with_widgets_and_alignment([self.header_label2]),
            get_horizontal_layout_with_widgets_and_alignment([self.email_text]),
            get_horizontal_layout_with_widgets_and_alignment([self.username_text]),
            get_horizontal_layout_with_widgets_and_alignment([self.header_label3]),
            get_horizontal_layout_with_widgets_and_alignment([self.api_text]),
            get_horizontal_layout_with_widgets_and_alignment([self.save_button])
        ))
        self.setCentralWidget(widget)

    def save(self):
        if self.secret_id_text.text() and self.api_text.text():
            write_output_file(self.api_text.text(), self.secret_id_text.text())
        else:
            self.rest_caller.set_api_url(self.api_text.text())
            response_code, response_json = self.rest_caller.register(self.username_text.text(), self.email_text.text())
            if response_code == 201:
                write_output_file(self.rest_caller.get_api_url(), response_json.get('secretId'))
        sys.exit()


def write_output_file(api_url, secret_id):
    with open('.player_config', 'w') as config:
        config.write(f"{api_url},{secret_id}")
