# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'q_analysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
import configparser as cfp
from openpyxl import load_workbook

class Ui_q_analysis(object):
    def setupUi(self, q_analysis):
        self.file = cfp.ConfigParser()
        self.file.read('save.ini')
        self.Answers_book = load_workbook(self.file['setting']['choose3'])  #创建xw对象
        self.Answers_sheet = self.Answers_book[self.file['setting']['c_sheet']]  #获取sheet页
        if self.file['End_analysis']['choose'] == '错题解析':
            self.a_list = self.file['end_analysis']['e_question'].split(',')
            self.c_list = self.file['end_analysis']['e_choose'].split('<~!~>')
        elif self.file['End_analysis']['choose'] == '对题解析':
            self.a_list = self.file['end_analysis']['t_question'].split(',')
            self.c_list = self.file['end_analysis']['t_choose'].split('<~!~>')
        else:
            if self.file['end_analysis']['e_question'] == '':
                self.a_list = self.file['end_analysis']['t_question'].split(',')
                self.c_list = self.file['end_analysis']['t_choose'].split('<~!~>')
            elif self.file['end_analysis']['t_question'] == '':
                self.a_list = self.file['end_analysis']['e_question'].split(',')
                self.c_list = self.file['end_analysis']['e_choose'].split('<~!~>')
            else:
                self.a_list = self.file['end_analysis']['e_question'].split(',') \
                              + self.file['end_analysis']['t_question'].split(',')
                self.c_list = self.file['end_analysis']['e_choose'].split('<~!~>') \
                              + self.file['end_analysis']['t_choose'].split('<~!~>')
        print(self.a_list,self.c_list)
        q_analysis.setObjectName("q_analysis")
        q_analysis.resize(532, 341)
        self.gridLayout = QtWidgets.QGridLayout(q_analysis)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(q_analysis)
        self.comboBox.setGeometry(QtCore.QRect(300, 0, 231, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QtCore.QSize(231, 41))
        self.comboBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setPlaceholderText("")
        self.comboBox.setObjectName("comboBox")
        for i in self.a_list:
            self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.question = QtWidgets.QLabel(q_analysis)
        self.question.setMinimumSize(QtCore.QSize(261, 121))
        self.question.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.question.setObjectName("question")
        self.gridLayout.addWidget(self.question, 1, 0, 1, 1)
        self.analysis = QtWidgets.QLabel(q_analysis)
        self.analysis.setMinimumSize(QtCore.QSize(221, 231))
        self.analysis.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.analysis.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.analysis.setObjectName("analysis")
        self.gridLayout.addWidget(self.analysis, 1, 1, 2, 1)
        self.choose = QtWidgets.QLabel(q_analysis)
        self.choose.setMinimumSize(QtCore.QSize(261, 91))
        self.choose.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.choose.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.choose.setObjectName("choose")
        self.gridLayout.addWidget(self.choose, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(q_analysis)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 41))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 41))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)

        self.retranslateUi(q_analysis)
        self.comboBox.highlighted['int'].connect(self.hightlight) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(q_analysis)

        self.pushButton.clicked.connect(q_analysis.close)

    def hightlight(self,text):
        print(text,type(text))
        self.question.setText(f"题目：{self.Answers_sheet[f'B{self.a_list[text]}'].value}")
        a = self.Answers_sheet[f'C{self.a_list[text]}:F{self.a_list[text]}']
        b = a[0]
        c = 0
        d = []
        print(len(b))
        for i in b:
            d.append(b[c].value)
            c += 1
        self.choose.setText(f"正确选项：{d[0]}\n错误选项：{d[1],d[2],d[3]}\n你的选择：{self.c_list[text]}")
        self.analysis.setText(f"解析：{self.Answers_sheet[f'A{self.a_list[text]}'].value}")
    def retranslateUi(self, q_analysis):
        _translate = QtCore.QCoreApplication.translate
        q_analysis.setWindowTitle(_translate("q_analysis", "题目解析"))
        a = 0
        for i in self.a_list:
            self.comboBox.setItemText(a, _translate("q_analysis", f"{self.Answers_sheet[f'B{i}'].value}"))
            a += 1
        self.pushButton.setText(_translate("q_analysis", "返回"))
        self.question.setText(_translate("q_analysis", "题目："))
        self.analysis.setText(_translate("q_analysis", "解析："))
        self.choose.setText(_translate("q_analysis", "选项："))
        self.analysis.setText(_translate("q_analysis", "解析："))
        self.question.setWordWrap(True)
        self.choose.setWordWrap(True)
        self.analysis.setWordWrap(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    q_analysis = QtWidgets.QWidget()
    ui = Ui_q_analysis()
    ui.setupUi(q_analysis)
    q_analysis.show()
    sys.exit(app.exec_())
