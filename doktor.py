import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QListWidgetItem
from PyQt5 import uic
from DB.doktorDB import doktorDB 

class DoktorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pencere = uic.loadUi(r"C:\Users\vektorel\Documents\GitHub\Python9DesktopProject\GUI\doktor.ui")
        self.pencere.btKaydet.clicked.connect(self.Calistir)
        self.pencere.cmbUzmanlik.currentIndexChanged.connect(self.cmbDegisti)
        self.AlanDoldur()
        self.unvanDoldur()
        self.tabloDoldur()
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

    def tabloDoldur(self):
        veriTabani = doktorDB()
        liste = veriTabani.doktorListeGetir()
        for adi,soyadi,id in liste:
            item = QListWidgetItem("{}-{} {}".format(id,adi,soyadi))
            self.pencere.doktorList.addItem(item)
    
    def cmbDegisti(self):
        print(self.pencere.cmbUzmanlik.currentIndex())

    def unvanDoldur(self):
        veriTabani = doktorDB()
        liste = veriTabani.SozlukListeGetir("1")
        self.pencere.cmbUnvan.addItem("Seçiniz","-1")
        for alanid,alanad in liste:
            self.pencere.cmbUnvan.addItem(alanad,alanid)

    def AlanDoldur(self):
        veriTabani = doktorDB()
        liste = veriTabani.SozlukListeGetir("2")
        self.pencere.cmbUzmanlik.addItem("Seçiniz","-1")
        for alanid,alanad in liste:
            self.pencere.cmbUzmanlik.addItem(alanad,alanid)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DoktorUI()
    sys.exit(app.exec_())