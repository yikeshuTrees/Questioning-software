# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e_text.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_e_text(object):
    def __init__(self,text):
        print(text)
        self.text = text
    def setupUi(self, e_text):
        e_text.setObjectName("e_text")
        e_text.resize(316, 170)
        self.buttonBox = QtWidgets.QDialogButtonBox(e_text)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(e_text)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 111))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        self.retranslateUi(e_text,self.text)
        self.buttonBox.accepted.connect(e_text.accept) # type: ignore
        self.buttonBox.rejected.connect(e_text.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(e_text)

    def retranslateUi(self, e_text, text):
        _translate = QtCore.QCoreApplication.translate
        e_text.setWindowTitle(_translate("e_text", "报错"))
        self.label.setText(_translate("e_text", f"{text}"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    e_text = QtWidgets.QDialog()
    ui = Ui_e_text()
    ui.setupUi(e_text)
    e_text.show()
    sys.exit(app.exec_())
