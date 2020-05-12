# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addPlayer(object):
    def setupUi(self, addPlayer):
        addPlayer.setObjectName("addPlayer")
        addPlayer.resize(640, 138)
        self.verticalLayout = QtWidgets.QVBoxLayout(addPlayer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.firstNameLabel = QtWidgets.QLabel(addPlayer)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameInput = QtWidgets.QLineEdit(addPlayer)
        self.firstNameInput.setObjectName("firstNameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameInput)
        self.surnameLabel = QtWidgets.QLabel(addPlayer)
        self.surnameLabel.setObjectName("surnameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.surnameLabel)
        self.surnameInput = QtWidgets.QLineEdit(addPlayer)
        self.surnameInput.setObjectName("surnameInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surnameInput)
        self.clubInput = QtWidgets.QLineEdit(addPlayer)
        self.clubInput.setObjectName("clubInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.clubInput)
        self.clubLabel = QtWidgets.QLabel(addPlayer)
        self.clubLabel.setObjectName("clubLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.clubLabel)
        self.applyButton = QtWidgets.QPushButton(addPlayer)
        self.applyButton.setObjectName("applyButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.applyButton)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(addPlayer)
        QtCore.QMetaObject.connectSlotsByName(addPlayer)

    def retranslateUi(self, addPlayer):
        _translate = QtCore.QCoreApplication.translate
        addPlayer.setWindowTitle(_translate("addPlayer", "Add Player"))
        self.firstNameLabel.setText(_translate("addPlayer", "First Name"))
        self.surnameLabel.setText(_translate("addPlayer", "Surname"))
        self.clubLabel.setText(_translate("addPlayer", "Club"))
        self.applyButton.setText(_translate("addPlayer", "Apply"))
