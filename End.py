# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'End.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
import configparser as cfp
import datetime, os, UI
from openpyxl import load_workbook

class Ui_End(object):
    def setupUi(self, End):
        self.file = cfp.ConfigParser()
        self.file.read('save.ini')  # 读取配置文件
        self.Answers_book = load_workbook(self.file['setting']['choose3'])  #创建xw对象
        self.Answers_sheet = self.Answers_book[self.file['setting']['c_sheet']]  #获取sheet页
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
        End.setObjectName("End")
        End.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(End)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 221, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Questions = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Questions.setObjectName("Questions")
        self.verticalLayout.addWidget(self.Questions)
        self.Time = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Time.setObjectName("Time")
        self.verticalLayout.addWidget(self.Time)
        self.Tnumber = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Tnumber.setObjectName("Tnumber")
        self.verticalLayout.addWidget(self.Tnumber)
        self.Fnumber = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Fnumber.setObjectName("Fnumber")
        self.verticalLayout.addWidget(self.Fnumber)
        self.Anumber = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Anumber.setObjectName("Anumber")
        self.verticalLayout.addWidget(self.Anumber)
        self.Accuracy = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Accuracy.setObjectName("Accuracy")
        self.verticalLayout.addWidget(self.Accuracy)
        self.FButton = QtWidgets.QPushButton(End)
        self.FButton.setGeometry(QtCore.QRect(240, 60, 141, 41))
        self.FButton.setObjectName("FButton")
        self.AButton = QtWidgets.QPushButton(End)
        self.AButton.setGeometry(QtCore.QRect(240, 110, 141, 41))
        self.AButton.setObjectName("AButton")
        self.TButton = QtWidgets.QPushButton(End)
        self.TButton.setGeometry(QtCore.QRect(240, 10, 141, 41))
        self.TButton.setObjectName("TButton")
        self.EndButton = QtWidgets.QPushButton(End)
        self.EndButton.setGeometry(QtCore.QRect(310, 260, 81, 31))
        self.EndButton.setObjectName("EndButton")
        self.SButton = QtWidgets.QPushButton(End)
        self.SButton.setGeometry(QtCore.QRect(240, 160, 141, 41))
        self.SButton.setObjectName("SButton")

        self.retranslateUi(End)
        QtCore.QMetaObject.connectSlotsByName(End)

        self.EndButton.clicked.connect(End.close)
        self.SButton.clicked.connect(self.save)
        self.FButton.clicked.connect(self.Fchoose)
        self.TButton.clicked.connect(self.Tchoose)
        self.AButton.clicked.connect(self.Achoose)

    def Fchoose(self):
        self.file['End_analysis'] = {
            'choose': '错题解析'
        }
        with open('save.ini', 'w') as configfile:
            self.file.write(configfile)
        if self.file['end_analysis']['e_question'] == '':
            UI.e_textW('不好意思，你没有做错的题，点这个没用')
        else:
            UI.q_analysisW()
    def Tchoose(self):
        self.file['End_analysis'] = {
            'choose': '对题解析'
        }
        with open('save.ini', 'w') as configfile:
            self.file.write(configfile)
        if self.file['end_analysis']['t_question'] == '':
            UI.e_textW('不好意思，你没有做对的题，点这个没用')
        else:
            UI.q_analysisW()

    def Achoose(self):
        self.file['End_analysis'] = {
            'choose':'所有解析'
        }
        with open('save.ini', 'w') as configfile:
            self.file.write(configfile)
        UI.q_analysisW()
    def save(self):
        print(f"选择题库：选择题库：{self.file['setting']['choose3']}"
              f"页:{self.file['setting']['c_sheet']}\n"
              f"完成时间：\n"
              f"正确题目数量：{self.file['answers']['right']}\n"
              f"错误题目数量：{self.file['answers']['bad']}\n"
              f"总题目数量：{self.file['setting']['num']}\n"
              f"正确率：{self.rightlv}%")
        t = datetime.datetime.now()
        name = f'{t.year}年{t.month}月{t.day}日{t.hour}时{t.minute}分'
        file = open(f'{name}.txt','a')
        file.write(f"选择题库：{self.file['setting']['choose3']}\n"
                   f"页:{self.file['setting']['c_sheet']}\n"
              f"完成时间：\
{datetime.datetime.now() - datetime.datetime.strptime(self.file['setting']['start_time'], '%Y-%m-%d %H:%M:%S.%f')}\n"
              f"正确题目数量：{self.file['answers']['right']}\n"
              f"错误题目数量：{self.file['answers']['bad']}\n"
              f"总题目数量：{self.file['setting']['num']}\n"
              f"正确率：{self.rightlv}%\n\n")
        e = 0
        for i in self.a_list:
            a = self.Answers_sheet[f'C{self.a_list[e]}:F{self.a_list[e]}']
            b = a[0]
            c = 0
            d = []
            print(len(b))
            for i in b:
                d.append(b[c].value)
                c += 1
            file.write(f"题目：{self.Answers_sheet[f'B{self.a_list[e]}'].value}\n"\
                       f"正确选项：{d[0]}\n错误选项：{d[1], d[2], d[3]}\n你的选择：{self.c_list[e]}\n"\
                       f"解析：{self.Answers_sheet[f'A{self.a_list[e]}'].value}\n\n")
            e += 1
    def retranslateUi(self, End):
        _translate = QtCore.QCoreApplication.translate
        End.setWindowTitle(_translate("End", "结算"))
        self.Questions.setWordWrap(True)
        self.Questions.setText(_translate("End", f"选择题库：{self.file['setting']['choose3']}"
                                                 f"(分类:{self.file['setting']['c_sheet']})"))
        self.Time.setText(_translate("End", f"完成时间：\
{datetime.datetime.now() - datetime.datetime.strptime(self.file['setting']['start_time'], '%Y-%m-%d %H:%M:%S.%f')}"))
        self.Tnumber.setText(_translate("End", f"正确题目数量：{self.file['answers']['right']}"))
        self.Fnumber.setText(_translate("End", f"错误题目数量：{self.file['answers']['bad']}"))
        self.Anumber.setText(_translate("End", f"总题目数量：{self.file['setting']['num']}"))
        self.rightlv = 100 * (int(self.file['answers']['right']) / int(self.file['setting']['num']))
        self.Accuracy.setText(_translate("End", f"正确率：{self.rightlv}%"))
        self.FButton.setText(_translate("End", "查看所有错题解析"))
        self.AButton.setText(_translate("End", "查看所有解析"))
        self.TButton.setText(_translate("End", "查看所有对题解析"))
        self.EndButton.setText(_translate("End", "结束"))
        self.SButton.setText(_translate("End", "保存数据"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    End = QtWidgets.QWidget()
    ui = Ui_End()
    ui.setupUi(End)
    End.show()
    sys.exit(app.exec_())
