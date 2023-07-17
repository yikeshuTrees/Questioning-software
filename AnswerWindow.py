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
        self.Answers_sheet = self.Answers_book['Sheet1']  #获取sheet页
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
        AnswerWindow.setObjectName("AnswerWindow")  #设置窗口对象的名字
        AnswerWindow.resize(400, 300)  #设置窗口大小
        self.window = AnswerWindow  #保存窗口对象为self.window
        self.verticalLayoutWidget = QtWidgets.QWidget(AnswerWindow)  #创建widget对象
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 100, 361, 163))  #设置widget的位置和大小
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")  #设置widget对象的名字
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)  #创建垂直布局
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)  #设置布局的边距
        self.verticalLayout.setObjectName("verticalLayout")  #设置布局对象的名字
        self.radioButtonA = QtWidgets.QRadioButton(self.verticalLayoutWidget)  #创建单选按钮A
        self.radioButtonA.setObjectName("radioButtonA")  #设置按钮对象的名字
        self.verticalLayout.addWidget(self.radioButtonA)  #将按钮添加到布局中
        self.radioButtonB = QtWidgets.QRadioButton(self.verticalLayoutWidget)  #创建单选按钮B
        self.radioButtonB.setObjectName("radioButtonB")  #设置按钮对象的名字
        self.verticalLayout.addWidget(self.radioButtonB)  #将按钮添加到布局中
        self.radioButtonC = QtWidgets.QRadioButton(self.verticalLayoutWidget)  #创建单选按钮C
        self.radioButtonC.setObjectName("radioButtonC")  #设置按钮对象的名字
        self.verticalLayout.addWidget(self.radioButtonC)  #将按钮添加到布局中
        self.radioButtonD = QtWidgets.QRadioButton(self.verticalLayoutWidget)  #创建单选按钮D
        self.radioButtonD.setObjectName("radioButtonD")  #设置按钮对象的名字
        self.verticalLayout.addWidget(self.radioButtonD)  #将按钮添加到布局中
        self.NextButton = QtWidgets.QPushButton(AnswerWindow)  #创建按钮
        self.NextButton.setGeometry(QtCore.QRect(300, 262, 75, 31))  #设置按钮的位置和大小
        self.NextButton.setObjectName("NextButton")  #设置按钮对象的名字
        self.label = QtWidgets.QLabel(AnswerWindow)  #创建标签
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 81))  #设置标签的位置和大小
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)  #设置标签的对齐方式
        self.label.setWordWrap(True)  #设置标签的换行方式
        self.label.setObjectName("label")  #设置标签对象的名字

        self.retranslateUi(AnswerWindow)  #调用翻译方法
        QtCore.QMetaObject.connectSlotsByName(AnswerWindow)  #连接槽函数和槽

        # 当点击“下一步”按钮时，调用get_choose_1方法
        self.NextButton.clicked.connect(self.get_choose_1)
        # 当点击“下一步”按钮时，调用check_condition方法
        self.NextButton.clicked.connect(self.check_condition)

    def get_choose_1(self):
        # 获取所选答案并进行判断
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
            print('You are error.')
        elif answer == self.t_answer:
            self.right += 1
            self.file['analysis']['analysis'] = str(self.ran)
            self.file['analysis']['judge'] = '答对了\n'
            self.file['answers']['right'] = str(self.right)
            self.t_question.append(self.ran)
            self.t_choose.append(answer)
            print(self.t_question,self.t_choose)
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
        self.i += 1
        if (self.file['setting']['choose1'] == '做题过程有解析（做一题出一题的解析）')\
                or (self.file['setting']['choose1'] == '正确的题无需解析（错误的题有解析）'\
                and self.file['analysis']['judge'] == '答错了\n'):
            UI.AnalysisW()
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
                self.ran = random.randint(2, rows.row)
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
