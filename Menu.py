import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from Game import *
flag_of_start = False
flag_of_starting_display = False
flag_of_game1 = False
flag_of_game2 = False
flag_of_game3 = False


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('menu.ui', self)
        self.pushButton.clicked.connect(self.memory)
        self.pushButton_2.clicked.connect(self.memory)
        self.pushButton_3.clicked.connect(self.memory)
        self.pushButton_4.clicked.connect(self.memory)
        self.pushButton_5.clicked.connect(self.memory)
        self.label.setVisible(False)

    def memory(self):
        global flag_of_start
        global flag_of_game1
        global flag_of_game2
        global flag_of_game3
        global flag_of_starting_display
        if self.sender() == self.pushButton:
            flag_of_starting_display = True
            flag_of_game1 = True
            self.setVisible(False)
            main()
            self.setVisible(True)
        if self.sender() == self.pushButton_2:
            flag_of_starting_display = True
            flag_of_game2 = True
            self.setVisible(False)
            main()
            self.setVisible(True)
        if self.sender() == self.pushButton_3:
            flag_of_starting_display = True
            flag_of_game3 = True
            self.setVisible(False)
            main()
            self.setVisible(True)
        if self.sender() == self.pushButton_4:
            sys.exit(app.exec())
        if self.sender() == self.pushButton_5:
            self.label.setVisible(True)


if __name__ != '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
