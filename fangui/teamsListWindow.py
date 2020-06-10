# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teamsListWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_teamsListWindow(object):
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
        self.verticalLayout_2.addWidget(self.applyButton)
        teamsListWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(teamsListWindow)
        QtCore.QMetaObject.connectSlotsByName(teamsListWindow)

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
