from PyQt5 import QtCore, QtGui, QtWidgets
import requests
#8081
gameId=[]
hostId=0
guestId=0
hostResult=0
guestResult=0

class Ui_referee(object):
    def getGames(self):
        global gameId
        global hostResult
        global guestResult
        global guestId
        global hostId
        self.gamesList.clear()
        self.gamesList.addItem('')
        response=requests.get("http://localhost:8081/game")
        if response.status_code==200:
            json=response.json()
            print(json)
            for i in json:
                host=i['host']
                guest=i['guest']
                text = host['city'] + ' ' + host['name'] + ' vs ' + guest['city'] + ' ' + guest['name']
                self.gamesList.addItem(text)

    def chooseGame(self):
        global gameId
        gameId=self.gamesList.currentIndex()
        response=requests.get("http://localhost:8081/game/{}".format(gameId))
        print(response.status_code)
        if response.status_code==200:
            json=response.json()
            print(json)
            host = json['host']
            guest = json['guest']
            hostName=host['city'] + ' ' + host['name']
            guestName=guest['city'] + ' ' + guest['name']
            self.hostLabel.setText(hostName)
            self.guestLabel.setText(guestName)

    def saveResult(self):
        global gameId
        global hostResult
        global guestResult
        hostResult=self.hostResultInput.toPlainText()
        guestResult=self.guestResultInput.toPlainText()
        response=requests.patch("http://localhost:8081/game/{}".format(gameId), json={
            "hostResult": hostResult,
	        "guestResult": guestResult
        })
        print(response.status_code)

    def setupUi(self, referee):
        referee.setObjectName("referee")
        referee.resize(640, 240)
        self.centralwidget = QtWidgets.QWidget(referee)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.getGamesButton = QtWidgets.QPushButton(self.centralwidget)
        self.getGamesButton.setObjectName("getGamesButton")
        self.getGamesButton.clicked.connect(self.getGames)
        self.verticalLayout.addWidget(self.getGamesButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gamesList = QtWidgets.QComboBox(self.centralwidget)
        self.gamesList.setObjectName("gamesList")
        self.verticalLayout.addWidget(self.gamesList)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.chooseGameButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseGameButton.setObjectName("chooseGameButton")
        self.chooseGameButton.clicked.connect(self.chooseGame)
        self.verticalLayout.addWidget(self.chooseGameButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hostLabel = QtWidgets.QLabel(self.centralwidget)
        self.hostLabel.setObjectName("hostLabel")
        self.horizontalLayout.addWidget(self.hostLabel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.hostResultInput = QtWidgets.QTextEdit(self.centralwidget)
        self.hostResultInput.setObjectName("hostResultInput")
        self.horizontalLayout.addWidget(self.hostResultInput)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.guestResultInput = QtWidgets.QTextEdit(self.centralwidget)
        self.guestResultInput.setObjectName("guestResultInput")
        self.horizontalLayout.addWidget(self.guestResultInput)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.guestLabel = QtWidgets.QLabel(self.centralwidget)
        self.guestLabel.setObjectName("guestLabel")
        self.horizontalLayout.addWidget(self.guestLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.saveResult)
        self.verticalLayout.addWidget(self.applyButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        referee.setCentralWidget(self.centralwidget)

        self.retranslateUi(referee)
        QtCore.QMetaObject.connectSlotsByName(referee)

    def retranslateUi(self, referee):
        _translate = QtCore.QCoreApplication.translate
        referee.setWindowTitle(_translate("referee", "Referee"))
        self.getGamesButton.setText(_translate("referee", "Get games list"))
        self.chooseGameButton.setText(_translate("referee", "Choose game"))
        self.hostLabel.setText(_translate("referee", "Host"))
        self.guestLabel.setText(_translate("referee", "Guest"))
        self.applyButton.setText(_translate("referee", "Apply result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    referee = QtWidgets.QMainWindow()
    ui = Ui_referee()
    ui.setupUi(referee)
    referee.show()
    sys.exit(app.exec_())
