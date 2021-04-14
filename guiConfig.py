import sys
from PyQt5.QtWidgets import QApplication
from guiCode import MainGui

class Start:

    def __init__(self):
        self.__app = QApplication(sys.argv)
        self.gui = MainGui()
        self.__app.exec_()