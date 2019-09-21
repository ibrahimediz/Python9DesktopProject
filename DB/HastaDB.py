from DB.DB import DBTools
import os


class HastaDBTool(DBTools):
    def __init__(self):
        super(HastaDBTool,self).__init__(os.getcwd()+os.sep+r"DB\hastane.db")
        self.Tablo = "HASTA_BILGI"


    def hastaListele(self,sart=""):
        return self.listeleme(TABLO=self.Tablo,SUTUN=[
            "HASTA_ID",
            "HASTA_TC",
            "HASTA_ADI",
            "HASTA_SOYADI",
            "HASTA_TEL"],SART=sart)

    def tirnakEkle(self,param = ""):
        return "'" + param + "'"

    def hastaEkle(self,
                HASTA_TC,
                HASTA_ADI,
                HASTA_SOYADI,
                HASTA_TEL):
        return  self.ekleme(TABLO=self.Tablo,SUTUN=[
            "HASTA_TC",
            "HASTA_ADI",
            "HASTA_SOYADI",
            "HASTA_TEL"],DEGER=[
                HASTA_TC,
                self.tirnakEkle(HASTA_ADI),
                self.tirnakEkle(HASTA_SOYADI),
                self.tirnakEkle(HASTA_TEL)
            ])
