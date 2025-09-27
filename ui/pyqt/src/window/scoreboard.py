from PyQt6.QtWidgets import QTextEdit, QVBoxLayout, QLabel, QDialog, QDialogButtonBox

from util.layoututil import get_horizontal_layout_with_widgets_and_alignment

class ScoreBoard(QDialog):
    def __init__(self, rest_caller):
        super().__init__()
        self.setWindowTitle("Scoreboard")
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.accepted.connect(self.accept)
        label = QLabel("High scores")
        text = QTextEdit()
        score_board_txt = ""
        scores = rest_caller.get_score_board()
        for score in scores:
            score_board_txt = score_board_txt + f'{score["player"]}: {score["score"]}\n'
        text.setText(score_board_txt)
        text.setReadOnly(True)
        layout = QVBoxLayout()
        layout.addLayout(get_horizontal_layout_with_widgets_and_alignment([label]))
        layout.addLayout(get_horizontal_layout_with_widgets_and_alignment([text]))
        layout.addLayout(get_horizontal_layout_with_widgets_and_alignment([self.buttonBox]))
        self.setLayout(layout)
