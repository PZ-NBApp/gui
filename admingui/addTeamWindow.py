#DZIALA
from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_addTeamWindow(object):
    def click(self):
        name=self.nameInput.text()
        city=self.cityInput.text()
        response=requests.post("http://localhost:8080/team/add", json={
            "name": name,
            "city": city
        })
        if response.status_code == 200:
            print("OK")
    def setupUi(self, addTeamWindow):
        addTeamWindow.setObjectName("addTeamWindow")
        addTeamWindow.resize(640, 107)
        self.centralwidget = QtWidgets.QWidget(addTeamWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 631, 89))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.cityLabel = QtWidgets.QLabel(self.layoutWidget)
        self.cityLabel.setObjectName("cityLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.cityLabel)
        self.applyButton = QtWidgets.QPushButton(self.layoutWidget)
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.click)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.applyButton)
        self.nameInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.nameInput.setObjectName("nameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameInput)
        self.cityInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.cityInput.setObjectName("cityInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cityInput)
        addTeamWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(addTeamWindow)
        QtCore.QMetaObject.connectSlotsByName(addTeamWindow)

    def retranslateUi(self, addTeamWindow):
        _translate = QtCore.QCoreApplication.translate
        addTeamWindow.setWindowTitle(_translate("addTeamWindow", "Add Team"))
        self.nameLabel.setText(_translate("addTeamWindow", "Name"))
        self.cityLabel.setText(_translate("addTeamWindow", "City"))
        self.applyButton.setText(_translate("addTeamWindow", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addTeamWindow = QtWidgets.QMainWindow()
    ui = Ui_addTeamWindow()
    ui.setupUi(addTeamWindow)
    addTeamWindow.show()
    sys.exit(app.exec_())
