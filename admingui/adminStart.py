from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from addPlayerWindow import Ui_addPlayerWindow
from createGameWindow import Ui_createGameWindow
from addTeamWindow import Ui_addTeamWindow
from assignationWindow import Ui_assignationWindow
#8080

class Ui_adminStart(object):
    def show_addPlayer(self):
        self.window = QMainWindow()
        self.ui = Ui_addPlayerWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_addTeam(self):
        self.window = QMainWindow()
        self.ui = Ui_addTeamWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_createGame(self):
        self.window = QMainWindow()
        self.ui = Ui_createGameWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_addAssignation(self):
        self.window = QMainWindow()
        self.ui = Ui_assignationWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, adminStart):
        adminStart.setObjectName("adminStart")
        adminStart.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(adminStart)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.addPlayerButton = QtWidgets.QPushButton(self.centralwidget)
        self.addPlayerButton.setObjectName("addPlayerButton")
        self.verticalLayout.addWidget(self.addPlayerButton)
        self.addPlayerButton.clicked.connect(self.show_addPlayer)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.addAssignationButton = QtWidgets.QPushButton(self.centralwidget)
        self.addAssignationButton.setObjectName("addAssignationButton")
        self.addAssignationButton.clicked.connect(self.show_addAssignation)
        self.verticalLayout.addWidget(self.addAssignationButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.addTeamButton = QtWidgets.QPushButton(self.centralwidget)
        self.addTeamButton.setObjectName("addTeamButton")
        self.verticalLayout.addWidget(self.addTeamButton)
        self.addTeamButton.clicked.connect(self.show_addTeam)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.createGameButton = QtWidgets.QPushButton(self.centralwidget)
        self.createGameButton.setObjectName("createGameButton")
        self.verticalLayout.addWidget(self.createGameButton)
        self.createGameButton.clicked.connect(self.show_createGame)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        adminStart.setCentralWidget(self.centralwidget)

        self.retranslateUi(adminStart)
        QtCore.QMetaObject.connectSlotsByName(adminStart)

    def retranslateUi(self, adminStart):
        _translate = QtCore.QCoreApplication.translate
        adminStart.setWindowTitle(_translate("adminStart", "Admin"))
        self.addPlayerButton.setText(_translate("adminStart", "Add Player"))
        self.addAssignationButton.setText(_translate("adminStart", "Add Assignation"))
        self.addTeamButton.setText(_translate("adminStart", "Add Team"))
        self.createGameButton.setText(_translate("adminStart", "Create game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminStart = QtWidgets.QMainWindow()
    ui = Ui_adminStart()
    ui.setupUi(adminStart)
    adminStart.show()
    sys.exit(app.exec_())
