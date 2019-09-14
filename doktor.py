import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import uic

class DoktorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pencere = uic.loadUi("doktor.ui")
        self.pencere.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DoktorUI()
    sys.exit(app.exec_())