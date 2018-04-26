import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication

from mainwindow import MainWindow

def main():
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