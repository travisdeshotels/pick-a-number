import sys

from PyQt6.QtWidgets import QApplication, QDialog

from window.prompt import CustomDialog
from window.mainwindow import MainWindow
from window.configprompt import ConfigWindowWithSecret, ConfigWindowNoSecret
from window.util import RestCaller, ConfigUtil
from window.error import ErrorDialog
import os

def delete_error_file():
    try:
        os.remove('.player_config')
    except OSError:
        pass


app = QApplication(sys.argv)
config_util = ConfigUtil()
if config_util.is_player_config_present():
    window = MainWindow(RestCaller(config_util.get_config_from_file()))
else:
    user_has_secret_key = CustomDialog()
    if user_has_secret_key.exec():
        window = ConfigWindowWithSecret(RestCaller((None, None)))
    else:
        window = ConfigWindowNoSecret(RestCaller((None, None)))
window.show()
app.exec()
conf_values = config_util.get_config_from_file()
if conf_values[0] == "Error":
    delete_error_file()
    dlg = ErrorDialog()
    dlg.exec()
