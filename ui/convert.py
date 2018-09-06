# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convert.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import os

import canmatrix.formats
import canmatrix.canmatrix as cm
import canmatrix.convert as can_convert

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(552, 391)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.FileInlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.FileInlineEdit.setGeometry(QtCore.QRect(190, 122, 113, 31))
        self.FileInlineEdit.setObjectName("FileInlineEdit")

        self.FileInputlabel = QtWidgets.QLabel(self.centralwidget)
        self.FileInputlabel.setGeometry(QtCore.QRect(100, 130, 81, 21))
        self.FileInputlabel.setTextFormat(QtCore.Qt.RichText)
        self.FileInputlabel.setScaledContents(True)
        self.FileInputlabel.setObjectName("FileInputlabel")

        self.OpenFileButton = QtWidgets.QToolButton(self.centralwidget)
        self.OpenFileButton.setGeometry(QtCore.QRect(310, 120, 61, 31))
        self.OpenFileButton.setObjectName("OpenFileButton")

        self.OpenFileButton.clicked.connect(self.OpenFileButton_Function)

        self.FileOutlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.FileOutlineEdit.setGeometry(QtCore.QRect(190, 172, 113, 31))
        self.FileOutlineEdit.setObjectName("FileOutlineEdit")

        self.ConvertButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConvertButton.setGeometry(QtCore.QRect(190, 230, 171, 41))

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.FileOutputlabel = QtWidgets.QLabel(self.centralwidget)
        self.FileOutputlabel.setGeometry(QtCore.QRect(100, 180, 81, 21))
        self.FileOutputlabel.setTextFormat(QtCore.Qt.RichText)
        self.FileOutputlabel.setScaledContents(True)
        self.FileOutputlabel.setObjectName("FileOutputlabel")

        self.WarningtextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.WarningtextEdit.setEnabled(False)
        self.WarningtextEdit.setGeometry(QtCore.QRect(120, 50, 321, 31))
        self.WarningtextEdit.setObjectName("WarningtextEdit")

        self.ChooseFileComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.ChooseFileComboBox.setGeometry(QtCore.QRect(310, 171, 61, 31))
        self.ChooseFileComboBox.setObjectName("ChooseFileComboBox")
        self.ChooseFileComboBox.addItem("")
        self.ChooseFileComboBox.addItem("")

        self.ConvertButton.setFont(font)
        self.ConvertButton.setObjectName("ConvertButton")
        self.ConvertButton.clicked.connect(self.ConvertButton_Function)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 552, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FileInputlabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">文件输入：</span></p></body></html>"))
        self.OpenFileButton.setText(_translate("MainWindow", "..."))
        self.ConvertButton.setText(_translate("MainWindow", "Convert"))
        self.FileOutputlabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">文件输出：</span></p></body></html>"))
        self.WarningtextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">warning: 只支持DBC文件和xls文件互转</span></p></body></html>"))
        self.ChooseFileComboBox.setItemText(0, _translate("MainWindow", ".xls"))
        self.ChooseFileComboBox.setItemText(1, _translate("MainWindow", ".dbc"))

    def OpenFileButton_Function(self):
        FileName, FileType = QFileDialog.getOpenFileName()
        self.FileInlineEdit.setText(FileName)
        (FilePath, tempfilename) = os.path.splitext(FileName)
        self.FileOutlineEdit.setText(FilePath)

    def ConvertButton_Function(self):
        inFile = self.FileInlineEdit.text()
        print(inFile)
        outFile = self.FileOutlineEdit.text()+self.ChooseFileComboBox.currentText()
        print(outFile)
        can_convert.convert(inFile, outFile, dbcImportEncoding='GBK', dbcExportEncoding='GBK')


