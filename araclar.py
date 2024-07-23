

class AracKiralama:
    def __init__(self,stok_adet,marka,model,gunlukFiyat,saatlikFiyat,haftalikFiyat,aylikFiyat):
        '''Aracı tanımlıyoruz'''
        self.stok = stok_adet
        self.marka = marka
        self.model = model
        self.kiralanmisAracSayisi = 0
        self.gunlukFiyat = gunlukFiyat
        self.saatlikFiyat = saatlikFiyat
        self.haftalikFiyat = haftalikFiyat
        self.aylikFiyat = aylikFiyat

    def kirala(self,kiralanan_aracSayisi):
        '''Eğer istenen miktarda boşta araç varsa kiralama işlemi yapılıyor.Kiralanan araç sayısı değişkeninin artmasını sağlıyor'''
        if (self.stok - self.kiralanmisAracSayisi) >= kiralanan_aracSayisi:
            self.kiralanmisAracSayisi += kiralanan_aracSayisi
            return True
        else:
            return False
        
    def AnlikStokGoruntule(self):
        '''Boştaki araç sayısını veriyor'''
        return self.stok - self.kiralanmisAracSayisi
    
    def KritikStokGoruntule(self):
        '''Eğer boştaki araç sayısı %25in altındaysa her ana menü çağırıldığında uyarı veriyor'''
        if self.AnlikStokGoruntule() < self.stok * 0.25:
            print(f"\n{self.marka} {self.model} Kritik Stokta")

    def GunlukKirala(self,kiralanan_aracSayisi):
        '''Aracın günlük kiralanmasını sağlıyor'''
        if self.kirala(kiralanan_aracSayisi):
            return True
        else:
            return False
        
    def SaatlikKirala(self,kiralanan_aracSayisi):
        '''Aracın saatlik kiralanmasını sağlıyor'''
        if self.kirala(kiralanan_aracSayisi):
            return True
        else:
            return False
        
    def HaftalikKirala(self,kiralanan_aracSayisi):
        '''Aracın haftalık kiralanmasını sağlıyor'''
        if self.kirala(kiralanan_aracSayisi):
            return True
        else:
            return False
        
    def AylikKirala(self,kiralanan_aracSayisi):
        '''Aracın aylık kiralanmasını sağlar'''
        if self.kirala(kiralanan_aracSayisi):
            return True
        else:
            return False
        
    def Indirim(self,oran):
        '''İndirim oranı şart verilmişse şarta uygunluğu kontrol edilir'''
        return oran

    def GeriDonenArac(self,geriDonen_aracSayisi):
        '''Kiralanmadan gelen araçların tekrar stoğa eklenmesini sağlar'''
        self.kiralanmisAracSayisi -= geriDonen_aracSayisi        

class ArabaKiralama(AracKiralama):
    pass

class MotorsikletKiralama(AracKiralama):
    pass

class KaravanKiralama(AracKiralama):
    def Indirim(self,oran):
        '''İndirim oranı şart verilmişse şarta uygunluğu kontrol edilir'''
        if oran > 25:
            oran = 25
            print("\nEn fazla %25 indirim yapılabilir")
        return oran

__aracTipleri = [ArabaKiralama,MotorsikletKiralama,KaravanKiralama]

class KiralamaIslemi():
    def __init__(self,arac,kiralanmisAracSayisi,fatura):
        '''Kiralama İşlemi tanımlanır'''
        self.arac = arac
        self.kiralanmisAracSayisi = kiralanmisAracSayisi
        self.fatura = fatura