from rpiMorse import pinList
import rpiMorse

from PyQt5.QtWidgets import QMainWindow, QMessageBox, qApp
from PyQt5.QtCore import QSettings
from ui_mainwindow import Ui_MainWindow
from configdialog import ConfigDialog

import socket

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        rpiMorse.setup()
        
        self.configDialog = ConfigDialog(self)
        
        self.userInput.textChanged.connect(self.updateMorse)
        self.transmitButton.clicked.connect(self.transmitMorse)
        self.actionConfigure.triggered.connect(self.showConfigDialog)
        self.actionAbout_Qt.triggered.connect(qApp.aboutQt)
        
        # Load settings
        settings = QSettings()
        self.outputPin = int(settings.value("activePin", "18"))
        
    def updateMorse(self):
        code = rpiMorse.parseLine(self.userInput.toPlainText())
        
        self.morseOutput.setText(code.replace("WORD", "").replace("STOP", ""))
    
    def transmitMorse(self):
        code = rpiMorse.parseLine(self.userInput.toPlainText())
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            settings = QSettings()
            sock.connect((settings.value("serverIp"), int(settings.value("serverPort"))))
        except Exception as e:
            QMessageBox.critical(self, "Error!", str(e))
            return
        
        sock.send(b'MORSE:' + bytes(code.encode("utf-8")))
    
    def closeEvent(self, event):
        # Cleanup the GPIO first
        rpiMorse.cleanup()
        
        # Finally, destroy the window
        event.accept()
    
    def showConfigDialog(self):
        self.configDialog.exec_()
        
        # Update settings for the main window
        settings = QSettings()
        self.outputPin = int(settings.value("activePin", "18"))