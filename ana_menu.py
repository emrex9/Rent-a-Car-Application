from araclar import ArabaKiralama,__aracTipleri
import musteriler

Musteriler = []

def musterileriGoster():
    print("""
            ***** Müşteriler *****
            """)
    index = 1
    for musteri in Musteriler:
        print(f"{str(index)} - {musteri.isim} - {musteri.musteriTipi.adi}\n")
        index += 1

ana_menü = True

araclar = []

araclar.append(__aracTipleri[0](10,"BMW","i8",10,10,10,10))

Musteriler.append(musteriler.Musteriler(musteriler.__musteriTipleri[2],"Emre"))

def aracTipiGetir(aracTipi):
    seciliAraclar = []
    for arac in araclar:
        if type(arac) == aracTipi:
            seciliAraclar.append(arac)
    return seciliAraclar

def secilenTipAraclariGoster(araclar):
    index = 1
    for arac in araclar:
        print(f"{str(index)} - {arac.marka} {arac.model} Stok: {str(arac.AnlikStokGoruntule())} \n")
        index += 1


def kiralamaSistem(aracTuruAdi,aracTuruAdiCogul,aracTipi):
    global ana_menü,bitir
    secilenAracTuru = aracTipiGetir(aracTipi)
    if len(Musteriler) <= 0 or len(secilenAracTuru) <= 0:
        print("\nMÜŞTERİ veya ARAÇ yok!!\n")
        ana_menü = True
    else:
        print(f"""
            ***** {aracTuruAdi} Kiralama *****
            1. {aracTuruAdi} stoğunu göster
            2. Saatlik Kiralama
            3. Günlük Kiralama
            4. Haftalık Kiralama
            5. Aylık Kiralama
            6. Ana Menüye Geri Dön
            7. Çıkış
            """)
        secim = int(input("İstenilen Menüdeki harfi Girin: "))
        if secim == 7:
            bitir = True
        elif secim == 6:
            ana_menü = True
        elif secim == 1:
            secilenAracTuru = aracTipiGetir(aracTipi)

            print(f"""
                ***** {aracTuruAdiCogul} *****""")
            secilenTipAraclariGoster(secilenAracTuru)
            ana_menü = True
        else:
            musterileriGoster()
            seciliSira = int(input("\nSeçilen Müşteri : "))
            seciliMusteri = Musteriler[seciliSira - 1]
            secilenAracTuru = aracTipiGetir(aracTipi)

            print(f"""
                ***** {aracTuruAdiCogul} *****""")
            secilenTipAraclariGoster(secilenAracTuru)

            seciliSira = int(input("\nSeçilen Araba : "))
            miktar = int(input("\nKiralanıcak Araba Sayısı : "))
            sonuc = False
            ucret = 0
            if secim == 2:
                sonuc = secilenAracTuru[seciliSira - 1].SaatlikKirala(miktar)
                ucret = secilenAracTuru[seciliSira - 1].saatlikFiyat
            elif secim == 3:
                sonuc = secilenAracTuru[seciliSira - 1].GunlukKirala(miktar)
                ucret = secilenAracTuru[seciliSira - 1].gunlukFiyat
            elif sonuc == 4:
                sonuc = secilenAracTuru[seciliSira - 1].HaftalikKirala(miktar)
                ucret = secilenAracTuru[seciliSira - 1].haftalikFiyat
            elif sonuc == 5:
                sonuc = secilenAracTuru[seciliSira - 1].AylikKirala(miktar)
                ucret = secilenAracTuru[seciliSira - 1].aylikFiyat
            if sonuc:     
                ekstraIndirim = int(input("\n Ekstra İndirim Yüzdesi : %"))
                ekstraIndirim = secilenAracTuru[seciliSira - 1].Indirim(ekstraIndirim)
                if seciliMusteri.musteriTipi != None:
                    fatura =  (ucret * miktar) - ((ucret * miktar) * (seciliMusteri.musteriTipi.indirimOrani / 100))
                    print(f"\n Müşteri Tipinden %{seciliMusteri.musteriTipi.indirimOrani} indirim uygulandı")
                else:
                    fatura =  (ucret * miktar)
                fatura = fatura - (fatura * (ekstraIndirim / 100))
                seciliMusteri.Taleb(secilenAracTuru[seciliSira - 1],miktar,fatura)

                seciliMusteri.sonFatura = fatura
                seciliMusteri.toplamOdenen += fatura
                print(f"\nKiralama Ücreti ₺{fatura}")
                print("\nAraba(lar) kiralandı")
            else:
                print("Araç kiralanamadı!!")
            ana_menü = True

