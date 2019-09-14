import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import uic

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = uic.loadUi(r"C:\Users\vektorel\Documents\GitHub\Python9DestktopProject\firstGUI.ui")
        self.pencere.bt1.clicked.connect(self.tiklandi)
        self.pencere.show()


    def tiklandi(self):
        print(self.pencere.txt1.text())
        self.pencere.txt1.setText("Merhaba")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
