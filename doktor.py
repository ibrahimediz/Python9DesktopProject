import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from PyQt5 import uic
from DB.doktorDB import doktorDB 

class DoktorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pencere = uic.loadUi(r"C:\Users\vektorel\Documents\GitHub\Python9DestktopProject\GUI\doktor.ui")
        self.pencere.btKaydet.clicked.connect(self.Calistir)
        self.pencere.btTemizle.clicked.connect(self.unvanDoldur)
        self.pencere.show()

    def Calistir(self):
        veriTabani = doktorDB()
        ad = self.pencere.txtAdi.text()
        soyadi = self.pencere.txtSoyadi.text()
        unv = 1
        uzm = 1
        if veriTabani.doktorEkle(ad,soyadi,unv,uzm):
            QMessageBox.information(self,"Bilgi","Kayıt Başarılı",QMessageBox.Ok,QMessageBox.Ok)
            sonuc =  QMessageBox.question(self,"Soru","Yağmur Yağacak mı?",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            if sonuc == QMessageBox.Yes:
                QMessageBox.information(self,"Bilgi","bencede",QMessageBox.Ok,QMessageBox.Ok)
    def unvanDoldur(self):
        veriTabani = doktorDB()
        liste = veriTabani.unvanListele()
        self.pencere.cmbUnvan.addItem("Seçiniz","-1")
        for alanid,alanad in liste:
            self.pencere.cmbUnvan.addItem(alanad,alanid)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DoktorUI()
    sys.exit(app.exec_())