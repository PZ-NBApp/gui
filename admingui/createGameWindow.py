from PyQt5 import QtCore, QtGui, QtWidgets
import requests

ls=[]
class Ui_createGameWindow(object):
    def click(self):

        hostId = str(self.hostChoose.currentIndex())
        guestId = str(self.guestChoose.currentIndex())
        response = requests.post("http://localhost:8080/game/add", json={
            "host": hostId,
            "guest": guestId
        })

        if response.status_code == 200:
            print("OK")

    def setupUi(self, createGameWindow):
        createGameWindow.setObjectName("createGameWindow")
        createGameWindow.resize(642, 110)
        self.centralwidget = QtWidgets.QWidget(createGameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(3, 8, 631, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.hostLabel = QtWidgets.QLabel(self.layoutWidget)
        self.hostLabel.setObjectName("hostLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.hostLabel)
        self.hostChoose = QtWidgets.QComboBox(self.layoutWidget)
        self.hostChoose.setObjectName("hostChoose")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hostChoose)
        self.guestChoose = QtWidgets.QComboBox(self.layoutWidget)
        self.guestChoose.setObjectName("guestChoose")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.guestChoose)
        self.applyButton = QtWidgets.QPushButton(self.layoutWidget)
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.click)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.applyButton)
        self.guestLabel = QtWidgets.QLabel(self.layoutWidget)
        self.guestLabel.setObjectName("guestLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.guestLabel)
        createGameWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(createGameWindow)
        QtCore.QMetaObject.connectSlotsByName(createGameWindow)

        self.hostChoose.clear()
        self.hostChoose.addItem('')
        self.guestChoose.clear()
        self.guestChoose.addItem('')
        response = requests.get("http://localhost:8080/team")
        if response.status_code == 200:
            json = response.json()
            print(json)
            for i in json:
                text = i['city'] +' '+ i['name']
                ls.append(text)
        ls.reverse()
        self.hostChoose.addItems(ls)
        self.guestChoose.addItems(ls)

    def retranslateUi(self, createGameWindow):
        _translate = QtCore.QCoreApplication.translate
        createGameWindow.setWindowTitle(_translate("createGameWindow", "Create Game"))
        self.hostLabel.setText(_translate("createGameWindow", "Host"))
        self.applyButton.setText(_translate("createGameWindow", "Apply"))
        self.guestLabel.setText(_translate("createGameWindow", "Guest"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createGameWindow = QtWidgets.QMainWindow()
    ui = Ui_createGameWindow()
    ui.setupUi(createGameWindow)
    createGameWindow.show()
    sys.exit(app.exec_())