while True:
    if ana_menü:
        print("""
              ***** Araç kiralama Sistemi *****
              A. Araba Kiralama 
              B. Bisiklet Kiralama
              C. Karavan Kiralama
              D. Müşteri Ekleme/Silme
              E. Araç Marka-Model Ekleme/Silme
              F. Araç İade
              Q. Çıkış
              """)
        ana_menü = False

        for arac in araclar:
            arac.KritikStokGoruntule()

        secim = input("İstenilen Menüdeki harfi Girin: ")
    bitir = False

    
    if secim == "A" or secim == "a":
        kiralamaSistem("Araba","Arabalar",__aracTipleri[0])
        if bitir:
            break
    elif secim == "B" or secim == "b":
        kiralamaSistem("Bisiklet","Bisikletler",__aracTipleri[1])
        if bitir:
            break
    elif secim == "C" or secim == "c":
        kiralamaSistem("Karavan","Karavanlar",__aracTipleri[2])
        if bitir:
            break
    elif secim == "E" or secim == "e":
        print("""
              ***** Araç Ekleme/Silme *****
              1 - Ekle
              2 - Sil
              3 - Ana Menü
              """)
        secim = int(input("İstenilen Menüdeki harfi Girin: "))
        if secim == 1:
            print("""
                ***** Araç Tipleri *****
                1 - Araba
                2 - Bisiklet
                3 - Karavan
                """)
            aracTipiSirasi = int(input("\nArac Tipi Sırası : "))
            _marka = input("\n Marka Adı : ")
            _model = input("\n Model Adı : ")
            _stok = int(input("\n Stok Adedi : "))
            _gunlukFiyat = int(input("\n Günlük Fiyat : "))
            _saatlikFiyat = int(input("\n Saatlik Fiyat : "))
            _haftalikFiyat = int(input("\n Haftalık Fiyat : "))
            _aylikFiyat = int(input("\n Aylık Fiyat : "))
            arac = __aracTipleri[aracTipiSirasi - 1](_stok,_marka,_model,_gunlukFiyat,_saatlikFiyat,_haftalikFiyat,_aylikFiyat)
            araclar.append(arac)
            print("Araç eklendi")
            ana_menü = True
        elif secim == 2:
            if len(araclar) <= 0:
                print("\nAraç sayısı 0\n")
                ana_menü = True
                continue 
            secilenTipAraclariGoster(araclar)
            seciliSira = int(input("\nSeçilen Araç : "))
            araclar.pop(seciliSira - 1)
            print("Araç Silindi")
            ana_menü = True
        elif secim == 3:
            ana_menü = True
    elif secim == "D" or secim == "d":
        print("""
              ***** Müşteri Ekleme/Silme *****
              1 - Ekle
              2 - Sil
              3 - Ana Menü
              """)
        secim = int(input("İstenilen Menüdeki harfi Girin: "))
        if secim == 1:
            musteriIsim = input("Müşteri Adı : ")
            print("""
                ***** Müşteri Tipleri *****
                1 - Platinium %20 İndirim
                2 - Gold %10 İndirim
                3 - Silver %5 İndirim
                4 - Normal Müşteri
                """)
            musteriTipi = int(input("Müşteri Tipi Sırası : "))
            secilenMusteriTipi = None
            if musteriTipi != 4:
                secilenMusteriTipi = musteriler.__musteriTipleri[musteriTipi - 1]
            Musteriler.append(musteriler.Musteriler(secilenMusteriTipi,musteriIsim))
            ana_menü = True
        elif secim == 2:
            if len(Musteriler) <= 0:
                print("\nMüşteri sayısı 0\n")
                ana_menü = True
                continue
            musterileriGoster()
            seciliSira = int(input("\nSeçilen Müşteri : "))
            Musteriler.pop(seciliSira - 1)
            print("Müşteri Silindi")
            ana_menü = True
        elif secim == 3:
            ana_menü = True
    elif secim == "F" or secim == "f":
        musterileriGoster()
        seciliSira = int(input("\nSeçilen Müşteri : "))
        print("""
            ***** Müşteri Kiralama İşlemleri *****
            """)
        sira = 1
        if Musteriler[seciliSira - 1].TalepSayisi() > 0:
            for islem in Musteriler[seciliSira - 1].talepler:
                print(f"\n {str(sira)} - {islem.arac.marka} {islem.arac.model}    Kiralanan Araç Sayısı : {islem.kiralanmisAracSayisi}    Fatura : ₺{islem.fatura}")
                sira += 1
            seciliIslemSira = int(input("\nSeçilen İşlem : "))
            secilenIslem = Musteriler[seciliSira - 1].talepler[seciliIslemSira - 1]
            for arac in araclar:
                if secilenIslem.arac == arac:
                    arac.GeriDonenArac(secilenIslem.kiralanmisAracSayisi)
            print()
            yanit = input("\n Araçlar geç mi teslim edildi? Evet/Hayır\n ")
            if yanit == "Evet" or yanit == "evet":
                ekstraUcret = secilenIslem.fatura * 0.2
                print(f"\n Gecikme Ücreti : ₺{str(ekstraUcret)}   Toplam Ücret : ₺{str(ekstraUcret + secilenIslem.fatura)}")
            else:
                print(f"\n Toplam Ücret : ₺{str(secilenIslem.fatura)}")
            print("\nAraç(lar) teslim edildi")
            Musteriler[seciliSira - 1].GeriIade(secilenIslem)
            ana_menü = True
        else:
            print("\n Seçili müşterinin kiralama işlemi bulunmamaktadır")
            ana_menü = True
    elif secim == "Q" or secim == "q":
        print("Çıkış yapılıyor...")
        break
    else:
        print("\n Geçersiz İşlem!!")
        ana_menü = True
