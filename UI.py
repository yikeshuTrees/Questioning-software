from PyQt5.QtWidgets import QDialog
import AnswerWindow, Setting, MainWindows,Analysis,End,e_text,q_analysis
from PyQt5.QtCore import Qt

def SettingW():
    app = QDialog()
    ui = Setting.Ui_Setting()
    ui.setupUi(app)
    app.setWindowModality(Qt.ApplicationModal)
    app.show()
    app.exec_()


def MainWindowsW():
    app = QDialog()
    ui = MainWindows.Ui_MainWindows()
    ui.setupUi(app)
    app.setWindowModality(Qt.ApplicationModal)
    app.show()
    app.exec_()


def AnswerWindowW():
    app = QDialog()
    ui = AnswerWindow.Ui_AnswerWindow()
    ui.setupUi(app)
    app.setWindowModality(Qt.ApplicationModal)
    app.show()
    app.exec_()

def AnalysisW():
    app = QDialog()
    ui = Analysis.Ui_Analysis()
    ui.setupUi(app)
    app.setWindowModality(Qt.ApplicationModal)
    app.show()
    app.exec_()

def EndW():
    app = QDialog()
    ui = End.Ui_End()
    ui.setupUi(app)
    app.setWindowModality(Qt.ApplicationModal)
    app.show()
    app.exec_()
def e_textW(text):
    app = QDialog()
    ui = e_text.Ui_e_text(text = text)
    ui.setupUi(app)
    app.setWindowModality(Qt.ApplicationModal)
    app.show()
    app.exec_()
def q_analysisW():
    app = QDialog()
    ui = q_analysis.Ui_q_analysis()
    ui.setupUi(app)
    app.setWindowModality(Qt.ApplicationModal)
    app.show()
    app.exec_()
'''class UI():
    def SettingW(self):
        app = QDialog()
        ui = Setting.Ui_Setting()
        ui.setupUi(app)
        app.show()
        app.exec_()
    def MainWindowW(self):
        app = QDialog()
        ui = MainWindow.Ui_MainWindow()
        ui.setupUi(app)
        app.show()
        app.exec_()
    def AnswerWindowW(self):
        app = QDialog()
        ui = AnswerWindow.Ui_AnswerWindow()
        ui.setupUi(app)
        app.show()
        app.exec_()'''