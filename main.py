from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
import ui_main
from os import walk
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('NotesViewer')
        self.ui.exit_btn.clicked.connect(sys.exit)
        files = []
        for (dirpath, dirnames, filenames) in walk('./notes'):
            files.extend(filenames)
            break

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = mywindow()
    window.show()
    sys.exit(app.exec())