import sqlite3 as sql

data = sql.connect("world.db")
cursor = data.cursor()

def CapitalCountry():
    capital = input("Baskentini Ogrenmek istediginiz Ulke ismini giriniz : ").capitalize()
    cursor.execute("""SELECT country.Name, city.Name FROM city, country WHERE country.Name = ? AND country.Capital = city.ID """,(capital,))
    query = cursor.fetchone()
    print("Capital of {} is {}.".format(query[0],query[1]))

def LanguageCountry():
    country_name = input("Lutfen bir ulke ismi giriniz : ").capitalize()
    cursor.execute("""SELECT countrylanguage.language FROM countrylanguage, country WHERE country.Name = ? AND country.Code = countrylanguage.CountryCode""", (country_name,))
    query = cursor.fetchall()
    for i in range(len(query)):
        print("Language {} : {} ".format(i+1,query[i][0]))

def SumCityLanguage():
    language = input("Lutfen bir dil ismi giriniz : ").capitalize()
    cursor.execute("""SELECT city.Name FROM city, countrylanguage WHERE countrylanguage.Language=? AND countrylanguage.CountryCode = city.CountryCode """, (language,))
    query = cursor.fetchall()
    print("number of cities spoken in {} : {}".format(language, len(query)))

def LanguageOffical():
    cursor.execute("""SELECT DISTINCT Region FROM country ORDER BY Region""")
    regions = cursor.fetchall()
    for i in range(len(regions)):
        print("{} -) {}".format(i+1, regions[i][0] ))
    regions_number = int(input("yukaridaki bolge isimlerindan birinin numarasini giriniz : "))

    cursor.execute("""SELECT DISTINCT Language FROM countrylanguage ORDER BY Language """)
    language = cursor.fetchall()
    for i in range(len(language)):
        print("{} -) {}".format(i + 1, language[i][0]))
    language_number = int(input("yukaridaki bolge isimlerindan birinin numarasini giriniz : "))


    cursor.execute("""SELECT country.Name, countrylanguage.Language, countrylanguage.IsOfficial 
    FROM countrylanguage, country 
    WHERE countrylanguage.Language = ? 
    AND country.Region=? 
    AND country.Code = countrylanguage.CountryCode 
    AND countrylanguage.IsOfficial="T" """
                   ,(language[language_number - 1][0],regions[regions_number-1][0],))
    sonuc = cursor.fetchall()
    if sonuc:
        for i in sonuc:
            print(i)
    else:
        print("\n {} dili {} bolgesindeki hicbir ulkede resmi dil degildir".format(language[language_number - 1][0],regions[regions_number-1][0]))

def LanguageContinent():
    cursor.execute("""SELECT country.Continent, COUNT(DISTINCT countrylanguage.Language) 
    FROM country, countrylanguage 
    WHERE country.Code = countrylanguage.CountryCode
    GROUP BY country.Continent""")
    sonuc = cursor.fetchall()
    for i in sonuc:
        print(i)

#GIRILEN ULKENIN BASKENTINI BULAN FONKSIYON
# CapitalCountry()

#GIRILEN ULKEDE KONUSULAN DILLERI BULAN FONKSIYON
# LanguageCountry()

#GIRILEN DILIN KONUSULDUGU SEHIR SAYISI
# SumCityLanguage()

#INPUT OLARAK ALINAN DILIN YINE INPUT OLARAK ALINAN BOLGEDE RESMI DIL OLUP OLMADIGINI BULAN FONKSIYON
# LanguageOffical()

#KITALARDA KONUSULAN DIL SAYISI
# LanguageContinent()

