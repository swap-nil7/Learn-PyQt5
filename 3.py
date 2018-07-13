import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

## button ##
def window():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Lesson 3")
    w.setGeometry(100, 100, 300, 200)
    l = QLabel(w)
    l.setText('Hello World')
    b = QPushButton(w)
    b.setText('Push Me')
    l.move(110, 100)
    b.move(100, 50)
    w.show()
    sys.exit(app.exec_())

window()
