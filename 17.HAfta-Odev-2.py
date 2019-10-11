""""world.db" database'ini kullanarak isterseniz video derste oldugu gibi
 bir dongu icerisinde yaparak isterseniz de ayri ayri kodlar yazarak
 asagidaki sorulari cevaplamanizi istiyoruz.

1-X ülkesinin başkenti neresidir? (X kullanıcı inputu olacaktır)

2-Y bölgesinde konuşulan tüm dilleri listeleyin. (Y kullanıcı inputu olacaktır)

3-Z dilinin konuşulduğu şehirlerin sayısını bulunuz. (Z kullanıcı inputu olacaktır)

4-Kullanıcıdan bir A bölgesi(region) ve bir B dili(language) alın. Eğer bu B dili,
 A bölg indeki ülkelerin birinde resmi dil ise, o ülke(ler)in isim(ler)ini listeleyin.
 Eğer o bölgedeki hiçbir ülkede resmi dil değilse, "B dili A bölgesindeki
 hiçbir ülkede resmi dil değildir." şeklinde bir output verin. (A ve B kullanıcı inputu olacaktır.)

5-Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı ile birlikte bulunuz.
(Bazı dillerin bir kıtada birden fazla ülkede konuşulduğunu unutmayın ve bunu
dikkate alarak bir dili birden fazla kez hesaplamayın.)"""

import sqlite3 as sql
vt=sql.connect(r"C:\Users\hkn\Desktop\Odevler\17.Hafta-Odevler\world.db")
im=vt.cursor()

karsilama_mesaji= """ 
****************DUNYAYA HOSGELDINIZ***************
DUNYA HAKKINDA OGRENMEK ISTEYEBILECEGINIZ BILGILER
1) DUNYA NUFUSU
2) ULKE BILGILERI(Baskent,Nufus,YUzolcumu,Kita)
3) BIR BOLGEDE KONUSULAN DILLER
4) BIR DILIN KONUSULDUGU SEHIRLER
5) BOLGE-DIL SORGULAMA
6) KITALARA GORE KONUSULAN DIL SAYISI SORGULAMA
7) CIKMAK ICIN 'Q'ya BASINIZ
"""
print(karsilama_mesaji)

while True:
    kullanici_secimi = input("Lutfen seciminizi yapiniz: ")

    if kullanici_secimi == "1":
        im.execute('SELECT SUM(Population)as "Toplam Nufus" FROM country')
        print(im.fetchall())
        # vt.commit()

    elif kullanici_secimi == "2":
        ulke_adi = input("Lutfen detay bilgilerini ogrenmek istediginiz ulkenin adini giriniz: ")
        cap=ulke_adi.title()
        im.execute("SELECT city.name from country,city where country.Capital=city.ID and Country.Name = ?",(cap,))
        print(im.fetchall())
        im.execute("SELECT * from country where name = ?",(cap,))
        print(im.fetchall())
        # vt.commit()

    elif kullanici_secimi == "3":
        bolgeler = input("Lutfen bolge adini giriniz:")
        bol=bolgeler.title()
        print("BOLGEDE KONUSULAN DILLER")
        im.execute('SELECT Language FROM country,countrylanguage where country.code=countrylanguage.CountryCode and country.Region=?',(bol,))
        diller=im.fetchall()
        if len(diller)>0:
            print(set(diller))
        else:
            print("Gecersiz Giris veya Bolgede konusulan dil yok.")
    elif kullanici_secimi == "4":
        dil= input("Sorgulamak istediginiz Dil:")
        dill = dil.title()
        print(dill,"Dilinin konusuldugu sehirler:")
        im.execute(
            'SELECT city.name FROM city,country,countrylanguage where countrylanguage.CountryCode=city.CountryCode and countrylanguage.language=?',
            (dill,))
        lang_city = im.fetchall()
        if len(lang_city) > 0:
            print(dill,"in konusuldugu sehir saysi=",len(set(lang_city)),'\n',set(lang_city))
        else:
            print("Gecersiz Giris veya dilin konusuldugu sehir yok.")
    elif kullanici_secimi == "5":
        B = input("Sorgulamak istediginiz bolge adi:")
        A = input("Sorgulamak istediginiz dil:")
        dill = A.title()
        bolge=B.title()
        print(bolge,"sinde",dill,"dilinin konusuldugu ulkeler:")
        im.execute(
            'SELECT country.name FROM country,countrylanguage where countrylanguage.CountryCode=Country.Code and (country.Region=? and countrylanguage.Language=?)',
            (bolge,dill,))
        lang_city = im.fetchall()
        if len(lang_city) > 0:
            print(dill,"in konusuldugu sehir saysi=",len(set(lang_city)),'\n',set(lang_city))
        else:
            print("Gecersiz Giris veya dilin konusuldugu sehir yok.")
    elif kullanici_secimi == "6":
        kitalar=["Asia","Africa","Europe","North America","South America","Oceania","Antarctica"]
        print('"Asia","Africa","Europe","North America","South America","Oceania","Antarctica" kitalarinda konusulan diller sirasiyla asagidadir.')
        for i in kitalar:
            if i=="Antarctica":
                print("Antarctica'da henuz konusulan dil yok belki penguence diyebiliriz...")
            else:
                kita=im.execute('SELECT Language FROM country,countrylanguage where country.code=countrylanguage.CountryCode and Country.Continent=?',(i,))
                kitas=set(kita)
                print("Konusulan dil sayisi=",len(kitas),sorted(kitas))

    elif kullanici_secimi == "q" or kullanici_secimi == "Q":
        print("Programdan cikiliyor")
        quit()