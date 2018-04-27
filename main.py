import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from mainwindow import MainWindow

import argparse

def main():
    # Parse application arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, help='IP for the server')
    parser.add_argument('--port', type=int, help='Port for the server')
    parser.add_argument('--disable-server', action='store_true',
                        help='Disable the internal server')
    args = parser.parse_args()
    
    # Configure the application
    QCoreApplication.setApplicationName("RPiMorse")
    
    # Create the application
    app = QApplication(sys.argv)
    # Creating the main window
    window = MainWindow(ip=args.ip, port=args.port, server=(not args.disable_server))
    window.show()
    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        rpiMorse.cleanup()