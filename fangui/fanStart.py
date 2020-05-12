# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fanStart.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fanStart(object):
    def setupUi(self, fanStart):
        fanStart.setObjectName("fanStart")
        fanStart.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(fanStart)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gamesButton = QtWidgets.QPushButton(self.centralwidget)
        self.gamesButton.setObjectName("gamesButton")
        self.verticalLayout.addWidget(self.gamesButton)
        self.tableButton = QtWidgets.QPushButton(self.centralwidget)
        self.tableButton.setObjectName("tableButton")
        self.verticalLayout.addWidget(self.tableButton)
        self.teamButton = QtWidgets.QPushButton(self.centralwidget)
        self.teamButton.setObjectName("teamButton")
        self.verticalLayout.addWidget(self.teamButton)
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
