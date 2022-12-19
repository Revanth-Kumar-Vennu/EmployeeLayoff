# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'company.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 429)
        MainWindow.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"background-color: rgb(85, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 210, 201, 31))
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 170, 0);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 210, 71, 33))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 330, 401, 31))
        self.pushButton.setStyleSheet("color: rgb(255, 170, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 30, 51, 33))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 90, 731, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 150, 811, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 191, 31))
        self.label_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 170, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.label_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 170, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 121, 31))
        self.label_5.setStyleSheet("color: rgb(255, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 280, 171, 21))
        self.label_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 170, 0);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 270, 241, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Company Details"))
        self.label.setText(_translate("MainWindow", "Country std Code:"))
        self.pushButton.setText(_translate("MainWindow", "Store Comapny Details in Data base"))
        self.label_3.setText(_translate("MainWindow", "Company  Name:"))
        self.label_4.setText(_translate("MainWindow", "Company Code:"))
        self.label_5.setText(_translate("MainWindow", "Country:"))
        self.label_2.setText(_translate("MainWindow", "Area std Code:"))

