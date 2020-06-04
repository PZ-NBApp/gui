from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_addPlayer(object):
    def click(self):
        firstName=self.firstNameInput.text()
        surname=self.surnameInput.text()
        club=self.clubInput.text()
        if(club==''):
            response=requests.post("http://localhost:8080/players/add", json={
            "firstName": firstName,
            "surname": surname
            })
        if response.status_code == 200:
            print("OK")
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
        self.applyButton.clicked.connect(self.click)
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addPlayer = QtWidgets.QWidget()
    ui = Ui_addPlayer()
    ui.setupUi(addPlayer)
    addPlayer.show()
    sys.exit(app.exec_())
