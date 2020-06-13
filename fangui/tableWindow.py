from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
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
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(('City', 'Name', 'Games Played', 'Games Won', 'Games Lost', 'Win %'))
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        tableWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(tableWindow)
        QtCore.QMetaObject.connectSlotsByName(tableWindow)


        response = requests.get("http://localhost:8082/team/standings")
        if response.status_code == 200:
            json = response.json()
            print(json)
            for i in json:
                name = i['name']
                city = i['city']
                gamesPlayed = str(i['gamesPlayed'])
                gamesWon = str(i['gamesWon'])
                gamesLost = str(i['gamesLost'])
                winPer = str(i['winPercentage'])
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(city))
                self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(name))
                self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(gamesPlayed))
                self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(gamesWon))
                self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(gamesLost))
                self.tableWidget.setItem(rowPosition, 5, QTableWidgetItem(winPer))

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
