#Televizyon Kumandası Uygulaması
#İşlemler: 1,2,3,4

from random import randint as r

class Kumanda:
    def __init__(self,tvDurum=False,tvSes=0,kanalListesi=["Trt"],kanal="Trt"):
        print("Kumanda Oluşturuluyor...")
        self.TvSesi = tvSes
        self.TvDurumu = tvDurum
        self.KanalListesi = kanalListesi
        self.Kanal = kanal
    def SesAzaltArttir(self):
        while True:
            if self.TvDurumu!=True:
                print("Önce televizyonu açman lazım.")
                break
            karakter = input("Sesi azaltmak için '<', sesi arttırmak için '>', çıkış için 'q' tuşlarını kullan.")
            if karakter =='<' and self.TvSesi!=0:
                self.TvSesi -=1
            elif karakter=='>' and  self.TvSesi!=15:
                self.TvSesi+=1
            elif karakter =="q":
                print("Ses => {}.. Menüden çıkılıyor...".format(self.TvSesi))
                break
            print("Ses => {}".format(self.TvSesi))
    def TvKapat(self):
        if self.TvDurumu ==True:
            print("Televizyon kapatılıyor...")
            self.TvDurumu =False
        else:
            print("Televizyon zaten kapalı.")
    def TvAc(self):
        if self.TvDurumu ==False:
            print("Televizyon açılıyor...")
            self.TvDurumu = True
        else :
            print("Televizyon zaten açık.")

    def RastgeleKanal(self):
        rastgele = r(0,len(self.KanalListesi)-1)
        self.Kanal = self.KanalListesi[rastgele]
        print("Şuanki kanal => {}".format(self.Kanal))
    def KanalEkle(self,kanal):
        print("Kanal eklendi, eklenen kanal => {}".format(kanal))
        self.KanalListesi.append(kanal)

    def KanalBilgileriniGoster(self):
         for x in self.KanalListesi:
             print(x)
    def __str__(self):
        return "Televi<yon Durumu: {}\n Ses: {}\n Kanallar: {}\n Şuanki Kanal : {}\n".format(self.TvDurumu,self.TvSesi,self.KanalListesi,self.Kanal)