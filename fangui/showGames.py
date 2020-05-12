# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showGames.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_games(object):
    def setupUi(self, games):
        games.setObjectName("games")
        games.resize(640, 480)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(games)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gamesList = QtWidgets.QListView(games)
        self.gamesList.setObjectName("gamesList")
        self.verticalLayout.addWidget(self.gamesList)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(games)
        QtCore.QMetaObject.connectSlotsByName(games)

    def retranslateUi(self, games):
        _translate = QtCore.QCoreApplication.translate
        games.setWindowTitle(_translate("games", "Games"))
