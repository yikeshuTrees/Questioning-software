# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Analysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#hello world
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtWidgets
from openpyxl import load_workbook
import configparser as cfp

class Ui_Analysis(object):
    def setupUi(self, Analysis):
        self.file = cfp.ConfigParser()
        self.file.read('save.ini')
        self.ran = self.file.get('analysis','analysis')
        self.Answers_book = load_workbook(self.file['setting']['choose3'])  #创建xw对象
        self.Answers_sheet = self.Answers_book[self.file['setting']['c_sheet']]  #获取sheet页
        Analysis.setObjectName("Analysis")
        Analysis.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Analysis)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Analysis_2 = QtWidgets.QLabel(Analysis)
        self.Analysis_2.setMinimumSize(QtCore.QSize(361, 191))
        self.Analysis_2.setTextFormat(QtCore.Qt.AutoText)
        self.Analysis_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Analysis_2.setObjectName("Analysis_2")
        self.verticalLayout.addWidget(self.Analysis_2)
        self.pushButton = QtWidgets.QPushButton(Analysis)
        self.pushButton.setMaximumSize(QtCore.QSize(75, 51))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Analysis)
        QtCore.QMetaObject.connectSlotsByName(Analysis)

        self.pushButton.clicked.connect(self.close)
        self.pushButton.clicked.connect(Analysis.close)
    def close(self):
        self.Answers_book.close()
    def retranslateUi(self, Analysis):
        self.Analysis_2.setWordWrap(True)
        _translate = QtCore.QCoreApplication.translate
        ran = self.Answers_sheet[f'B{self.ran}']
        judge = self.file['analysis']['judge']
        Analysis.setWindowTitle(_translate("Analysis", "解析"))
        self.Analysis_2.setText(_translate("Analysis", f"{judge}\n解析：{ran.value}"))
        self.pushButton.setText(_translate("Analysis", "确定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Analysis = QtWidgets.QWidget()
    ui = Ui_Analysis()
    ui.setupUi(Analysis)
    Analysis.show()
    sys.exit(app.exec_())
