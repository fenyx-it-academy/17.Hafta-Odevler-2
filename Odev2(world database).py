import _sqlite3 as sql

vt = sql.connect('world.db')
im = vt.cursor()

# 1. X ülkesinin başkenti neresidir? (X kullanıcı inputu olacaktır)
baskent= input("Lutfen baskentini ogrenmek istediginiz ulkeyi bas harfi buyuk giriniz(in English):")
im.execute("SELECT city.Name FROM city INNER JOIN country ON city.CountryCode=country.Code WHERE country.name= ?"
           "AND city.id=country.capital",(baskent,) )
print("Capital city of",baskent, *im.fetchall())

# 2. Y bölgesinde konuşulan tüm dilleri listeleyin. (Y kullanıcı inputu olacaktır)
bolge= input("Lutfen konusulan tum dilleri ogrenmek istediginiz bolge ismini giriniz(in English):")
im.execute("SELECT DISTINCT countrylanguage.Language FROM countrylanguage INNER JOIN country ON "
           "countrylanguage.countryCode=country.Code WHERE country.Region= ?",(bolge,))
print(im.fetchall())

# 3. Z dilinin konuşulduğu şehirlerin sayısını bulunuz. (Z kullanıcı inputu olacaktır)
dil= input("Lutfen kac sehirde konusuldugunu ogrenmek istediginiz dili giriniz(in English):")
im.execute("SELECT COUNT(city.Name) FROM city INNER JOIN countrylanguage"
           " ON city.CountryCode=countrylanguage.countrycode WHERE countrylanguage.Language = ?",(dil,))
print(im.fetchall())

# 4. Kullanıcıdan bir A bölgesi(region) ve bir B dili(language) alın. Eğer bu B dili, A bölgesindeki ülkelerin
# birinde resmi dil ise, o ülke(ler)in isim(ler)ini listeleyin. Eğer o bölgedeki hiçbir ülkede resmi
# dil değilse, "B dili A bölgesindeki hiçbir ülkede resmi dil değildir." şeklinde bir output verin.
# (A ve B kullanıcı inputu olacaktır.)
bolge = input("Lutfen bir bolge giriniz:")
dil = input("Lutfen bir dil giriniz:")
im.execute("SELECT country.Name FROM countrylanguage INNER JOIN country ON countrylanguage.countryCode=country.Code "
           "WHERE countrylanguage.IsOfficial = 'T' AND country.Region = ? "
           "AND countrylanguage.language= ?",(bolge,dil,))
veri = im.fetchall()
if veri == []:
    print("{} dili {} bolgesindeki hicbir ulkede resmi dil degildir.".format(dil,bolge))
else:
    print(veri)

# 5. Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı ile birlikte bulunuz. (Bazı dillerin bir kıtada birden
#  fazla ülkede konuşulduğunu unutmayın ve bunu dikkate alarak bir dili birden fazla kez hesaplamayın.)
continents = ['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Oceania', 'Antarctica']
for i in continents:
    im.execute("SELECT COUNT(DISTINCT countrylanguage.language) FROM countrylanguage INNER JOIN country "
               "ON countrylanguage.CountryCode=country.Code WHERE country.continent= ?", (i,))
    print(i, *im.fetchall())
