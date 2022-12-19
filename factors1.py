import sys
from factors import *
from PyQt5 import QtWidgets, QtGui, QtCore

#import pymysql
#con = pymysql.connect(host='localhost', port=3306, user='team1', passwd='test623', db='layoff1')

import sqlite3
con = sqlite3.connect('layoff1')


class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues) 

   

  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        fact1 = str(self.ui.lineEdit_14.text())
        fact2 = str(self.ui.lineEdit_4.text())
        fact3 = str(self.ui.lineEdit_5.text())
        fact4 = str(self.ui.lineEdit_6.text())
        fact5 = str(self.ui.lineEdit_7.text())	
        fact6 = str(self.ui.lineEdit_8.text())
        fact7 = str(self.ui.lineEdit_9.text())
        cur.execute('INSERT INTO factors VALUES(?,?,?,?,?,?,?)',(fact1,fact2,fact3,fact4,fact5,fact6,fact7))
        con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


