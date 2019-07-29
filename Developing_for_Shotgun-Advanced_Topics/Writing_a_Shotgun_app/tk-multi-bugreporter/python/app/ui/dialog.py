# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(431, 392)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.ticket_title = QtGui.QLineEdit(Dialog)
        self.ticket_title.setObjectName("ticket_title")
        self.horizontalLayout_2.addWidget(self.ticket_title)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.cc_layout = QtGui.QHBoxLayout()
        self.cc_layout.setContentsMargins(-1, 0, -1, -1)
        self.cc_layout.setObjectName("cc_layout")
        self.cc_label = QtGui.QLabel(Dialog)
        self.cc_label.setObjectName("cc_label")
        self.cc_layout.addWidget(self.cc_label)
        self.verticalLayout.addLayout(self.cc_layout)
        self.ticket_body = QtGui.QPlainTextEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ticket_body.sizePolicy().hasHeightForWidth())
        self.ticket_body.setSizePolicy(sizePolicy)
        self.ticket_body.setObjectName("ticket_body")
        self.verticalLayout.addWidget(self.ticket_body)
        self.lower_layout = QtGui.QHBoxLayout()
        self.lower_layout.setSpacing(5)
        self.lower_layout.setContentsMargins(-1, 0, -1, -1)
        self.lower_layout.setObjectName("lower_layout")
        self.screenshot = QtGui.QLabel(Dialog)
        self.screenshot.setMinimumSize(QtCore.QSize(50, 50))
        self.screenshot.setMaximumSize(QtCore.QSize(50, 50))
        self.screenshot.setStyleSheet("border: 1px solid grey")
        self.screenshot.setText("")
        self.screenshot.setAlignment(QtCore.Qt.AlignCenter)
        self.screenshot.setObjectName("screenshot")
        self.lower_layout.addWidget(self.screenshot)
        self.screen_grab = QtGui.QPushButton(Dialog)
        self.screen_grab.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.screen_grab.setObjectName("screen_grab")
        self.lower_layout.addWidget(self.screen_grab)
        self.verticalLayout.addLayout(self.lower_layout)
        self.buttons = QtGui.QDialogButtonBox(Dialog)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttons.setObjectName("buttons")
        self.verticalLayout.addWidget(self.buttons)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Report a bug!", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Subject:", None, QtGui.QApplication.UnicodeUTF8))
        self.cc_label.setText(QtGui.QApplication.translate("Dialog", "CC:", None, QtGui.QApplication.UnicodeUTF8))
        self.screen_grab.setText(QtGui.QApplication.translate("Dialog", "Take a screenshot!", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
