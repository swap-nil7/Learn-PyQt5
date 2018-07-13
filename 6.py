import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5 import QtWidgets

## line edit ##

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QtWidgets.QLineEdit()
        self.b = QPushButton('Clear')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b)

        self.setLayout(v_box)

        self.setWindowTitle('Lesson 6')

        self.show()



app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
