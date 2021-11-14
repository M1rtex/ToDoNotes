from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
import ui_main

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = ui_main.Ui_MainWindow()
        self.rand = 0
        self.ui.setupUi(self)