import sys
import os
from layof import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_3.clicked.connect(self.plt1)
     self.ui.pushButton_4.clicked.connect(self.factrs)
     self.ui.pushButton_5.clicked.connect(self.cdetails)
     self.ui.pushButton.clicked.connect(self.wts)
     self.ui.pushButton_9.clicked.connect(self.pred1)
       

  def factrs(self):
    os.system("python factors1.py")

  def wts(self):
    os.system("python nn2.py")

  def edetails(self):
    os.system("python employee1.py")

  def cdetails(self):
    os.system("python company1.py")
	
  def plt1(self):
    os.system("python sgmd1.py")

  def pred1(self):
    os.system("python nn3.py")


if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
