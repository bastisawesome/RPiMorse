# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.morseOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.morseOutput.setEnabled(True)
        self.morseOutput.setAcceptDrops(False)
        self.morseOutput.setReadOnly(True)
        self.morseOutput.setObjectName("morseOutput")
        self.gridLayout.addWidget(self.morseOutput, 1, 1, 1, 1)
        self.userInput = QtWidgets.QTextEdit(self.centralwidget)
        self.userInput.setTabChangesFocus(True)
        self.userInput.setObjectName("userInput")
        self.gridLayout.addWidget(self.userInput, 1, 0, 1, 1)
        self.transmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.transmitButton.setObjectName("transmitButton")
        self.gridLayout.addWidget(self.transmitButton, 2, 0, 1, 2)
        self.textLabel = QtWidgets.QLabel(self.centralwidget)
        self.textLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textLabel.setStyleSheet("")
        self.textLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.textLabel.setObjectName("textLabel")
        self.gridLayout.addWidget(self.textLabel, 0, 0, 1, 1)
        self.morseLabel = QtWidgets.QLabel(self.centralwidget)
        self.morseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.morseLabel.setObjectName("morseLabel")
        self.gridLayout.addWidget(self.morseLabel, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionPins = QtWidgets.QAction(MainWindow)
        self.actionPins.setObjectName("actionPins")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionConfigure = QtWidgets.QAction(MainWindow)
        self.actionConfigure.setObjectName("actionConfigure")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.menuFile.addAction(self.actionConfigure)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.transmitButton.setText(_translate("MainWindow", "Transmit"))
        self.textLabel.setText(_translate("MainWindow", "Plain Text"))
        self.morseLabel.setText(_translate("MainWindow", "Morse Code"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.actionPins.setText(_translate("MainWindow", "&Pins"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionConfigure.setText(_translate("MainWindow", "&Configure"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "A&bout Qt"))

