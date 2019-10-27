##1-X ülkesinin başkenti neresidir? (X kullanıcı inputu olacaktır)
##
##2-Y bölgesinde konuşulan tüm dilleri listeleyin. (Y kullanıcı inputu olacaktır)
##
##3-Z dilinin konuşulduğu şehirlerin sayısını bulunuz. (Z kullanıcı inputu olacaktır)
##
##          4-Kullanıcıdan bir A bölgesi(region) ve bir B dili(language) alın. Eğer bu B dili, A bölgesindeki ülkelerin birinde resmi dil ise,
##      o ülke(ler)in isim(ler)ini listeleyin. Eğer o bölgedeki hiçbir ülkede resmi dil değilse, "B dili A bölgesindeki hiçbir ülkede resmi dil değildir."
##      şeklinde bir output verin. (A ve B kullanıcı inputu olacaktır.)
##
##5-Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı ile birlikte bulunuz.
##(Bazı dillerin bir kıtada birden fazla ülkede konuşulduğunu unutmayın ve bunu dikkate alarak bir dili birden fazla kez hesaplamayın.)


import os
import sqlite3 as tab
vt=tab.connect("world.db")
im=vt.cursor()

print(""" Aşağıdaki seçeneklerden birini yanındaki numarayı tuşlayarak seçiniz:
1-Ülkenin başkentini sorgulama
2-Bölgede konuşulan dilleri sorgulama
3-Hangi dilin kaç farklı şehirde konuşulduğunu sorgulama
4-Bölge ve dil  eşleşmesinde ülkeleri bulma
5-Kıtalarda konuşulan farklı dil sayısını bulma""")



secim=input("seciminizi tuşlayınız..")

if secim=="1":
    ulk=input ("\nBaşkentini bulmak istediğini ülkenin adını giriniz..:")
    im.execute ("""SELECT city.name FROM city, Country WHERE city.ID==country.Capital AND (country.Name==?)""",(ulk,))
    baskent=list(im.fetchall())[0][0]
    print(baskent)
    print ("\n {} ülkesinin başkenti, {} dir".format (ulk, baskent))


if secim=="2":
    blg=input ("\nHangi dillerin konuşulduğunu öğrenmek istediğiniz bölgeyi giriniz..:")
    im.execute ("""SELECT city.name FROM city, Country WHERE city.ID==country.Capital AND (country.Region==?)""",(blg,))
    baskent=list(im.fetchall())[0][0]
    print(baskent)
    print ("\n {} ülkesinin başkenti, {} dir".format (ulk, baskent))

    
if secim=="3":
    dil=input ("\nKaç şehirde konuşulduğunu öğrenmek için bir dil adı giriniz..:")
    im.execute("""SELECT COUNT(city.Name) FROM city INNER JOIN countrylanguage ON city.CountryCode=countrylanguage.countrycode WHERE countrylanguage.Language = ?""",(dil,))
    print(im.execute)

if secim=="4":
    bolge=input ("\nLütfen bölge ve dil eşleşmesini öğrenmek için önce \nBir bölge adı giriniz...")
    dil=input("Lütfen şimdi de bir dil adı giriniz..:")
    im.execute("""SELECT country.Name FROM countrylanguage INNER JOIN country ON countrylanguage.countryCode=country.Code WHERE countrylanguage.IsOfficial = 'T' AND country.Region = ? AND countrylanguage.language= ?""",(bolge,dil,))
    sonuc=im.fetchall()
    if sonuc==[]:
        print("\n{} dili {} bölgesindeki hiçbir ülkede resmi dil değildir.".format(dil,bolge))
    else:
        print(sonuc)
    
if secim=="5":
    im.execute("""SELECT continent,count(Distinct language) FROM countrylanguage,country
        Where countrylanguage.countrycode=country.code
        GROUP BY country.continent """ )
    print(im.fetchall())

