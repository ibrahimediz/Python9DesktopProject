import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QListWidgetItem
from PyQt5 import uic
from DB.doktorDB import doktorDB
import os

class DoktorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pencere = uic.loadUi(os.getcwd()+os.sep+r"GUI\doktor.ui")
        self.pencere.btKaydet.clicked.connect(self.Calistir)
        self.pencere.cmbUzmanlik.currentIndexChanged.connect(self.cmbDegisti)
        self.pencere.btTemizle.clicked.connect(self.doldurma)
        self.pencere.doktorList.doubleClicked.connect(self.DoktorSecim)
        self.veriTabani = doktorDB()
        self.AlanDoldur()
        self.unvanDoldur()
        self.tabloDoldur()
        self.pencere.show()

    def Calistir(self):
        ad = self.pencere.txtAdi.text()
        soyadi = self.pencere.txtSoyadi.text()
        unv = 1
        uzm = 1
        if self.veriTabani.doktorEkle(ad,soyadi,unv,uzm):
            QMessageBox.information(self,"Bilgi","Kayıt Başarılı",QMessageBox.Ok,QMessageBox.Ok)
            sonuc =  QMessageBox.question(self,"Soru","Yağmur Yağacak mı?",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            if sonuc == QMessageBox.Yes:
                QMessageBox.information(self,"Bilgi","bencede",QMessageBox.Ok,QMessageBox.Ok)

    def DoktorSecim(self):
        metin  = self.pencere.doktorList.currentItem().text().split("-")
        gelen = self.veriTabani.doktorListeGetir("1",metin[0])[0]
        print(gelen)
        self.doldurma(list(gelen))
        

    def tabloDoldur(self):
        liste = self.veriTabani.doktorListeGetir()
        for id,adi,soyadi,unv,uzm in liste:
            item = QListWidgetItem("{}-{} {}".format(id,adi,soyadi))
            self.pencere.doktorList.addItem(item)
    
    def cmbDegisti(self):
        print(self.pencere.cmbUzmanlik.currentIndex())

    def unvanDoldur(self):
        liste = self.veriTabani.SozlukListeGetir("1")
        self.pencere.cmbUnvan.addItem("Seçiniz","-1")
        for alanid,alanad in liste:
            self.pencere.cmbUnvan.addItem(alanad,alanid)

    def AlanDoldur(self):
        liste = self.veriTabani.SozlukListeGetir("2")
        self.pencere.cmbUzmanlik.addItem("Seçiniz","-1")
        for alanid,alanad in liste:
            self.pencere.cmbUzmanlik.addItem(alanad,alanid)
    
    def doldurma(self,gelen=[]):
        if not gelen:
            self.pencere.txtAdi.setText("")
            self.pencere.txtSoyadi.setText("")
            self.pencere.cmbUnvan.setCurrentIndex(0)
            self.pencere.cmbUnvan.setCurrentIndex(0)
            self.pencere.lblDokID.setText("")
        else:
            self.pencere.txtAdi.setText(gelen[1])
            self.pencere.txtSoyadi.setText(gelen[2])
            self.pencere.cmbUnvan.setCurrentIndex(int(gelen[3]))
            self.pencere.cmbUnvan.setCurrentIndex(int(gelen[4]))
            self.pencere.lblDokID.setText(str(gelen[0]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DoktorUI()
    sys.exit(app.exec_())