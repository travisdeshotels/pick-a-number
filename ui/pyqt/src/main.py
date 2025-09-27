import sys

from PyQt6.QtWidgets import QApplication
from window.mainwindow import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
