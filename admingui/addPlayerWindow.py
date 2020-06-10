from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_addPlayerWindow(object):
    def click(self):
        firstName=self.firstNameInput.text()
        surname=self.surnameInput.text()
        club=self.clubChooseBox.currentText()
        response=requests.post("http://localhost:8080/players/add", json={
            "firstName": firstName,
            "surname": surname
            })
        #TODO
        #how to assign player to club
        if response.status_code == 200:
            print("OK")
    def setupUi(self, addPlayerWindow):
        addPlayerWindow.setObjectName("addPlayerWindow")
        addPlayerWindow.resize(640, 132)
        self.centralwidget = QtWidgets.QWidget(addPlayerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(3, 9, 631, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.firstNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.firstNameInput.setObjectName("firstNameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameInput)
        self.surnameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.surnameLabel.setObjectName("surnameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.surnameLabel)
        self.surnameInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.surnameInput.setObjectName("surnameInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surnameInput)
        self.clubLabel = QtWidgets.QLabel(self.layoutWidget)
        self.clubLabel.setObjectName("clubLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.clubLabel)
        self.applyButton = QtWidgets.QPushButton(self.layoutWidget)
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.click)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.applyButton)
        self.clubChooseBox = QtWidgets.QComboBox(self.layoutWidget)
        self.clubChooseBox.setObjectName("clubChooseBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.clubChooseBox)
        addPlayerWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(addPlayerWindow)
        QtCore.QMetaObject.connectSlotsByName(addPlayerWindow)

        self.clubChooseBox.clear()
        response = requests.get("http://localhost:8080/team")
        if response.status_code == 200:
            json = response.json()
            print(json)
            for i in json:
                '''
                for i in json:
                 idG.append(i['id'])
                 ex_type.append(i['examinationType'])
                 examination_type = ExamTypes[i['examinationType']].value
                 self.exams.addItem(examination_type)
             print(idG)
                '''

    def retranslateUi(self, addPlayerWindow):
        _translate = QtCore.QCoreApplication.translate
        addPlayerWindow.setWindowTitle(_translate("addPlayerWindow", "Add Player"))
        self.firstNameLabel.setText(_translate("addPlayerWindow", "First Name"))
        self.surnameLabel.setText(_translate("addPlayerWindow", "Surname"))
        self.clubLabel.setText(_translate("addPlayerWindow", "Club"))
        self.applyButton.setText(_translate("addPlayerWindow", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addPlayerWindow = QtWidgets.QMainWindow()
    ui = Ui_addPlayerWindow()
    ui.setupUi(addPlayerWindow)
    addPlayerWindow.show()
    sys.exit(app.exec_())
