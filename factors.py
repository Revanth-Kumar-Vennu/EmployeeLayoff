# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'factors.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 618)
        MainWindow.setStyleSheet("background-color: rgb(134, 146, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 440, 371, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 28, 130);\n"
"color: rgb(77, 61, 255);\n"
"background-color: rgb(123, 176, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(71, 35, 255);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(630, 120, 41, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 601, 31))
        self.label_4.setStyleSheet("color: rgb(255, 26, 137);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(720, 160, 41, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(720, 210, 41, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(610, 250, 41, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 691, 31))
        self.label_6.setStyleSheet("color: rgb(255, 19, 121);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 210, 691, 31))
        self.label_7.setStyleSheet("color: rgb(255, 25, 148);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 250, 571, 31))
        self.label_8.setStyleSheet("color: rgb(255, 29, 169);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(640, 80, 41, 33))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 80, 621, 31))
        self.label_14.setStyleSheet("color: rgb(255, 25, 144);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 471, 31))
        self.label_9.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(20, 12, 255);\n"
"color: rgb(255, 10, 75);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 300, 581, 31))
        self.label_10.setStyleSheet("color: rgb(255, 21, 146);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(620, 300, 41, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(630, 350, 41, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 350, 591, 31))
        self.label_11.setStyleSheet("color: rgb(255, 16, 132);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Company Factors"))
        self.pushButton.setText(_translate("MainWindow", "Store Factors in Data base"))
        self.label_4.setText(_translate("MainWindow", "Company Revenues increasing gradually from last 3 years?"))
        self.label_6.setText(_translate("MainWindow", "Company Customer Strength increasing gradually from last 3 years?"))
        self.label_7.setText(_translate("MainWindow", "Company Employee Strength increasing gradually from last 3 years?"))
        self.label_8.setText(_translate("MainWindow", "Company Assets  increasing gradually from last 3 years?"))
        self.label_14.setText(_translate("MainWindow", "Company Total profits increasing gradually from last 3 years?"))
        self.label_9.setText(_translate("MainWindow", "Give Input 1, if the factor exists; Otherwise 0"))
        self.label_10.setText(_translate("MainWindow", "Company Debts Decreasing gradually from last 3 years?"))
        self.label_11.setText(_translate("MainWindow", "Employee Salaries  increasing gradually from last 3 years?"))

