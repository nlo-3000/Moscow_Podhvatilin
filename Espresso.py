import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.count = 0
        self.name_input = QLineEdit(self)
        self.name_input.move(50, 350)

    def run(self):
        try:
            arg = int(self.name_input.text())
            if arg in [1, 2, 3, 4]:
                self.count = arg

        except:
            pass
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM main""").fetchmany(self.count)
        for i in result:
            self.txt1.setText("")
            self.txt2.setText("")
            self.txt3.setText("")
            self.txt4.setText("")

            if i[0] == 1:
                self.txt1.setText('{}    {}  {}  {}  {}   {}       {}'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
            elif i[0] == 2:
                self.txt2.setText('{}    {}  {}  {}  {}   {}       {}'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
            elif i[0] == 3:
                self.txt3.setText('{}    {}  {}  {}  {}   {}       {}'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
            elif i[0] == 4:
                self.txt4.setText('{}    {}  {}  {}  {}   {}       {}'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
