from araclar import KiralamaIslemi

class Musteriler:
    def __init__(self,musteriTipi,isim):
        '''Müşteriyi Tanımlıyoruz'''
        self.talepler = []
        self.isim = isim
        self.musteriTipi = musteriTipi
        self.toplamOdenen = 0
    def Taleb(self,arac,kiralanmisAracSayisi,fatura):
        '''Talepler değişkenine yapılan kiralama işlemeleri ekleniyor'''
        self.talepler.append(KiralamaIslemi(arac,kiralanmisAracSayisi,fatura))
    def GeriIade(self,kiralamaIslemi):
        '''Araç geri teslim edildiğinde yapılan talep kaldırılıyor'''
        self.talepler.remove(kiralamaIslemi)
    def TalepSayisi(self):
        '''Yapılan talep sayısı çağırılıyor'''
        return len(self.talepler)


class MusteriTipi:
    def __init__(self,adi,indirimOrani):
        '''Müşteri Tipini tanımlıyoruz'''
        self.adi = adi
        self.indirimOrani = indirimOrani

__musteriTipleri = [MusteriTipi("Silver",5),MusteriTipi("Gold",10),MusteriTipi("Platinium",20)]