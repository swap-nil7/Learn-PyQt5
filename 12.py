import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout)
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

## Save Text File ##

class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.save_button = QPushButton('Save')

        self.init_ui()

    def init_ui(self):

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save_text)

        self.setLayout(layout)

        self.setWindowTitle('Lesson 12')

        self.show()

    def save_text(self):
        with open('test.txt', 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)


app = QApplication(sys.argv)
a_window = Notepad()
sys.exit(app.exec_())
