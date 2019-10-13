import sqlite3
print("""
X ülkesinin başkenti neresidir? (X kullanıcı inputu olacaktır)

Y bölgesinde konuşulan tüm dilleri listeleyin. (Y kullanıcı inputu olacaktır)

Z dilinin konuşulduğu şehirlerin sayısını bulunuz. (Z kullanıcı inputu olacaktır)

Kullanıcıdan bir A bölgesi(region) ve bir B dili(language) alın. Eğer bu B dili,
 A bölgesindeki ülkelerin birinde resmi dil ise, o ülke(ler)in isim(ler)ini listeleyin.
 Eğer o bölgedeki hiçbir ülkede resmi dil değilse, "B dili A bölgesindeki hiçbir ülkede resmi dil değildir.
 " şeklinde bir output verin. (A ve B kullanıcı inputu olacaktır.)

Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı ile birlikte bulunuz.
(Bazı dillerin bir kıtada birden fazla ülkede konuşulduğunu unutmayın ve bunu dikkate alarak bir dili birden fazla kez hesaplamayın.)

""")

while True:
    mesenger = """

    MENU
    _________________________________
    Baskent Sorgulama               1
    Bolgelerin Dilleri              2
    Konusulan Dillerin Ulkeleri     3
    Resmi Dil Sorgulama             4
    Kita Dilleri                    5
    cikis                           Q
    _________________________________
    """
    print ( mesenger )
    try:
        Data = sqlite3.connect ( "C:\\payton\\17.Hafta-Odevler\\world.db" )
        crsr = Data.cursor ()
        secim=input('Choise : ')
        if secim.lower()=='q':
            break
        elif secim=='1':

            ulke=input('Country :')
            Capital_city = list ( crsr.execute ("""SELECT country.Name , city.Name
            FROM country, city WHERE country.Capital == city.ID and country.Name=? """,(ulke,) ) );
            if Capital_city==[]:
                print('there is not Capital city')
            else:

                for i in Capital_city:
                   print('The Capital city of ',i[0], 'is ',i[1])
                Data.commit ()
                Data.close ()


        elif secim=='2':

            Bolge=input('Region : ')

            Language_religion= list ( crsr.execute ( """SELECT country.Name , countrylanguage.Language
                   FROM country, countrylanguage WHERE country.Code=countrylanguage.CountryCode and country.Region=? """ , (Bolge ,) ) );
            if Language_religion == [] :
                print ( 'there is not Language ' )
            else :

                for i in Language_religion :
                    print (i[0],'--->'.rjust(5),i[1])
                Data.commit ()
                Data.close ()

        elif secim=='3':

            Languages=input('Language:')
            Language_city=list ( crsr.execute ( """SELECT city.Name
                   FROM city, countrylanguage WHERE city.CountryCode=countrylanguage.CountryCode and countrylanguage.Language=?""" , (Languages ,) ) );
            print(len(Language_city))
            Data.commit ()
            Data.close ()



        elif secim=='4':
            Region_choise=input('Region : ')
            Languages_choise=input('Language: ')

            control_country=list ( crsr.execute ( """SELECT country.Name , countrylanguage.Language,countrylanguage.IsOfficial
                   FROM country, countrylanguage WHERE country.Code=countrylanguage.CountryCode and country.Region=? and countrylanguage.Language=? and countrylanguage.IsOfficial='T'  """ ,  (Region_choise ,Languages_choise) ) );

            if control_country== [] :
                print ( Languages_choise, Region_choise,'Bolgesinde resmi dil degildir ' )
            else :

                for i in control_country :
                    print ( *i )
                Data.commit ()
                Data.close ()
        elif secim == '5' :

            continent=list ( crsr.execute ( """SELECT country.Continent , countrylanguage.Language
                   FROM country, countrylanguage WHERE country.Code=countrylanguage.CountryCode """  ) );
            continent=sorted(set(continent))
            sayac=list()
            for i in continent:
                sayac.extend(i)
            print('Africa Continent `Languges are ',sayac.count('Africa'))
            print ( 'Asia Continent `Languges` are ' , sayac.count ( 'Asia' ) )
            print ( 'Europe Continent` Languges are ' , sayac.count ( 'Europe' ) )
            print ( 'North America Continent` Languges are ' , sayac.count ( 'North America' ) )
            print ( 'South America Continent` Languges are ' , sayac.count ( 'South America' ) )
            print ( 'Oceania Continent `Languges are ' , sayac.count ( 'Oceania' ) )

            Data.commit ()
            Data.close ()
        else:
            print('Wrong Choise')
            continue

    except:
        print('wrong Record')
        continue








