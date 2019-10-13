import sqlite3 as sql

db = sql.connect('world.db')
im = db.cursor()

#1- X ülkesinin başkenti neresidir? (X kullanıcı inputu olacaktır)

#2-Y bölgesinde konuşulan tüm dilleri listeleyin. (Y kullanıcı inputu olacaktır)

#3-Z dilinin konuşulduğu şehirlerin sayısını bulunuz. (Z kullanıcı inputu olacaktır)

#4-Kullanıcıdan bir A bölgesi(region) ve bir B dili(language) alın. Eğer bu B dili,
# A bölgesindeki ülkelerin birinde resmi dil ise, o ülke(ler)in isim(ler)ini listeleyin.
# Eğer o bölgedeki hiçbir ülkede resmi dil değilse, "B dili A bölgesindeki hiçbir ülkede resmi dil değildir."
# şeklinde bir output verin. (A ve B kullanıcı inputu olacaktır.)

#5-Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı ile birlikte bulunuz.
# (Bazı dillerin bir kıtada birden fazla ülkede konuşulduğunu unutmayın ve bunu dikkate alarak
# bir dili birden fazla kez hesaplamayın.)
karsilama_mesaji = """ ULKELER VE DILLER\n\n
Baskentini ogrenmek ustdiginiz ulkeyi ogrenmek icin 1'e basiniz\n
Dunyanin herhangi bir bolgesinde konusulan dilleri ogrenmek icin 2'ye basiniz\n
Herhangi bir dilin konusuldugu sehirlerin sayisini bulmak icin 3'e basiniz\n
Sectiginiz herhangi bir dilin , sectiginiz herhangi bir bolgedeki ulkelerde konusulup konusulmadigini ogrenmek icin 4'e basiniz\n
Tum kitalari ve o kitalardaki konusulan dillerin sayisini ogrenmek icin 5'e basiniz\n
Programdan cikmak icin 'q' harfine basiniz
"""
print(karsilama_mesaji)
while True:
    kullanici_secimi = input("Lutfen seciminizi yapiniz: ")
    if kullanici_secimi == "1":
        kullanici_ulke = input("Lutfen Baskentini Ogrenmek Istediginiz Ulkenin Adini Yaziniz: ").capitalize()
        im.execute(""" SELECT city.Name FROM city, country 
	    WHERE country.Name = ?
	    AND city.ID = country.Capital""",(kullanici_ulke,))
        veri1 = im.fetchall()[0]
        print(*veri1)
    elif kullanici_secimi == "2":
        konusulan_dil = input("Konusulan dilleri gormek icin ulke adi giriniz: ").capitalize()
        im.execute("SELECT Language FROM countrylanguage "
                   "INNER JOIN country on country.Code = countrylanguage.CountryCode "
                   "WHERE country.Name = ?", (konusulan_dil,))
        veri2 = im.fetchall()
        print(*veri2)
    elif kullanici_secimi == "3":
        dil = input("Hangi dilin kac sehirde konusuldugunu gormek icin dil adi girin: ").capitalize()
        im.execute("SELECT Count(city.Name) FROM city "
                   "INNER JOIN countrylanguage on countrylanguage.CountryCode = city.CountryCode "
                   "WHERE countrylanguage.Language = ?", (dil,))
        sehir_sayisi = im.fetchall()[0]
        print(*sehir_sayisi, "sehirde konusuluyor.")
    elif kullanici_secimi == "4":
        bolge = input("Lutfen bolge adi girin: ").title()
        dil = input("Lurfen dil adi girin: ").capitalize()
        im.execute("""select country.Name from country,countrylanguage 
            where country.Region= ? and country.Code=countrylanguage.CountryCode 
            and countrylanguage.Language= ? 
            and countrylanguage.IsOfficial='T'""", (bolge, dil,))
        ulkeler = im.fetchall()
        if len(ulkeler) == 0:
            print("Bu dil bu bolgede resmi dil olarak kullanilmamaktadir.")
        else:
            print(bolge, 'bolgesinde', dil, 'dilini resmi olarak konusulan ulkeler:\n', ulkeler)
    elif kullanici_secimi == "5":
        im.execute("""SELECT continent,count(Distinct language) FROM countrylanguage,country
        Where countrylanguage.countrycode=country.code
        GROUP BY country.continent""")
        dil=im.fetchall()
        print("Tum kitalar ve kitalarda konusulan diller",*dil)
    elif kullanici_secimi == "q" or kullanici_secimi == "Q":
        print("Programdan cikiliyor")
        quit()