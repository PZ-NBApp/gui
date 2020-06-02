from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addTeam(object):
    def setupUi(self, addTeam):
        addTeam.setObjectName("addTeam")
        addTeam.resize(640, 107)
        self.verticalLayout = QtWidgets.QVBoxLayout(addTeam)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(addTeam)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.cityLabel = QtWidgets.QLabel(addTeam)
        self.cityLabel.setObjectName("cityLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.cityLabel)
        self.applyButton = QtWidgets.QPushButton(addTeam)
        self.applyButton.setObjectName("applyButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.applyButton)
        self.nameInput = QtWidgets.QLineEdit(addTeam)
        self.nameInput.setObjectName("nameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameInput)
        self.cityInput = QtWidgets.QLineEdit(addTeam)
        self.cityInput.setObjectName("cityInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cityInput)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(addTeam)
        QtCore.QMetaObject.connectSlotsByName(addTeam)

    def retranslateUi(self, addTeam):
        _translate = QtCore.QCoreApplication.translate
        addTeam.setWindowTitle(_translate("addTeam", "Add Team"))
        self.nameLabel.setText(_translate("addTeam", "Name"))
        self.cityLabel.setText(_translate("addTeam", "City"))
        self.applyButton.setText(_translate("addTeam", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addTeam = QtWidgets.QWidget()
    ui = Ui_addTeam()
    ui.setupUi(addTeam)
    addTeam.show()
    sys.exit(app.exec_())
