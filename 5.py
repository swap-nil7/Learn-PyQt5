import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5 import QtWidgets

## class ##
## add action to click ##

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.l = QLabel('I have not been pushed')
        self.b = QPushButton('Push Me')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('Lesson 5')

        self.b.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        self.l.setText('I have been clicked.')


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
