# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Show(object):
    def setupUi(self, Show):
        Show.setObjectName("Show")
        Show.resize(260, 353)
        self.result = QtWidgets.QTextBrowser(Show)
        self.result.setGeometry(QtCore.QRect(40, 30, 181, 261))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.result.setFont(font)
        self.result.setReadOnly(True)
        self.result.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.result.setObjectName("result")
        self.done = QtWidgets.QPushButton(Show)
        self.done.setGeometry(QtCore.QRect(70, 310, 115, 32))
        self.done.setObjectName("done")

        self.retranslateUi(Show)
        self.done.clicked['bool'].connect(Show.close)
        QtCore.QMetaObject.connectSlotsByName(Show)

    def retranslateUi(self, Show):
        _translate = QtCore.QCoreApplication.translate
        Show.setWindowTitle(_translate("Show", "Log"))
        self.done.setText(_translate("Show", "Done"))
