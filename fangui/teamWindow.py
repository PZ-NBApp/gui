from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_teamWindow(object):
    def team(self):
        teamId=self.teamsList.currentIndex()
        response=requests.get("http://localhost:8082/team/{}".format(teamId))
        print(response.status_code)
        if response.status_code==200:
            json=response.json()
            print(json)
            self.nameOutput.setText(json['name'])
            self.cityOutput.setText(json['city'])
            self.gamesPlayedOutput.setText(str(json['gamesPlayed']))
            self.gamesWonOutput.setText(str(json['gamesWon']))
            self.gamesLostOutput.setText(str(json['gamesLost']))
            response2=requests.get("http://localhost:8082/assignation/team/{}".format(teamId))
            print(response2.status_code)
            if response2.status_code==200:
                json2=response2.json()
                print(json2)
                for i in json2:
                    player=i['firstName']+' '+i['surname']
                    self.playerList.addItem(player)


    def player(self):
        '''
            self.teamsList.clear()
            response = requests.get("http://localhost:8082/team")
            if response.status_code == 200:
                json = response.json()
                print(json)
                for i in json:

                    for i in json:
                     idG.append(i['id'])
                     ex_type.append(i['examinationType'])
                     examination_type = ExamTypes[i['examinationType']].value
                     self.exams.addItem(examination_type)
                 print(idG)

        '''
        print()

    def setupUi(self, teamWindow):
        teamWindow.setObjectName("teamWindow")
        teamWindow.resize(640, 640)
        self.centralwidget = QtWidgets.QWidget(teamWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.teamsList = QtWidgets.QComboBox(self.centralwidget)
        self.teamsList.setObjectName("teamsList")
        self.verticalLayout.addWidget(self.teamsList)
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.team)
        self.verticalLayout.addWidget(self.applyButton)
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
        self.playerChoose = QtWidgets.QComboBox(self.centralwidget)
        self.playerChoose.setObjectName("playerChoose")
        self.verticalLayout_3.addWidget(self.playerChoose)
        self.showPlayerButton = QtWidgets.QPushButton(self.centralwidget)
        self.showPlayerButton.setObjectName("showPlayerButton")
        self.verticalLayout_3.addWidget(self.showPlayerButton)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.playersListLabel = QtWidgets.QLabel(self.centralwidget)
        self.playersListLabel.setObjectName("playersListLabel")
        self.verticalLayout.addWidget(self.playersListLabel)
        self.playerList = QtWidgets.QListWidget(self.centralwidget)
        self.playerList.setObjectName("playerList")
        self.verticalLayout.addWidget(self.playerList)
        self.playerLabel = QtWidgets.QLabel(self.centralwidget)
        self.playerLabel.setObjectName("playerLabel")
        self.verticalLayout.addWidget(self.playerLabel)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.firstNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameOutput = QtWidgets.QLabel(self.centralwidget)
        self.firstNameOutput.setText("")
        self.firstNameOutput.setObjectName("firstNameOutput")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameOutput)
        self.surnameLabel = QtWidgets.QLabel(self.centralwidget)
        self.surnameLabel.setObjectName("surnameLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.surnameLabel)
        self.surnameOutput = QtWidgets.QLabel(self.centralwidget)
        self.surnameOutput.setText("")
        self.surnameOutput.setObjectName("surnameOutput")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surnameOutput)
        self.verticalLayout.addLayout(self.formLayout_2)
        teamWindow.setCentralWidget(self.centralwidget)

        self.teamsList.clear()
        self.teamsList.addItem('')
        response = requests.get("http://localhost:8082/team")
        print(response.status_code)
        if response.status_code == 200:
            json = response.json()
            print(json)
            for i in json:
                text = i['city'] + ' ' + i['name']
                self.teamsList.addItem(text)

        self.retranslateUi(teamWindow)
        QtCore.QMetaObject.connectSlotsByName(teamWindow)

    def retranslateUi(self, teamWindow):
        _translate = QtCore.QCoreApplication.translate
        teamWindow.setWindowTitle(_translate("teamWindow", "Team"))
        self.applyButton.setText(_translate("teamWindow", "Show Team"))
        self.nameLabel.setText(_translate("teamWindow", "Name"))
        self.cityLabel.setText(_translate("teamWindow", "City"))
        self.gamesPlayedLabel.setText(_translate("teamWindow", "Games played"))
        self.gamesWonLabel.setText(_translate("teamWindow", "Games won"))
        self.gamesLostLabel.setText(_translate("teamWindow", "Games lost"))
        self.playersListLabel.setText(_translate("teamWindow", "Players list"))
        self.showPlayerButton.setText(_translate("teamWindow", "Show Player"))
        self.playerLabel.setText(_translate("teamWindow", "Player"))
        self.firstNameLabel.setText(_translate("teamWindow", "First Name"))
        self.surnameLabel.setText(_translate("teamWindow", "Surname"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    teamWindow = QtWidgets.QMainWindow()
    ui = Ui_teamWindow()
    ui.setupUi(teamWindow)
    teamWindow.show()
    sys.exit(app.exec_())
