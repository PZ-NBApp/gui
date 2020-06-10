from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from PyQt5.QtWidgets import QMainWindow
from teamWindow import Ui_teamWindow

class Ui_teamsListWindow(object):
    def click(self):
        self.window = QMainWindow()
        self.ui = Ui_teamWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, teamsListWindow):
        teamsListWindow.setObjectName("teamsListWindow")
        teamsListWindow.resize(640, 74)
        self.centralwidget = QtWidgets.QWidget(teamsListWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.teamsList = QtWidgets.QComboBox(self.centralwidget)
        self.teamsList.setObjectName("teamsList")
        self.verticalLayout_2.addWidget(self.teamsList)
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.click)
        self.verticalLayout_2.addWidget(self.applyButton)
        teamsListWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(teamsListWindow)
        QtCore.QMetaObject.connectSlotsByName(teamsListWindow)
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
    def retranslateUi(self, teamsListWindow):
        _translate = QtCore.QCoreApplication.translate
        teamsListWindow.setWindowTitle(_translate("teamsListWindow", "Teams List"))
        self.applyButton.setText(_translate("teamsListWindow", "Show Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    teamsListWindow = QtWidgets.QMainWindow()
    ui = Ui_teamsListWindow()
    ui.setupUi(teamsListWindow)
    teamsListWindow.show()
    sys.exit(app.exec_())
