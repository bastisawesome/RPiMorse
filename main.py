import sys
from PyQt5.QtWidgets import QApplication

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

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        rpiMorse.cleanup()