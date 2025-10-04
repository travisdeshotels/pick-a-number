import sys

from PyQt6.QtWidgets import QApplication
from window.mainwindow import MainWindow
from window.configprompt import ConfigWindow
import window.util.configutil as configutil
from window.rest.rest import RestCaller

app = QApplication(sys.argv)
if configutil.is_player_config_present():
    window = MainWindow(RestCaller(configutil.get_config_from_file()))
else:
    window = ConfigWindow(RestCaller((None, None)))
window.show()
app.exec()
