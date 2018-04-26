import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication

import rpiMorse
from rpiMorse import PINS
from mainwindow import MainWindow
from server import Server

def main():
    # rpiMorse.setup()
    #
    # userInput = ""
    # while True:
    #     userInput = input("Line (q to quit): ")
    #
    #     if userInput.lower() == "q" or userInput.lower() == "quit": break
    #
    #     code = rpiMorse.parseLine(userInput)
    #     rpiMorse.outputCode(code, PINS.GPIO18)
    #
    # rpiMorse.cleanup()
    
    # Manage the server
    server = Server()
    server.start()
    
    QCoreApplication.setApplicationName("RPiMorse")
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec_()
    
    server.stop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        rpiMorse.cleanup()