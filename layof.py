# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layof.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 377)
        MainWindow.setStyleSheet("background-color: rgb(38, 19, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 210, 271, 41))
        self.pushButton.setStyleSheet("color: rgb(165, 248, 255);\n"
"color: rgb(255, 170, 0);\n"
"background-color: rgb(137, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 30, 271, 41))
        self.pushButton_5.setStyleSheet("color: rgb(255, 170, 0);\n"
"background-color: rgb(146, 254, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 150, 271, 41))
        self.pushButton_3.setStyleSheet("color: rgb(255, 170, 0);\n"
"background-color: rgb(144, 255, 252);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 90, 271, 41))
        self.pushButton_4.setStyleSheet("color: rgb(255, 170, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(133, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(270, 270, 271, 41))
        self.pushButton_9.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(103, 235, 255);\n"
"border-color: rgb(61, 252, 255);\n"
"border-color: rgb(85, 255, 255);\n"
"color: rgb(255, 170, 0);")
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Layoff Analysis"))
        self.pushButton.setText(_translate("MainWindow", "Weights"))
        self.pushButton_5.setText(_translate("MainWindow", "Company Details"))
        self.pushButton_3.setText(_translate("MainWindow", "Plot the sigmoid"))
        self.pushButton_4.setText(_translate("MainWindow", "Factors"))
        self.pushButton_9.setText(_translate("MainWindow", "Prediction"))

