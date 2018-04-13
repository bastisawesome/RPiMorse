from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QSettings
from ui_configdialog import Ui_ConfigDialog

import rpiMorse

class ConfigDialog(QDialog, Ui_ConfigDialog):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__(parent)
        self.setupUi(self)
        
        # Load settings
        settings = QSettings()
        
        if not rpiMorse.rpio:
            self.pinSelector.setEnabled(False)
        else:
            self.pinSelector.addItems([str(i) for i in rpiMorse.pinList])
            self.pinSelector.setCurrentIndex(self.pinSelector.findText(settings.value("activePin", "18")))
            
        self.ipAddressLine.setText(settings.value("serverIp"))
        self.portLine.setText(settings.value("serverPort"))
        
        self.finished.connect(self.updateSettings)
        self.pingButton.clicked.connect(self.pingServer)
    
    def updateSettings(self, value:int):
        if value:
            # Update settings
            settings = QSettings()
            if rpiMorse.rpio:
                settings.setValue("activePin", int(self.pinSelector.currentText()))
            settings.setValue("serverIp", self.ipAddressLine.text())
            settings.setValue("serverPort", self.portLine.text())
    
    def pingServer(self):
        pass