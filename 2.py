import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

## resize, label
def window():
    app = QApplication(sys.argv)
    w = QWidget()
    li = QLabel(w)
    li.setText('Hello World')
    w.setWindowTitle("Lesson 2")
    w.setGeometry(100, 100, 300, 200)
    li.move(100, 20)
    w.show()
    sys.exit(app.exec_())

window()