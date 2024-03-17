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
        #print(self.a_list,self.c_list)
        q_analysis.setObjectName("q_analysis")
        q_analysis.resize(578, 323)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(q_analysis.sizePolicy().hasHeightForWidth())
        q_analysis.setSizePolicy(sizePolicy)
        q_analysis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(q_analysis)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(q_analysis)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 25))
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
        self.pushButton = QtWidgets.QPushButton(q_analysis)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 41))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 50))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(q_analysis)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 258, 249))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.analysis = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysis.sizePolicy().hasHeightForWidth())
        self.analysis.setSizePolicy(sizePolicy)
        self.analysis.setMinimumSize(QtCore.QSize(210, 0))
        self.analysis.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.analysis.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.analysis.setWordWrap(True)
        self.analysis.setObjectName("analysis")
        self.verticalLayout_3.addWidget(self.analysis)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout.addWidget(self.scrollArea_2, 1, 1, 3, 1)
        self.scrollArea = QtWidgets.QScrollArea(q_analysis)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -65, 258, 378))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.choose = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose.sizePolicy().hasHeightForWidth())
        self.choose.setSizePolicy(sizePolicy)
        self.choose.setMinimumSize(QtCore.QSize(210, 0))
        self.choose.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.choose.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.choose.setWordWrap(True)
        self.choose.setObjectName("choose")
        self.verticalLayout_2.addWidget(self.choose)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 1)
        self.scrollArea_3 = QtWidgets.QScrollArea(q_analysis)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 258, 140))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_4.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.question = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question.sizePolicy().hasHeightForWidth())
        self.question.setSizePolicy(sizePolicy)
        self.question.setMinimumSize(QtCore.QSize(210, 0))
        self.question.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.question.setWordWrap(True)
        self.question.setObjectName("question")
        self.verticalLayout_4.addWidget(self.question)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout.addWidget(self.scrollArea_3, 1, 0, 2, 1)

        self.retranslateUi(q_analysis)
        self.comboBox.highlighted['int'].connect(self.hightlight) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(q_analysis)

        self.pushButton.clicked.connect(q_analysis.close)

    def hightlight(self,text):
        #print(text,type(text))
        self.question.setText(f"题目：{self.Answers_sheet[f'B{self.a_list[text]}'].value}")
        a = self.Answers_sheet[f'C{self.a_list[text]}:F{self.a_list[text]}']
        b = a[0]
        c = 0
        d = []
        #print(len(b))
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
