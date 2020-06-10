from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from tableWindow import Ui_tableWindow
from teamWindow import Ui_teamWindow
from gamesWindow import Ui_gamesWindow
#8082
class Ui_fanStart(object):
    def getTable(self):
        self.window = QMainWindow()
        self.ui = Ui_tableWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def getTeams(self):
        self.window = QMainWindow()
        self.ui = Ui_teamWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def getGames(self):
        self.window = QMainWindow()
        self.ui = Ui_gamesWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, fanStart):
        fanStart.setObjectName("fanStart")
        fanStart.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(fanStart)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gamesButton = QtWidgets.QPushButton(self.centralwidget)
        self.gamesButton.setObjectName("gamesButton")
        self.gamesButton.clicked.connect(self.getGames)
        self.verticalLayout.addWidget(self.gamesButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.tableButton = QtWidgets.QPushButton(self.centralwidget)
        self.tableButton.setObjectName("tableButton")
        self.tableButton.clicked.connect(self.getTable)
        self.verticalLayout.addWidget(self.tableButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.teamButton = QtWidgets.QPushButton(self.centralwidget)
        self.teamButton.setObjectName("teamButton")
        self.teamButton.clicked.connect(self.getTeams)
        self.verticalLayout.addWidget(self.teamButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        fanStart.setCentralWidget(self.centralwidget)

        self.retranslateUi(fanStart)
        QtCore.QMetaObject.connectSlotsByName(fanStart)

    def retranslateUi(self, fanStart):
        _translate = QtCore.QCoreApplication.translate
        fanStart.setWindowTitle(_translate("fanStart", "Fan"))
        self.gamesButton.setText(_translate("fanStart", "Games"))
        self.tableButton.setText(_translate("fanStart", "Table"))
        self.teamButton.setText(_translate("fanStart", "Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fanStart = QtWidgets.QMainWindow()
    ui = Ui_fanStart()
    ui.setupUi(fanStart)
    fanStart.show()
    sys.exit(app.exec_())
