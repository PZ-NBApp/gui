# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showTeam.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_teamView(object):
    def setupUi(self, teamView):
        teamView.setObjectName("teamView")
        teamView.resize(640, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(teamView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(teamView)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameOutput = QtWidgets.QLabel(teamView)
        self.nameOutput.setText("")
        self.nameOutput.setObjectName("nameOutput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameOutput)
        self.cityLabel = QtWidgets.QLabel(teamView)
        self.cityLabel.setObjectName("cityLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.cityLabel)
        self.cityOutput = QtWidgets.QLabel(teamView)
        self.cityOutput.setText("")
        self.cityOutput.setObjectName("cityOutput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cityOutput)
        self.gamesPlayedLabel = QtWidgets.QLabel(teamView)
        self.gamesPlayedLabel.setObjectName("gamesPlayedLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.gamesPlayedLabel)
        self.gamesPlayedOutput = QtWidgets.QLabel(teamView)
        self.gamesPlayedOutput.setText("")
        self.gamesPlayedOutput.setObjectName("gamesPlayedOutput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gamesPlayedOutput)
        self.gamesWonLabel = QtWidgets.QLabel(teamView)
        self.gamesWonLabel.setObjectName("gamesWonLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.gamesWonLabel)
        self.gamesWonOutput = QtWidgets.QLabel(teamView)
        self.gamesWonOutput.setText("")
        self.gamesWonOutput.setObjectName("gamesWonOutput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.gamesWonOutput)
        self.gamesLostLabel = QtWidgets.QLabel(teamView)
        self.gamesLostLabel.setObjectName("gamesLostLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.gamesLostLabel)
        self.gamesLostOutput = QtWidgets.QLabel(teamView)
        self.gamesLostOutput.setText("")
        self.gamesLostOutput.setObjectName("gamesLostOutput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.gamesLostOutput)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.playersListLabel = QtWidgets.QLabel(teamView)
        self.playersListLabel.setObjectName("playersListLabel")
        self.verticalLayout_3.addWidget(self.playersListLabel)
        self.playersList = QtWidgets.QListView(teamView)
        self.playersList.setObjectName("playersList")
        self.verticalLayout_3.addWidget(self.playersList)
        self.playerChoose = QtWidgets.QComboBox(teamView)
        self.playerChoose.setObjectName("playerChoose")
        self.verticalLayout_3.addWidget(self.playerChoose)
        self.showPlayerButton = QtWidgets.QPushButton(teamView)
        self.showPlayerButton.setObjectName("showPlayerButton")
        self.verticalLayout_3.addWidget(self.showPlayerButton)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(teamView)
        QtCore.QMetaObject.connectSlotsByName(teamView)

    def retranslateUi(self, teamView):
        _translate = QtCore.QCoreApplication.translate
        teamView.setWindowTitle(_translate("teamView", "Team"))
        self.nameLabel.setText(_translate("teamView", "Name"))
        self.cityLabel.setText(_translate("teamView", "City"))
        self.gamesPlayedLabel.setText(_translate("teamView", "Games played"))
        self.gamesWonLabel.setText(_translate("teamView", "Games won"))
        self.gamesLostLabel.setText(_translate("teamView", "Games lost"))
        self.playersListLabel.setText(_translate("teamView", "Players list"))
        self.showPlayerButton.setText(_translate("teamView", "Show Player"))
