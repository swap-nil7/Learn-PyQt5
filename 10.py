"""
⠀⠀⠀⠀⠀⢀⣀⣀⣀
⠀⠀⠀⠰⡿⠿⠛⠛⠻⠿⣷
⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀
⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷
⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁
⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀
⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗
⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄
⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁
⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟
⠀⠀⠀⠀⠀⠉⠉⠉
"""
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QRadioButton, QPushButton, QVBoxLayout, QLabel)
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

## Radio button ##

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel('What do you like the most?')
        self.dog = QRadioButton('Dogs')
        self.cat = QRadioButton('Cats')
        self.btn = QPushButton('Select')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.dog)
        layout.addWidget(self.cat)
        layout.addWidget(self.btn)

        self.setLayout(layout)

        self.setWindowTitle('Lesson 10')

        self.btn.clicked.connect(lambda: self.btn_clk(self.dog.isChecked(), self.lbl))

        self.show()

    def btn_clk(self, chx, lbl):
        if chx:
            lbl.setText('I guess you like dogs.')
        else:
            lbl.setText("I guess you like cats.")


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
