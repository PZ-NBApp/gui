from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_tableWindow(object):
    def setupUi(self, tableWindow):
        tableWindow.setObjectName("tableWindow")
        tableWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(tableWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        tableWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(tableWindow)
        QtCore.QMetaObject.connectSlotsByName(tableWindow)
    '''
        self.guestChoose.clear()
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

    def retranslateUi(self, tableWindow):
        _translate = QtCore.QCoreApplication.translate
        tableWindow.setWindowTitle(_translate("tableWindow", "Table"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tableWindow = QtWidgets.QMainWindow()
    ui = Ui_tableWindow()
    ui.setupUi(tableWindow)
    tableWindow.show()
    sys.exit(app.exec_())
