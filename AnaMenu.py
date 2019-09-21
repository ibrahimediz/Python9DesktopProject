import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QTableWidgetItem,QMessageBox
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
        self.win.tblHasta.doubleClicked.connect(self.Secim)
        self.win.btYeni.clicked.connect(self.doldur)
        # self.win.doktorislem.triggered.connect(self.doktorAc)
        # self.win.txtTC.textChanged.connect(self.deneme)
        self.TabloDoldur()
        self.win.show()
    
    def Secim(self):
        secim = self.win.tblHasta.item(self.win.tblHasta.currentRow(),0).text()
        gelenHasta = self.db.hastaListele(secim)[0]
        self.doldur(gelenHasta)
    
    def doldur(self,gelenHasta=[]):
        if gelenHasta:
            self.win.lblID.setText(str(gelenHasta[0]))
            self.win.txtTC.setText(str(gelenHasta[1]))
            self.win.txtAdi.setText(str(gelenHasta[2]))
            self.win.txtSoyadi.setText(str(gelenHasta[3]))
            self.win.txtTel.setText(str(gelenHasta[4]))
        else:
            self.win.lblID.setText("")
            self.win.txtTC.setText("")
            self.win.txtAdi.setText("")
            self.win.txtSoyadi.setText("")
            self.win.txtTel.setText("")

    def doktorAc(self):
        self.doktor = DoktorUI()

    def TabloDoldur(self):
        self.win.tblHasta.clear()
        self.win.tblHasta.setRowCount(10)
        self.win.tblHasta.setColumnCount(5)
        liste = self.db.hastaListele()
        for i in range(0,len(liste)):
            for j in range(0,len(liste[0])):
                self.win.tblHasta.setItem(i,j,QTableWidgetItem(str(liste[i][j])))



    def Kaydet(self):
        HASTA_ID = self.win.lblID.text()
        HASTA_TC = self.win.txtTC.text() 
        HASTA_ADI = self.win.txtAdi.text()
        HASTA_SOYADI = self.win.txtSoyadi.text()
        HASTA_TEL = self.win.txtTel.text()

        elCavap = QMessageBox.question(self,"Soru","Kaydetmek İstiyor musun?",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.Cancel)

        if elCavap == QMessageBox.Yes:
            sonuc = self.db.hastaEkleGuncelle(HASTA_TC,HASTA_ADI,HASTA_SOYADI,HASTA_TEL,HASTA_ID)
            if sonuc:
                QMessageBox.information(self,"Bilgi","Kaydedildi",QMessageBox.Ok,QMessageBox.Ok)
                self.TabloDoldur()
        elif elCavap == QMessageBox.No:
            self.doldur()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AnaMenu()
    sys.exit(app.exec_())