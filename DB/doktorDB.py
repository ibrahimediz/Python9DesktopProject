from DB.DB import DBTools
import os

class doktorDB(DBTools):
    def __init__(self):
        super(doktorDB,self).__init__(os.getcwd()+os.sep+r"DB\hastane.db")
        self.TABLO = "DOKTOR_BILGI"
    
    def doktorEkle(self,ad,soyad,unv,uzman):
        return self.ekleme(TABLO=self.TABLO,SUTUN=["DOK_ADI","DOK_SOYADI","DOK_UNVAN","DOK_UZ_ID"],
DEGER=["'"+ad+"'","'"+soyad+"'",unv,uzman])

    


    def SozlukListeGetir(self,param):
        return self.listeleme(TABLO="ST_SOZLUK",SUTUN=["ALAN_ID","ALAN_ADI"],SART="TABLO_ID = "+param)

    def doktorListeGetir(self,filtre="",param=""):
        sart = ""
        if filtre == "1" :
            sart = " DOK_ID = "+param
        elif filtre == "2":
            sart = " DOK_UZ_ID =" + param
        else:
            sart = " DOK_ID > 0 "
        return self.listeleme(TABLO=self.TABLO,SUTUN=["DOK_ID","DOK_ADI","DOK_SOYADI","DOK_UNVAN","DOK_UZ_ID"],SART=sart)