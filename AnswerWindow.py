import datetime

from PyQt5 import QtCore, QtWidgets
import UI, random
import configparser as cfp
from openpyxl import load_workbook

# 导入模块和库

class Ui_AnswerWindow(object):
    def setupUi(self, AnswerWindow):
        # 设置界面布局和控件属性
        self.t_question = []
        self.e_question = []
        self.t_choose = []
        self.e_choose = []
        self.file = cfp.ConfigParser()
        self.file.read('save.ini')  #读取配置文件
        self.file['analysis'] = {}  #初始化配置文件
        self.file['answers'] = {
            'right':'0',
            'bad':'0'
        }
        self.Answers_book = load_workbook(self.file['setting']['choose3'])  #创建xw对象
        self.Answers_sheet = self.Answers_book[self.file['setting']['c_sheet']]  #获取sheet页
        self.i = 0  #初始化变量
        self.right = 0  #初始化变量
        self.bad = 0  #初始化变量
        self.ran_list = []
        for rows in self.Answers_sheet['A']:
            if rows.value == None:
                break
        if self.file['setting']['choose2'] == 'None':
            self.ran = random.randint(2, rows.row - 1)
            self.ran_list.append(self.ran)
        else:
            self.ran = random.randint(2, rows.row - 1)
        AnswerWindow.setObjectName("AnswerWindow")  # 设置窗口对象的名字
        AnswerWindow.resize(400, 300)  # 设置窗口大小
        self.window = AnswerWindow  # 保存窗口对象为self.window
        self.gridLayout = QtWidgets.QGridLayout(AnswerWindow)
        self.gridLayout.setObjectName("gridLayout")
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
        self.radioButtonA = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonA.sizePolicy().hasHeightForWidth())
        self.radioButtonA.setSizePolicy(sizePolicy)
        self.radioButtonA.setMinimumSize(QtCore.QSize(0, 16))
        self.radioButtonA.setObjectName("radioButtonA")
        self.verticalLayout.addWidget(self.radioButtonA)
        self.radioButtonB = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonB.sizePolicy().hasHeightForWidth())
        self.radioButtonB.setSizePolicy(sizePolicy)
        self.radioButtonB.setMinimumSize(QtCore.QSize(0, 16))
        self.radioButtonB.setObjectName("radioButtonB")
        self.verticalLayout.addWidget(self.radioButtonB)
        self.radioButtonC = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonC.sizePolicy().hasHeightForWidth())
        self.radioButtonC.setSizePolicy(sizePolicy)
        self.radioButtonC.setMinimumSize(QtCore.QSize(0, 16))
        self.radioButtonC.setObjectName("radioButtonC")
        self.verticalLayout.addWidget(self.radioButtonC)
        self.radioButtonD = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonD.sizePolicy().hasHeightForWidth())
        self.radioButtonD.setSizePolicy(sizePolicy)
        self.radioButtonD.setMinimumSize(QtCore.QSize(0, 16))
        self.radioButtonD.setObjectName("radioButtonD")
        self.verticalLayout.addWidget(self.radioButtonD)
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
    def get_choose_1(self):
        if self.radioButtonA.isChecked():
            answer = self.radioButtonA.text()
            print(f'checkA:{answer}')
        elif self.radioButtonB.isChecked():
            answer = self.radioButtonB.text()
            print(f'checkB:{answer}')
        elif self.radioButtonC.isChecked():
            answer = self.radioButtonC.text()
            print(f'checkC:{answer}')
        elif self.radioButtonD.isChecked():
            answer = self.radioButtonD.text()
            print(f'checkD:{answer}')
        else:
            answer = 'error'
        if answer == 'error':
            UI.e_textW('请选择答案！！！')
        elif answer == self.t_answer:
            self.right += 1
            self.file['analysis']['analysis'] = str(self.ran)
            self.file['analysis']['judge'] = '答对了\n'
            self.file['answers']['right'] = str(self.right)
            self.t_question.append(self.ran)
            self.t_choose.append(answer)
            print(self.t_question,self.t_choose)
            with open('save.ini', 'w') as configfile:
                self.file.write(configfile)
            if self.file['setting']['choose1'] == '做题过程有解析（做一题出一题的解析）':
                UI.AnalysisW()
            self.i += 1
            self.check_condition()
        else:
            self.bad += 1
            self.file['analysis']['analysis'] = str(self.ran)
            self.file['analysis']['judge'] = '答错了\n'
            self.file['answers']['bad'] = str(self.bad)
            self.e_question.append(self.ran)
            self.e_choose.append(answer)
            print(self.e_question,self.e_choose)
            with open('save.ini', 'w') as configfile:
                self.file.write(configfile)
            if (self.file['setting']['choose1'] == '做题过程有解析（做一题出一题的解析）') \
                    or (self.file['setting']['choose1'] == '正确的题无需解析（错误的题有解析）' \
                        and self.file['analysis']['judge'] == '答错了\n'):
                UI.AnalysisW()
            self.i += 1
            self.check_condition()
    def check_condition(self):
        if self.i == int(self.file.get('setting', 'num')):
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
        else:
            i = []
            for rows in self.Answers_sheet['A']:
                if rows.value == None:
                    break
            if self.file['setting']['choose2'] == 'None':
                self.ran = random.randint(2, rows.row - 1)
                while self.ran in self.ran_list:
                    self.ran = random.randint(2, rows.row - 1)
                self.ran_list.append(self.ran)
            else:
                self.ran = random.randint(2, rows.row - 1)
            for b in self.Answers_sheet[f'A{self.ran}:F{self.ran}']:
                AQA_list = b
            self.t_answer = AQA_list[2].value
            a = random.randint(2, 5)
            i.append(a)
            self.radioButtonA.setText(AQA_list[a].value)
            while a in i:
                a = random.randint(2, 5)
            i.append(a)
            self.radioButtonB.setText(AQA_list[a].value)
            while a in i:
                a = random.randint(2, 5)
            i.append(a)
            self.radioButtonC.setText(AQA_list[a].value)
            while a in i:
                a = random.randint(2, 5)
            i.append(a)
            self.radioButtonD.setText(AQA_list[a].value)
            self.label.setText(AQA_list[1].value)

    def retranslateUi(self, AnswerWindow):
        self.label.setWordWrap(True)
        _translate = QtCore.QCoreApplication.translate
        i = []
        AQA_list = []
        self.file['analysis']['analysis'] = str(self.ran)
        for b in self.Answers_sheet[f'A{self.ran}:F{self.ran}']:
            AQA_list = b
        AnswerWindow.setWindowTitle(_translate("AnswerWindow", "答题中"))
        self.t_answer = AQA_list[2].value
        a = random.randint(2, 5)
        i.append(a)
        self.radioButtonA.setText(_translate("AnswerWindow", AQA_list[a].value))
        while a in i:
            a = random.randint(2, 5)
        i.append(a)
        self.radioButtonB.setText(_translate("AnswerWindow", AQA_list[a].value))
        while a in i:
            a = random.randint(2, 5)
        i.append(a)
        self.radioButtonC.setText(_translate("AnswerWindow", AQA_list[a].value))
        while a in i:
            a = random.randint(2, 5)
        i.append(a)
        self.radioButtonD.setText(_translate("AnswerWindow", AQA_list[a].value))
        self.NextButton.setText(_translate("AnswerWindow", "确定"))
        self.label.setText(_translate("AnswerWindow", AQA_list[1].value))
