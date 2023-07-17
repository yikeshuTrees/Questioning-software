from PyQt5 import QtWidgets
import sys, MainWindows

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = MainWindows.Ui_MainWindows()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
#pyinstaller -F -i Trees.ico main.py
