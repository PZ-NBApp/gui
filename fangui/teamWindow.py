# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teamWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_teamWindow(object):
    def setupUi(self, teamWindow):
        teamWindow.setObjectName("teamWindow")
        teamWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(teamWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameOutput = QtWidgets.QLabel(self.centralwidget)
        self.nameOutput.setText("")
        self.nameOutput.setObjectName("nameOutput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameOutput)
        self.cityLabel = QtWidgets.QLabel(self.centralwidget)
        self.cityLabel.setObjectName("cityLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.cityLabel)
        self.cityOutput = QtWidgets.QLabel(self.centralwidget)
        self.cityOutput.setText("")
        self.cityOutput.setObjectName("cityOutput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cityOutput)
        self.gamesPlayedLabel = QtWidgets.QLabel(self.centralwidget)
        self.gamesPlayedLabel.setObjectName("gamesPlayedLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.gamesPlayedLabel)
        self.gamesPlayedOutput = QtWidgets.QLabel(self.centralwidget)
        self.gamesPlayedOutput.setText("")
        self.gamesPlayedOutput.setObjectName("gamesPlayedOutput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gamesPlayedOutput)
        self.gamesWonLabel = QtWidgets.QLabel(self.centralwidget)
        self.gamesWonLabel.setObjectName("gamesWonLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.gamesWonLabel)
        self.gamesWonOutput = QtWidgets.QLabel(self.centralwidget)
        self.gamesWonOutput.setText("")
        self.gamesWonOutput.setObjectName("gamesWonOutput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.gamesWonOutput)
        self.gamesLostLabel = QtWidgets.QLabel(self.centralwidget)
        self.gamesLostLabel.setObjectName("gamesLostLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.gamesLostLabel)
        self.gamesLostOutput = QtWidgets.QLabel(self.centralwidget)
        self.gamesLostOutput.setText("")
        self.gamesLostOutput.setObjectName("gamesLostOutput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.gamesLostOutput)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.playersListLabel = QtWidgets.QLabel(self.centralwidget)
        self.playersListLabel.setObjectName("playersListLabel")
        self.verticalLayout_3.addWidget(self.playersListLabel)
        self.playersList = QtWidgets.QListView(self.centralwidget)
        self.playersList.setObjectName("playersList")
        self.verticalLayout_3.addWidget(self.playersList)
        self.playerChoose = QtWidgets.QComboBox(self.centralwidget)
        self.playerChoose.setObjectName("playerChoose")
        self.verticalLayout_3.addWidget(self.playerChoose)
        self.showPlayerButton = QtWidgets.QPushButton(self.centralwidget)
        self.showPlayerButton.setObjectName("showPlayerButton")
        self.verticalLayout_3.addWidget(self.showPlayerButton)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        teamWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(teamWindow)
        QtCore.QMetaObject.connectSlotsByName(teamWindow)

    def retranslateUi(self, teamWindow):
        _translate = QtCore.QCoreApplication.translate
        teamWindow.setWindowTitle(_translate("teamWindow", "Team"))
        self.nameLabel.setText(_translate("teamWindow", "Name"))
        self.cityLabel.setText(_translate("teamWindow", "City"))
        self.gamesPlayedLabel.setText(_translate("teamWindow", "Games played"))
        self.gamesWonLabel.setText(_translate("teamWindow", "Games won"))
        self.gamesLostLabel.setText(_translate("teamWindow", "Games lost"))
        self.playersListLabel.setText(_translate("teamWindow", "Players list"))
        self.showPlayerButton.setText(_translate("teamWindow", "Show Player"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    teamWindow = QtWidgets.QMainWindow()
    ui = Ui_teamWindow()
    ui.setupUi(teamWindow)
    teamWindow.show()
    sys.exit(app.exec_())