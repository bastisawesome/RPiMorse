# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigDialog(object):
    def setupUi(self, ConfigDialog):
        ConfigDialog.setObjectName("ConfigDialog")
        ConfigDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ConfigDialog.resize(400, 300)
        self.formLayout = QtWidgets.QFormLayout(ConfigDialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(ConfigDialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.line = QtWidgets.QFrame(ConfigDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.pinLabel = QtWidgets.QLabel(ConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pinLabel.sizePolicy().hasHeightForWidth())
        self.pinLabel.setSizePolicy(sizePolicy)
        self.pinLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pinLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pinLabel.setObjectName("pinLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pinLabel)
        self.pinSelector = QtWidgets.QComboBox(ConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pinSelector.sizePolicy().hasHeightForWidth())
        self.pinSelector.setSizePolicy(sizePolicy)
        self.pinSelector.setObjectName("pinSelector")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pinSelector)
        self.line_2 = QtWidgets.QFrame(ConfigDialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.label_2 = QtWidgets.QLabel(ConfigDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(ConfigDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(ConfigDialog)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_4 = QtWidgets.QLabel(ConfigDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(ConfigDialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(ConfigDialog)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.pushButton)

        self.retranslateUi(ConfigDialog)
        QtCore.QMetaObject.connectSlotsByName(ConfigDialog)

    def retranslateUi(self, ConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfigDialog.setWindowTitle(_translate("ConfigDialog", "Form"))
        self.label.setText(_translate("ConfigDialog", "Output"))
        self.pinLabel.setText(_translate("ConfigDialog", "Active Pin"))
        self.label_2.setText(_translate("ConfigDialog", "Server"))
        self.label_3.setText(_translate("ConfigDialog", "IP Address"))
        self.lineEdit.setPlaceholderText(_translate("ConfigDialog", "localhost"))
        self.label_4.setText(_translate("ConfigDialog", "Port"))
        self.lineEdit_2.setPlaceholderText(_translate("ConfigDialog", "5000"))
        self.pushButton.setText(_translate("ConfigDialog", "Ping"))

