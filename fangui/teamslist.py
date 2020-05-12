# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teamslist.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_teamsChoose(object):
    def setupUi(self, teamsChoose):
        teamsChoose.setObjectName("teamsChoose")
        teamsChoose.resize(640, 80)
        self.verticalLayout = QtWidgets.QVBoxLayout(teamsChoose)
        self.verticalLayout.setObjectName("verticalLayout")
        self.teamsList = QtWidgets.QComboBox(teamsChoose)
        self.teamsList.setObjectName("teamsList")
        self.verticalLayout.addWidget(self.teamsList)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.applyButton = QtWidgets.QPushButton(teamsChoose)
        self.applyButton.setObjectName("applyButton")
        self.verticalLayout.addWidget(self.applyButton)

        self.retranslateUi(teamsChoose)
        QtCore.QMetaObject.connectSlotsByName(teamsChoose)

    def retranslateUi(self, teamsChoose):
        _translate = QtCore.QCoreApplication.translate
        teamsChoose.setWindowTitle(_translate("teamsChoose", "Teams List"))
        self.applyButton.setText(_translate("teamsChoose", "Show Team"))
