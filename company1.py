import sys
from company import *
from PyQt5 import QtWidgets, QtGui, QtCore

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
        countrycode = str(self.ui.lineEdit.text())
        cid = str(self.ui.lineEdit_3.text())
        cname = str(self.ui.lineEdit_4.text())
        ccode = str(self.ui.lineEdit.text())
        countryname = str(self.ui.lineEdit_6.text())	
        areacode = str(self.ui.lineEdit_2.text())
        cur.execute('INSERT INTO company VALUES(?,?,?,?,?)',(cid,cname,countrycode,countryname,areacode))
        con.commit()
        

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
