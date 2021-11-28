# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledzCnTww.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 800, 600))
        self.frame.setMinimumSize(QSize(800, 600))
        self.frame.setMaximumSize(QSize(800, 600))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.text_edit_frame = QFrame(self.frame)
        self.text_edit_frame.setObjectName(u"text_edit_frame")
        self.text_edit_frame.setFrameShape(QFrame.StyledPanel)
        self.text_edit_frame.setFrameShadow(QFrame.Raised)
        self.notice_text_edit = QTextEdit(self.text_edit_frame)
        self.notice_text_edit.setObjectName(u"notice_text_edit")
        self.notice_text_edit.setGeometry(QRect(5, 5, 451, 575))

        self.horizontalLayout.addWidget(self.text_edit_frame)

        self.edit_frame = QFrame(self.frame)
        self.edit_frame.setObjectName(u"edit_frame")
        self.edit_frame.setMaximumSize(QSize(300, 16777215))
        self.edit_frame.setFrameShape(QFrame.StyledPanel)
        self.edit_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.edit_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.edit_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.notice_frame = QFrame(self.frame_3)
        self.notice_frame.setObjectName(u"notice_frame")
        self.notice_frame.setMaximumSize(QSize(300, 250))
        self.notice_frame.setFrameShape(QFrame.StyledPanel)
        self.notice_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.notice_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.notice_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 250))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.file_list_view = QListWidget(self.frame_2)
        self.file_list_view.setObjectName(u"file_list_view")
        self.file_list_view.setMaximumSize(QSize(16777215, 180))

        self.verticalLayout_3.addWidget(self.file_list_view)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.create_note_btn = QPushButton(self.frame_4)
        self.create_note_btn.setObjectName(u"create_note_btn")

        self.horizontalLayout_2.addWidget(self.create_note_btn)

        self.save_note_btn = QPushButton(self.frame_4)
        self.save_note_btn.setObjectName(u"save_note_btn")

        self.horizontalLayout_2.addWidget(self.save_note_btn)

        self.delete_note_btn = QPushButton(self.frame_4)
        self.delete_note_btn.setObjectName(u"delete_note_btn")

        self.horizontalLayout_2.addWidget(self.delete_note_btn)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.notice_frame)

        self.teg_frame = QFrame(self.frame_3)
        self.teg_frame.setObjectName(u"teg_frame")
        self.teg_frame.setFrameShape(QFrame.StyledPanel)
        self.teg_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.teg_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.teg_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 250))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_5.addWidget(self.label)

        self.teg_list_view = QListWidget(self.frame_5)
        self.teg_list_view.setObjectName(u"teg_list_view")
        self.teg_list_view.setMaximumSize(QSize(16777215, 180))

        self.verticalLayout_5.addWidget(self.teg_list_view)

        self.teg_actions_frame = QFrame(self.frame_5)
        self.teg_actions_frame.setObjectName(u"teg_actions_frame")
        self.teg_actions_frame.setMaximumSize(QSize(16777215, 40))
        self.teg_actions_frame.setFrameShape(QFrame.StyledPanel)
        self.teg_actions_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.teg_actions_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.add_teg_btn = QPushButton(self.teg_actions_frame)
        self.add_teg_btn.setObjectName(u"add_teg_btn")

        self.horizontalLayout_3.addWidget(self.add_teg_btn)

        self.save_teg_btn = QPushButton(self.teg_actions_frame)
        self.save_teg_btn.setObjectName(u"save_teg_btn")

        self.horizontalLayout_3.addWidget(self.save_teg_btn)

        self.delete_teg_btn = QPushButton(self.teg_actions_frame)
        self.delete_teg_btn.setObjectName(u"delete_teg_btn")

        self.horizontalLayout_3.addWidget(self.delete_teg_btn)


        self.verticalLayout_5.addWidget(self.teg_actions_frame)


        self.verticalLayout_6.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.teg_frame)


        self.verticalLayout.addWidget(self.frame_3)

        self.exit_btn = QPushButton(self.edit_frame)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(200, 35))
        self.exit_btn.setMaximumSize(QSize(300, 300))

        self.verticalLayout.addWidget(self.exit_btn)


        self.horizontalLayout.addWidget(self.edit_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Notes</p></body></html>", None))
        self.create_note_btn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.save_note_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.delete_note_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Tegs</p></body></html>", None))
        self.add_teg_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.save_teg_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.delete_teg_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Close", None))
    # retranslateUi

