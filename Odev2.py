import sqlite3 as sql
db = sql.connect('world.db')
print('Database baglandi..')

print("------------------------------------------")

im = db.cursor()


# 1. X ülkesinin başkenti neresidir? (X kullanıcı inputu olacaktır)

str = input("1.Baskentini ogrenmek istediginiz ulkeyi girin: ")

im.execute("""
            SELECT City.Name
            FROM city City
            INNER JOIN country Country
            ON City.ID = Country.Capital
            WHERE Country.Name = ?
""", (str,))

veriler = im.fetchall()
print("{} baskenti: {}".format(str, veriler[0][0]))

print("------------------------------------------")

# 2. Y bölgesinde konuşulan tüm dilleri listeleyin.

str = input("2.Dillerini listelemek istediginiz ulkeyi girin: ")

im.execute("""
            SELECT CL.Language
            FROM countrylanguage CL
            INNER JOIN country Country
            ON CL.countryCode = Country.Code
            WHERE Country.Name = ?
""", (str,))

veriler = im.fetchall()
for i in veriler:
    print(i[0])

print("------------------------------------------")

# 3. Z dilinin konuşulduğu ulkelerin sayısını bulunuz.

str = input("3.Konusulan toplam ulke sayisini bulmak istediginiz dil: ")

im.execute("""
            SELECT COUNT(Country.Name)
            FROM country Country
            INNER JOIN countrylanguage CL
            ON CL.countryCode = Country.Code
            WHERE CL.Language = ?
""", (str,))

veriler = im.fetchall()
print(veriler[0][0])

print("------------------------------------------")

# 4.Kullanıcıdan bir A bölgesi(region) ve bir B dili(language) alın. Eğer bu B dili,
#   A bölgesindeki ülkelerin birinde resmi dil ise, o ülke(ler)in isim(ler)ini listeleyin.
#   Eğer o bölgedeki hiçbir ülkede resmi dil değilse, "B dili A bölgesindeki hiçbir ülkede
#   resmi dil değildir." şeklinde bir output verin.

str1 = input("4-a.Bir bolge girin: ")
str2 = input("4-b.Dil girin: ")

im.execute("""
            SELECT Country.Name
            FROM country Country
            INNER JOIN countrylanguage CL
            ON CL.countryCode = Country.Code
            WHERE CL.Language = ? and Country.Region = ? and CL.isOfficial == "T"
""", (str2, str1))

veriler = im.fetchall()
if len(veriler) == 0:
    print('{} dili {} bölgesindeki hiçbir ülkede resmi dil değildir.'.format(str2,str1))
for i in veriler:
    print(i[0])

print("------------------------------------------")

# 5. Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı ile birlikte bulunuz.
#    (Bazı dillerin bir kıtada birden fazla ülkede konuşulduğunu unutmayın ve
#    bunu dikkate alarak bir dili birden fazla kez hesaplamayın.)


im.execute("""
            SELECT Country.Continent, CL.language
            FROM country Country
            INNER JOIN countrylanguage CL
            ON CL.countryCode = Country.Code            
""")


veriler = im.fetchall()
ulkeler = []
for i in veriler:
    a = [i[0], i[1]]
    if a not in ulkeler:
        ulkeler.append([i[0], i[1]])
        ulkeler.sort()

diladet = []
dilulke= []
for i in ulkeler:
    if i[0] not in diladet:
        diladet.append([i[0]])

for i in diladet:
    if [i[0],diladet.count([i[0]])] not in dilulke:
        dilulke.append([i[0],diladet.count([i[0]])])

print("5.")
for i in dilulke:
   print("{} kitasinda konusulan toplam dil sayisi {}".format(i[0],i[1]))
