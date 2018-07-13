import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QCheckBox, QPushButton, QVBoxLayout, QLabel)
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

## check box ##

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel()
        self.chx = QCheckBox('Do you like dogs?')
        self.btn = QPushButton('Push Me!')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.chx)
        layout.addWidget(self.btn)

        self.setLayout(layout)

        self.setWindowTitle('Lesson 9')

        self.btn.clicked.connect(lambda: self.btn_clk(self.chx.isChecked(), self.lbl))

        self.show()

    def btn_clk(self, chx, lbl):
        if chx:
            lbl.setText('I guess you like dogs')
        else:
            lbl.setText("You don't like dogs, but why?")


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
