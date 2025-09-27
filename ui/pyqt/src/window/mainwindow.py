from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QComboBox, QWidget, QTextEdit
from rest.rest import RestCaller
from scoreboard import ScoreBoard
from util.configutil import get_config_from_file
from util.layoututil import get_main_layout, get_horizontal_layout_with_widgets_and_alignment


class MainWindow(QMainWindow):
    rest_caller = None
    guess = 1
    result_textbox = None
    stat_textbox = None
    label_stats = None
    label_header = None
    label_result = None
    submit_button = None
    scoreboard_button = None
    scoreboard = None


    def get_combo_box(self):
        box = QComboBox()
        selections = list(range(1, 11))
        box.addItems([str(n) for n in selections])
        box.currentIndexChanged.connect(self.index_changed)

        return box

    def create_labels(self):
        self.label_header = QLabel("Pick a number")
        self.label_result = QLabel("Result")
        self.label_stats = QLabel("Stats")

    def create_textboxes(self):
        self.result_textbox = QTextEdit()
        self.result_textbox.setReadOnly(True)
        self.stat_textbox = QTextEdit()
        self.stat_textbox.setReadOnly(True)

    def create_buttons(self):
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_guess)
        self.scoreboard_button = QPushButton("View scoreboard")
        self.scoreboard_button.clicked.connect(self.show_scoreboard)


    def __init__(self):
        super().__init__()
        self.rest_caller = RestCaller(get_config_from_file())
        self.setWindowTitle("Pick a number")
        self.create_buttons()
        self.create_labels()
        self.create_textboxes()
        self.setFixedSize(QSize(800, 600))
        widget = QWidget()
        widget.setLayout(get_main_layout(
            get_horizontal_layout_with_widgets_and_alignment([self.label_header]),
            get_horizontal_layout_with_widgets_and_alignment([self.get_combo_box(), self.submit_button]),
            get_horizontal_layout_with_widgets_and_alignment([self.label_result]),
            get_horizontal_layout_with_widgets_and_alignment([self.result_textbox], Qt.AlignmentFlag.AlignHCenter),
            get_horizontal_layout_with_widgets_and_alignment([self.label_stats]),
            get_horizontal_layout_with_widgets_and_alignment([self.stat_textbox], Qt.AlignmentFlag.AlignHCenter),
            get_horizontal_layout_with_widgets_and_alignment([self.scoreboard_button])
        ))
        self.setCentralWidget(widget)

    def show_scoreboard(self):
        self.scoreboard = ScoreBoard(self.rest_caller)
        self.scoreboard.show()

    def index_changed(self, i):
        self.guess = i + 1

    def submit_guess(self):
        response_dict = self.rest_caller.submit_guess(self.guess)
        self.display_result(response_dict['result'])
        self.display_stats(response_dict['username'], response_dict['stats'])

    def display_result(self, result):
        self.result_textbox.setPlainText('YOU WIN!' if result['result'] == 'win' else 'YOU LOSE.\n'
                                         f'Your guess: {result["guess"]}\n'
                                         f'Correct number: {result["correctNumber"]}'
                                         )

    def display_stats(self, username, stats):
        self.label_stats.setText(f'Stats for {username}')
        self.stat_textbox.setPlainText(f'Wins: {stats["wins"]}\n'
                                       f'Total played: {stats["total"]}\n'
                                       f'Most guessed: {stats["mostGuessed"]}'
        )