"""
Roses are red, Life is a fare
Give me the shirt, I don't really care
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


def window():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Lesson 1")
    w.show()
    sys.exit(app.exec_())

window()
