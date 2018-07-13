import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout)
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

## Text Edit ##

class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clr_button = QPushButton('Clear')

        self.init_ui()

    def init_ui(self):

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.clr_button)
        self.clr_button.clicked.connect(self.clear_text)

        self.setLayout(layout)

        self.setWindowTitle('Lesson 11')

        self.show()

    def clear_text(self):
        self.text.clear()


app = QApplication(sys.argv)
a_window = Notepad()
sys.exit(app.exec_())
