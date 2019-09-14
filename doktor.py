import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import uic
from DB.doktorDB import doktorDB 

class DoktorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pencere = uic.loadUi(r"C:\Users\vektorel\Documents\GitHub\Python9DestktopProject\GUI\doktor.ui")
        self.pencere.btKaydet.clicked.connect(self.Calistir)
        self.pencere.show()

    def Calistir(self):
        veriTabani = doktorDB()
        ad = self.pencere.txtAdi.text()
        soyadi = self.pencere.txtSoyadi.text()
        unv = 1
        uzm = 1
        veriTabani.doktorEkle(ad,soyadi,unv,uzm)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DoktorUI()
    sys.exit(app.exec_())