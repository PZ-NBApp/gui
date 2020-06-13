# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gamesWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gamesWindow(object):
    def setupUi(self, gamesWindow):
        gamesWindow.setObjectName("gamesWindow")
        gamesWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(gamesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        gamesWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(gamesWindow)
        QtCore.QMetaObject.connectSlotsByName(gamesWindow)

    def retranslateUi(self, gamesWindow):
        _translate = QtCore.QCoreApplication.translate
        gamesWindow.setWindowTitle(_translate("gamesWindow", "Games"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gamesWindow = QtWidgets.QMainWindow()
    ui = Ui_gamesWindow()
    ui.setupUi(gamesWindow)
    gamesWindow.show()
    sys.exit(app.exec_())
