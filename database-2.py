# coding=utf-8
import sqlite3 as sql
ana_menu='''Bir ülkenin başkentini öğrenmek için 1'e,
Bir bölgede konuşulan tüm dilleri öğrenmek için 2'ye,
Bir dilin konuşulduğu şehirlerin sayısını bulmak için 3'e,
Bir dilin bir bölgedeki hangi ülkelerde konuşulduğunu görmek için 4'e,
Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı öğrenmek için 5'e
Programdan çıkmak için q'ya basınız.\n\n'''

data=sql.connect('C:/Users/Toshiba/Desktop/antremanlar/17.Hafta-Odevler/world.db')
im=data.cursor()

print (ana_menu)
while True:
    secim=input('\nLütfen yapamak istediğiniz işlem için uygun giriş yapınız:')

    if secim == '1':
        try:
            veri=(input('\nBaşkentini öğrenmek istediğiniz ülkenin ismini yazınız: ')).title()
            im.execute("SELECT capital FROM country WHERE LocalName=? OR name=?",(veri,veri))
            capital =im.fetchone()
            im.execute("SELECT name FROM city WHERE id=?",(capital[0],))
            print (f'\nThe capital city of {veri} is {im.fetchone()[0]}\n\n')
        except TypeError:
            print ('Lütfen ülke ismini uluslararası veya lokal bir isim olarak giriniz.\n\n')

    elif secim == '2':
        try:
            veri=(input('Bir bölgede konuşulan tüm dilleri öğrenmek için bölge ismi giriniz.\n')).title()
            im.execute("""SELECT countrylanguage.Language FROM countrylanguage INNER JOIN country ON
            countrylanguage.countrycode=country.code WHERE Region=?""",(veri,))
            language=im.fetchall()
            print (f'The languages of region of {veri}:')
            for i in language:
                print(language.index(i)+1,'-',i[0],sep='')

        except TypeError:
            print ('Lütfen girdiğiniz bölge ismini kontrol ediniz.\n\n')

    elif secim == '3':
        try:
            veri = (input('Bir dilin kaç farklı şehirde konuşulduğun bulmak için bir dil ismi giriniz.\n')).title()
            im.execute("""SELECT city.name FROM city INNER JOIN countrylanguage ON
            countrylanguage.countrycode=city.countrycode WHERE Language=?""", (veri,))
            city=im.fetchall()
            print(f'{veri} language is spoken in {len(city)} city.')
        except TypeError:
            print ('Lütfen girdiğiniz dil ismini kontrol ediniz.\n\n')

    elif secim == '4':
        try:
            bolge=(input('Bir bölge ismi giriniz:')).title()
            dil = (input('Bir dil ismi giriniz:')).title()
            im.execute("""SELECT country.name FROM country INNER JOIN countrylanguage ON
            country.code=countrylanguage.countrycode WHERE isOfficial='T' AND language=? AND region=?""",(dil,bolge))
            country=im.fetchall()
            if country:
                for i in country:
                    print(country.index(i) + 1, '-', i[0], sep='')
            else:
                print(f'{dil} isn\'t an official language of any country in the {bolge} region' )

        except TypeError:
            print ('Lütfen girdiğiniz verileri kontrol ediniz.\n\n')

    elif secim == '5':
        im.execute("""SELECT country.continent,language FROM country,countrylanguage WHERE
        country.code=countrylanguage.countrycode""")
        continent=im.fetchall()
        soz={}
        for i in continent:
            soz[i[0]]=list({j[1] for j in continent if j[0]==i[0]})
        for i in soz.keys():
            print('\n',i.upper(),f'(Konuşulan dil sayısı:{len(soz[i])})','\n','-'*(len(i)+26))
            for j in soz[i]:
                print(soz[i].index(j)+1,'-',j,sep='')

    elif secim.lower() == 'q':
        print ('Program kapatılıyor.')
        exit()

    else:
        print ('Yanlış giriş yaptınız.')