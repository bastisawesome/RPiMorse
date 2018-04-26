import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication

import rpiMorse
from rpiMorse import PINS
from mainwindow import MainWindow

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
    
    # Configure the application
    QCoreApplication.setApplicationName("RPiMorse")
    
    # Create the application
    app = QApplication(sys.argv)
    # Creating the main window
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        rpiMorse.cleanup()