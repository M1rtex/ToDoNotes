from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QInputDialog

import ui_main
import json
from os import walk
import sys
from os import remove

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('NotesViewer')
        self.ui.exit_btn.clicked.connect(sys.exit)
        files = []
        self.set_files()
        self.ui.file_list_view.itemClicked.connect(self.open_note)
        self.ui.create_note_btn.clicked.connect(self.add_note)
        self.ui.delete_note_btn.clicked.connect(self.delete_note)


    def set_files(self):
        files = []
        self.ui.file_list_view.clear()
        for (dirpath, dirnames, filenames) in walk('./notes'):
            files.extend(filenames)
            break
        for f in files:
            with open(f'./notes/{f}', 'r') as read_file:
                read_data = json.load(read_file)
                self.ui.file_list_view.addItem(read_data['name'])

    def open_note(self):
        self.ui.teg_list_view.clear()
        self.ui.notice_text_edit.setText('')
        item = self.ui.file_list_view.currentItem().text()
        with open(f'./notes/{item}.json', 'r') as opened_file:
            opened_data = json.load(opened_file)
            self.ui.notice_text_edit.setText(opened_data['text'])
            for teg in opened_data['tegs']:
                self.ui.teg_list_view.addItem(teg)

    def delete_note(self):
        item = self.ui.file_list_view.currentItem().text()
        remove(path=f'./notes/{item}.json')
        self.set_files()

    def save_note(self):
        pass

    def add_note(self):
        note_name, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter note name:')
        with open(f'./notes/{note_name}.json', 'w+') as new_file:
            note_content = {}
            note_content['name'] = note_name
            note_content['text'] = ''
            note_content['tegs'] = []
            json.dump(note_content, new_file)
        self.set_files()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
