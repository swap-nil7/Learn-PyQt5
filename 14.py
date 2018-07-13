import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, qApp)
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

## Menu Bar ##

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

        # Create Menu Bar
        bar = self.menuBar()

        # Create Root Menus
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        # Create Actions for menus
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        quit_action = QAction('Quit', self)
        quit_action.setShortcut('Ctrl+Q')

        find_action = QAction('Find...', self)

        replace_action = QAction('Replace...', self)
        
        # Add actions to Menu
        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(quit_action)
        find_menu = edit.addMenu("Find")
        find_menu.addAction(find_action)
        find_menu.addAction(replace_action)

        # Events
        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.selected)

        self.setWindowTitle("My Menus")
        self.resize(600, 400)

        self.show()
        
    def quit_trigger(self):
        qApp.quit()

    def selected(self, q):
        print(q.text() + ' selected')


app = QApplication(sys.argv)
a_window = Menu()
sys.exit(app.exec_())
