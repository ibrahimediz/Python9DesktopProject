import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QListWidgetItem
from PyQt5 import uic
from DB.doktorDB import doktorDB
from doktor import DoktorUI
import os


class AnaMenu(QMainWindow):
    def __init__(self):
        super(AnaMenu,self).__init__()
        self.initUI()

    def initUI(self):
        self.win = uic.loadUi(os.getcwd()+os.sep+r"GUI\AnaEkran.ui")
        self.win.doktorislem.triggered.connect(self.doktorAc)
        self.win.txtTC.textChanged.connect(self.deneme)
        self.win.show()
    
    def doktorAc(self):
        self.doktor = DoktorUI()


    def deneme(self):
        metin = self.win.txtTC.text()
        self.win.lblID.setText(metin)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AnaMenu()
    sys.exit(app.exec_())