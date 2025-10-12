import sys

from PyQt6.QtWidgets import QApplication

from window.prompt import CustomDialog
from window.mainwindow import MainWindow
from window.configprompt import ConfigWindowWithSecret, ConfigWindowNoSecret
import window.util.configutil as configutil
from window.rest.rest import RestCaller

app = QApplication(sys.argv)
if configutil.is_player_config_present():
    window = MainWindow(RestCaller(configutil.get_config_from_file()))
else:
    user_has_secret_key = CustomDialog()
    if user_has_secret_key.exec():
        window = ConfigWindowWithSecret(RestCaller((None, None)))
    else:
        window = ConfigWindowNoSecret(RestCaller((None, None)))
window.show()
app.exec()
