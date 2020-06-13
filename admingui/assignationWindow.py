import requests
from PyQt5 import QtCore, QtGui, QtWidgets

teamList=[]
playerList=[]

class Ui_assignationWindow(object):
    def click(self):
        teamId=str(self.teamComboBox.currentIndex())
        playerId=str(self.playerComboBox.currentIndex())
        send=requests.post("http://localhost:8080/assignation/add", json={
            "player": playerId,
            "team": teamId
        })
        print(send.status_code)
    def setupUi(self, assignationWindow):
        assignationWindow.setObjectName("assignationWindow")
        assignationWindow.resize(640, 114)
        self.centralwidget = QtWidgets.QWidget(assignationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.playerLabel = QtWidgets.QLabel(self.centralwidget)
        self.playerLabel.setObjectName("playerLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.playerLabel)
        self.teamLabel = QtWidgets.QLabel(self.centralwidget)
        self.teamLabel.setObjectName("teamLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.teamLabel)
        self.playerComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.playerComboBox.setObjectName("playerComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.playerComboBox)
        self.teamComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.teamComboBox.setObjectName("teamComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.teamComboBox)
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.click)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.applyButton)
        self.verticalLayout.addLayout(self.formLayout)
        assignationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(assignationWindow)
        QtCore.QMetaObject.connectSlotsByName(assignationWindow)

        self.teamComboBox.clear()
        self.teamComboBox.addItem('')
        response = requests.get("http://localhost:8080/team")
        if response.status_code == 200:
            json = response.json()
            print(json)
            for i in json:
                text = i['city'] + ' ' + i['name']
                teamList.append(text)
        teamList.reverse()
        self.teamComboBox.addItems(teamList)

        self.playerComboBox.clear()
        self.playerComboBox.addItem('')
        response = requests.get("http://localhost:8080/players")
        if response.status_code == 200:
            json = response.json()
            print(json)
            for i in json:
                text = i['firstName'] + ' ' + i['surname']
                playerList.append(text)
        playerList.reverse()
        self.playerComboBox.addItem(text)

    def retranslateUi(self, assignationWindow):
        _translate = QtCore.QCoreApplication.translate
        assignationWindow.setWindowTitle(_translate("assignationWindow", "Assign"))
        self.playerLabel.setText(_translate("assignationWindow", "Player"))
        self.teamLabel.setText(_translate("assignationWindow", "Team"))
        self.applyButton.setText(_translate("assignationWindow", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    assignationWindow = QtWidgets.QMainWindow()
    ui = Ui_assignationWindow()
    ui.setupUi(assignationWindow)
    assignationWindow.show()
    sys.exit(app.exec_())
