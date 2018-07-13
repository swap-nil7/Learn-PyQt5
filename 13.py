import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog)
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

## Save and Open Prompt ##

class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clr_button = QPushButton('Clear')
        self.save_button = QPushButton('Save')
        self.open_button = QPushButton('Open')
        self.init_ui()

    def init_ui(self):

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clr_button)
        h_layout.addWidget(self.save_button)
        h_layout.addWidget(self.open_button)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.save_button.clicked.connect(self.save_text)
        self.clr_button.clicked.connect(self.clear_text)
        self.open_button.clicked.connect(self.open_text)

        self.setLayout(v_layout)

        self.setWindowTitle('Lesson 13')

        self.show()

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

    def clear_text(self):
        self.text.clear()


app = QApplication(sys.argv)
a_window = Notepad()
sys.exit(app.exec_())
