from DB.DB import DBTools

class doktorDB(DBTools):
    def __init__(self):
        super(doktorDB,self).__init__(r"C:\Users\vektorel\Documents\GitHub\Python9DestktopProject\DB\hastane.db")
        self.TABLO = "DOKTOR_BILGI"
    
    def doktorEkle(self,ad,soyad,unv,uzman):
        return self.ekleme(TABLO=self.TABLO,SUTUN=["DOK_ADI","DOK_SOYADI","DOK_UNVAN","DOK_UZ_ID"],
DEGER=["'"+ad+"'","'"+soyad+"'",unv,uzman])

    def unvanListele(self):
        return self.listeleme(TABLO="ST_SOZLUK",SUTUN=["ALAN_ID","ALAN_ADI"],SART="TABLO_ID = 1")

