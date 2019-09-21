import sqlite3 as sql

class DBTools():
    def __init__(self,adres=""):
        self.adres = adres
        

    def dbBaglan(self):
        self.db = sql.connect(self.adres)
        self.cur = self.db.cursor()
    
    def listeleme(self,**kwargs):
        try:
            self.dbBaglan()
            sutunlar = ""
            degerler = ""
            sart = ""
            for key,value in kwargs.items():
                if key == "TABLO":
                    tablo = value
                elif key == "SUTUN":
                    for item in value:
                        sutunlar += item + ","
                    sutunlar = sutunlar.rstrip(",")
                elif key == "SART":
                    sart = value
            if not sart:
                sart = "1 = 1"
            sorgu = "SELECT {} FROM {} WHERE {}".format(sutunlar,tablo,sart)
            print(sorgu)
            self.cur.execute(sorgu)
            return  self.cur.fetchall()
        except:
            return None
        finally:
            self.db.close()

    def ekleme(self,**kwargs):
        try:
            self.dbBaglan()
            sutunlar = ""
            degerler = ""
            for key,value in kwargs.items():
                if key == "TABLO":
                    tablo = value
                elif key == "SUTUN":
                    for item in value:
                        sutunlar += item + ","
                    sutunlar = sutunlar.rstrip(",")
                elif key == "DEGER":
                    for item in value:
                        degerler += str(item) + ","
                    degerler = degerler.rstrip(",")
            sorgu = "INSERT INTO {} ({}) values ({})".format(tablo,sutunlar,degerler)
            self.dbBaglan()
            print(sorgu)
            self.cur.execute(sorgu)
            self.db.commit()
            return True
        except Exception:
            return False
        finally:
            self.db.close()

    def guncelle(self,**kwargs):
        try:
            self.dbBaglan()
            sutunlar = []
            degerler = []
            sart = ""
            for key,value in kwargs.items():
                if key == "TABLO":
                    tablo = value
                elif key == "SUTUN":
                    sutunlar = value
                elif key == "DEGER":
                    degerler = value
                elif key == "SART":
                    sart = value
                
            guncel = ""
            for i in range(0,len(sutunlar)):
                guncel += sutunlar[i] + " = " + str(degerler[i]) + ","
            guncel = guncel.rstrip(",")

                
            sorgu = "UPDATE {} SET {} WHERE {}".format(tablo,guncel,sart)
            
            self.cur.execute(sorgu)
            self.db.commit()
            return True
        except Exception as hata:
            print(hata)
            return False
        finally:
            self.db.close()
    
    def silme(self,**kwargs):
        try:
            self.dbBaglan()
            sutunlar = []
            degerler = []
            sart = ""
            for key,value in kwargs.items():
                if key == "TABLO":
                    tablo = value
                elif key == "SART":
                    sart = value
                
                         
            sorgu = "DELETE FROM {} WHERE {}".format(tablo,sart)
            
            self.cur.execute(sorgu)
            self.db.commit()
            return True
        except Exception as hata:
            print(hata)
            return False
        finally:
            self.db.close()



