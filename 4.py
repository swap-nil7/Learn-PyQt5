import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5 import QtWidgets

## Box Layout ##
def window():
    app = QApplication(sys.argv)
    w = QWidget()
    l = QLabel('Look at me')
    b = QPushButton('Push Me')
    
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(l)
    h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)
    v_box.addLayout(h_box)

    w.setLayout(v_box)

    w.setWindowTitle("Lesson 4")
    w.show()
    sys.exit(app.exec_())

window()
