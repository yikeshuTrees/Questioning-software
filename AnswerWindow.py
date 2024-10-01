import datetime
from tkinter.commondialog import Dialog

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog

import UI, random, sys
import configparser as cfp # configparser 用于读取配置文件
from openpyxl import load_workbook # 用于处理 Excel 文件
from collections import Counter

# 导入模块和库

class Ui_AnswerWindow(object):
    def setupUi(self, AnswerWindow):
        # 设置界面布局和控件属性
        # 初始化一些变量和配置文件
        self.t_question = []  # 正确答案列表
        self.e_question = []  # 错误答案列表
        self.t_choose = []  # 正确选择列表
        self.e_choose = []  # 错误选择列表
        self.file = cfp.ConfigParser()  # 创建配置文件解析器
        self.file.read('save.ini')  # 读取配置文件
        self.file['analysis'] = {}  # 初始化分析部分的配置
        self.file['answers'] = {'right': '0', 'bad': '0'}  # 初始化正确和错误次数

        # 加载 Excel 文件并获取工作表
        self.Answers_book = load_workbook(self.file['setting']['choose3'])
        self.Answers_sheet = self.Answers_book[self.file['setting']['c_sheet']]
        self.i = 0  #初始化变量
        self.right = 0  #初始化变量
        self.bad = 0  #初始化变量
        self.ran_list = []
        AnswerWindow.setObjectName("AnswerWindow")  # 设置窗口对象的名字
        AnswerWindow.resize(400, 300)  # 设置窗口大小
        self.window = AnswerWindow  # 保存窗口对象为self.window
        self.gridLayout = QtWidgets.QGridLayout(AnswerWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(AnswerWindow)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 361, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.NextButton = QtWidgets.QPushButton(AnswerWindow)
        self.NextButton.setMinimumSize(QtCore.QSize(75, 31))
        self.NextButton.setMaximumSize(QtCore.QSize(75, 31))
        self.NextButton.setObjectName("NextButton")
        self.gridLayout.addWidget(self.NextButton, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(AnswerWindow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 137))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CheckBoxA = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBoxA.sizePolicy().hasHeightForWidth())
        self.CheckBoxA.setSizePolicy(sizePolicy)
        self.CheckBoxA.setMinimumSize(QtCore.QSize(0, 16))
        self.CheckBoxA.setObjectName("CheckBoxA")
        self.verticalLayout.addWidget(self.CheckBoxA)
        self.CheckBoxB = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBoxB.sizePolicy().hasHeightForWidth())
        self.CheckBoxB.setSizePolicy(sizePolicy)
        self.CheckBoxB.setMinimumSize(QtCore.QSize(0, 16))
        self.CheckBoxB.setObjectName("CheckBoxB")
        self.verticalLayout.addWidget(self.CheckBoxB)
        self.CheckBoxC = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBoxC.sizePolicy().hasHeightForWidth())
        self.CheckBoxC.setSizePolicy(sizePolicy)
        self.CheckBoxC.setMinimumSize(QtCore.QSize(0, 16))
        self.CheckBoxC.setObjectName("CheckBoxC")
        self.verticalLayout.addWidget(self.CheckBoxC)
        self.CheckBoxD = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBoxD.sizePolicy().hasHeightForWidth())
        self.CheckBoxD.setSizePolicy(sizePolicy)
        self.CheckBoxD.setMinimumSize(QtCore.QSize(0, 16))
        self.CheckBoxD.setObjectName("CheckBoxD")
        self.verticalLayout.addWidget(self.CheckBoxD)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 2)
        self.scrollArea_2 = QtWidgets.QScrollArea(AnswerWindow)
        self.scrollArea_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 363, 128))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(340, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea_2, 0, 0, 1, 2)

        self.retranslateUi(AnswerWindow)  #调用翻译方法
        QtCore.QMetaObject.connectSlotsByName(AnswerWindow)  #连接槽函数和槽

        self.NextButton.clicked.connect(self.get_choose_1)
        #print('UI放置成功')
    def get_choose_1(self): # 当点击“确定”按钮时，获取用户选择的答案并处理
        # 获取用户选择的答案
        answer = []
        if self.CheckBoxA.isChecked():
            answer.append('A')
            #print(f'checkA:{answer}')
        if self.CheckBoxB.isChecked():
            answer.append('B')
            #print(f'checkB:{answer}')
        if self.CheckBoxC.isChecked():
            answer.append('C')
            #print(f'checkC:{answer}')
        if self.CheckBoxD.isChecked():
            answer.append('D')
            #print(f'checkD:{answer}')
        print(answer,self.t_answer)
        if not(self.CheckBoxA.isChecked() or self.CheckBoxB.isChecked() or self.CheckBoxC.isChecked() or self.CheckBoxD.isChecked()):
            UI.e_textW('请选择答案！！！')
            return 0
        # 根据用户选择的答案，更新正确或错误次数，保存到配置文件
        elif dict(Counter(answer)) == dict(Counter(self.t_answer)):
            self.right += 1
            self.file['analysis']['analysis'] = str(self.ran)
            self.file['analysis']['judge'] = '答对了\n'
            self.file['answers']['right'] = str(self.right)
            self.t_question.append(self.ran)
            self.t_choose.append(answer)
            #print(self.t_question,self.t_choose)
            with open('save.ini', 'w') as configfile:
                self.file.write(configfile)
            # 如果用户选择了正确答案，显示解析（如果配置允许）
            if self.file['setting']['choose1'] == '做题过程有解析（做一题出一题的解析）':
                UI.AnalysisW()
            # 更新界面，准备下一题
            self.i += 1
            self.check_condition()
        else:
            self.bad += 1
            self.file['analysis']['analysis'] = str(self.ran)
            self.file['analysis']['judge'] = '答错了\n'
            self.file['answers']['bad'] = str(self.bad)
            self.e_question.append(self.ran)
            self.e_choose.append(answer)
            #print(self.e_question,self.e_choose)
            with open('save.ini', 'w') as configfile:
                self.file.write(configfile)
            # 如果用户选择了错误答案，显示解析（如果配置允许）
            if (self.file['setting']['choose1'] == '做题过程有解析（做一题出一题的解析）') \
                    or (self.file['setting']['choose1'] == '正确的题无需解析（错误的题有解析）' \
                        and self.file['analysis']['judge'] == '答错了\n'):
                UI.AnalysisW()
            # 更新界面，准备下一题
            self.i += 1
            self.check_condition()
    def check_condition(self):
        # 如果已经完成所有题目，保存最终分析结果并关闭窗口
        if self.i == int(self.file.get('setting', 'num')):
            #print('题目已出完')
            self.file['end_analysis'] = {
                't_question':','.join(str(item) for item in self.t_question),
                'e_question':','.join(str(item) for item in self.e_question),
                't_choose':'<~!~>'.join(str(item) for item in self.t_choose),
                'e_choose':'<~!~>'.join(str(item) for item in self.e_choose)}
            with open('save.ini', 'w') as configfile:
                self.file.write(configfile)
            self.window.close()
            UI.EndW()
            self.Answers_book.close()
        # 如果还有题目，继续加载下一题
        else:
            #print('题目未出完')
            i = []
            if self.file['setting']['choose2'] == 'None':
                self.ran = random.choice(self.random_list) + 2
                self.random_list.remove(self.ran-2)
                #print(f'出现题成功\n剩余题数:{self.random_list}')
            else:
                self.ran = random.randint(2, len(self.random_list))
            for b in self.Answers_sheet[f'A{self.ran}:G{self.ran}']:
                AQA_list = b
            #print("遍历A到F成功")
            #print(self.random_list)
            print(AQA_list)
            print(AQA_list[6].value)
            self.t_answer = str(AQA_list[6].value).split(',')
            self.CheckBoxA.setText(str(AQA_list[2].value))
            self.CheckBoxB.setText((AQA_list[3].value))
            self.CheckBoxC.setText(str(AQA_list[4].value))
            self.CheckBoxD.setText( str(AQA_list[5].value))
            self.label.setText(str(AQA_list[0].value))
            #print('随机选项成功')

    def retranslateUi(self, AnswerWindow):
        #遍历所选题库的sheet页的“A”列拥有的行数
        for rows in self.Answers_sheet['A']:
            if rows.value == None:
                break
        #print(f'遍历题目成功\n{rows}')
        #定义random_list并将其元素数等同于题数
        self.random_list = []
        for f in range(rows.row-2):
            self.random_list.append(f)
        #print(self.random_list)
        #随机选一题
        if self.file['setting']['choose2'] == 'None':
            #如果没勾选“重复题目”就将随机选到的题从random_list去除，以便之后判断
            self.ran = random.choice(self.random_list) + 2
            self.random_list.remove(self.ran-2)
        else:
            #如果勾选就随便出
            self.ran = random.randint(2, rows.row - 1)
        #print('随机出题成功')
        # 设置标签（label）的文本自动换行，以便长文本能够正确显示。
        self.label.setWordWrap(True)
        # 获取翻译函数，这个函数用于将字符串从程序的默认语言翻译成用户设置的语言。
        _translate = QtCore.QCoreApplication.translate
        # 初始化一个空列表，用于存储从 Excel 文件中读取的问题和选项。
        i = []
        # 初始化一个空列表，用于存储当前题目的答案选项。
        AQA_list = []
        # 设置当前题目的随机行号，这个行号会保存到配置文件中。
        self.file['analysis']['analysis'] = str(self.ran)
        # 遍历 Excel 文件中指定行（从 A 列到 G 列）的数据，并将每一行的数据存储到 AQA_list 中。
        for b in self.Answers_sheet[f'A{self.ran}:G{self.ran}']:
            AQA_list = b
        #print(f'遍历A到G成功，AQA_list:{AQA_list}')
        # 设置窗口标题为“答题中”，并使用翻译函数确保标题正确翻译。
        AnswerWindow.setWindowTitle(_translate("AnswerWindow", "答题中"))
        self.textBrowser.setHtml(_translate("AnswerWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">题目测试：要在控制台输出‘hello, world’下面哪个代码是正确的？( )</p></body></html>"))
        self.CheckBoxA.setText(_translate("AnswerWindow", "A.print(\'hello, world\')"))
        self.CheckBoxB.setText(_translate("AnswerWindow", "B.print(hello, world)"))
        self.CheckBoxC.setText(_translate("AnswerWindow", "C.print(\'hellonworld\')"))
        self.CheckBoxD.setText(_translate("AnswerWindow", "D.print(\'helloworld)"))
        # 获取当前题目的正确答案。
        self.t_answer = str(AQA_list[6].value).split(',')
        self.CheckBoxA.setText(_translate("AnswerWindow", str(AQA_list[2].value)))
        self.CheckBoxB.setText(_translate("AnswerWindow", str(AQA_list[3].value)))
        self.CheckBoxC.setText(_translate("AnswerWindow", str(AQA_list[4].value)))
        self.CheckBoxD.setText(_translate("AnswerWindow", str(AQA_list[5].value)))
        #print(f'随机选项成功')

        self.NextButton.setText(_translate("AnswerWindow", "确定"))
        self.label.setText(_translate("AnswerWindow", str(AQA_list[0].value)))
        #print('初始化成功')
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_AnswerWindow()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())