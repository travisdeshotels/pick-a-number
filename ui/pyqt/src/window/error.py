from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class ErrorDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Error")

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.accepted.connect(self.accept)

        layout = QVBoxLayout()
        message = QLabel("Cannot connect to the API. Validate the URL and try again.")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
