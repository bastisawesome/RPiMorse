from PyQt5.QtWidgets import QDialog
from ui_configwidget import Ui_ConfigWidget

class ConfigDialog(QDialog, Ui_ConfigWidget):
    def __init__(self, parent=None):
        super(ConfigWidget, self).__init__(parent)
        self.setupUi(self)