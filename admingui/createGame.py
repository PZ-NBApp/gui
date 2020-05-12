# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createGame.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createGame(object):
    def setupUi(self, createGame):
        createGame.setObjectName("createGame")
        createGame.resize(640, 107)
        self.verticalLayout = QtWidgets.QVBoxLayout(createGame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.hostLabel = QtWidgets.QLabel(createGame)
        self.hostLabel.setObjectName("hostLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.hostLabel)
        self.guestLabel = QtWidgets.QLabel(createGame)
        self.guestLabel.setObjectName("guestLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.guestLabel)
        self.hostChoose = QtWidgets.QComboBox(createGame)
        self.hostChoose.setObjectName("hostChoose")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hostChoose)
        self.guestChoose = QtWidgets.QComboBox(createGame)
        self.guestChoose.setObjectName("guestChoose")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.guestChoose)
        self.applyButton = QtWidgets.QPushButton(createGame)
        self.applyButton.setObjectName("applyButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.applyButton)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(createGame)
        QtCore.QMetaObject.connectSlotsByName(createGame)

    def retranslateUi(self, createGame):
        _translate = QtCore.QCoreApplication.translate
        createGame.setWindowTitle(_translate("createGame", "Create Game"))
        self.hostLabel.setText(_translate("createGame", "Host"))
        self.guestLabel.setText(_translate("createGame", "Guest"))
        self.applyButton.setText(_translate("createGame", "Apply"))
