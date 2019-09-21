import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QTableWidgetItem
from PyQt5 import uic
from DB.HastaDB import HastaDBTool
from doktor import DoktorUI
import os


class AnaMenu(QMainWindow):
    def __init__(self):
        super(AnaMenu,self).__init__()
        self.initUI()

    def initUI(self):
        self.win = uic.loadUi(os.getcwd()+os.sep+r"GUI\AnaEkran.ui")
        self.db = HastaDBTool()
        self.win.btKaydet.clicked.connect(self.Kaydet)
        # self.win.doktorislem.triggered.connect(self.doktorAc)
        # self.win.txtTC.textChanged.connect(self.deneme)
        self.TabloDoldur()
        self.win.show()
    
    def doktorAc(self):
        self.doktor = DoktorUI()

    def TabloDoldur(self):
        self.win.tblHasta.setRowCount(10)
        self.win.tblHasta.setColumnCount(5)
        deneme =  QTableWidgetItem("Deneme")
        self.win.tblHasta.setItem(0,0,deneme)



    def Kaydet(self):
        HASTA_ID = self.win.lblID.text()
        HASTA_TC = self.win.txtTC.text() 
        HASTA_ADI = self.win.txtAdi.text()
        HASTA_SOYADI = self.win.txtSoyadi.text()
        HASTA_TEL = self.win.txtTel.text()

        sonuc = self.db.hastaEkle(HASTA_TC,HASTA_ADI,HASTA_SOYADI,HASTA_TEL)
        print(sonuc)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AnaMenu()
    sys.exit(app.exec_())