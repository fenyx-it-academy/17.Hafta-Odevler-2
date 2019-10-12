print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


import sqlite3 as sql

db = sql.connect("C:\\Users\\gebruiker\\PycharmProjects\\mathchi\\huiswerks\\17.Week\\17.Hafta-Odevler\\world.db")
im = db.cursor()

# 1- X ülkesinin başkenti neresidir? (X kullanıcı inputu olacaktır)

# 2-Y bölgesinde konuşulan tüm dilleri listeleyin. (Y kullanıcı inputu olacaktır)

# 3-Z dilinin konuşulduğu şehirlerin sayısını bulunuz. (Z kullanıcı inputu olacaktır)

# 4-Kullanıcıdan bir A bölgesi(region) ve bir B dili(language) alın. Eğer bu B dili,
# A bölgesindeki ülkelerin birinde resmi dil ise, o ülke(ler)in isim(ler)ini listeleyin.
# Eğer o bölgedeki hiçbir ülkede resmi dil değilse, "B dili A bölgesindeki hiçbir ülkede resmi dil değildir."
# şeklinde bir output verin. (A ve B kullanıcı inputu olacaktır.)

# 5-Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı ile birlikte bulunuz.
# (Bazı dillerin bir kıtada birden fazla ülkede konuşulduğunu unutmayın ve bunu dikkate alarak
# bir dili birden fazla kez hesaplamayın.)

greetings = """\t\t\tCOUNTRIES AND LANGUANGES\t\t\t\n
-To learn the Country of the Capital city you want to input 1,\n
-To learn the Languages of any part of the World you want to input 2,\n
-To find the number of cities in which any language is spoken 3,\n
-To learn any language of your choice, whether speaking or not in any region of your choice, input 4,\n
-To learn all continents and number of languages in the these continents, input 5,\n
-For exit input 'q'.
"""
print(greetings)

while True:
    chosen = input("Please enter a number which you want to do: ").lower()

    if chosen == "1":
        country = input("Please enter name for learn the Country of the Capital city you want to: ").capitalize()

        for i in im.execute(""" SELECT city.Name FROM city, country 
	                WHERE country.Name = ?
                    AND city.ID = country.Capital;""", (country,)):
        # data1 = im.fetchall()[0]                             # istersek bununlada gosterebiliriz ama for dongusu daha kullanisli oluyor ozellikle siralama konusunda
            print(*i)

    elif chosen == "2":
        speaking_language = input("Please enter name of country you want to see which speaking: ").capitalize()

        for i, j in enumerate(im.execute("SELECT Language FROM countrylanguage "
                   "INNER JOIN country on country.Code = countrylanguage.CountryCode "
                   "WHERE country.Name = ?", (speaking_language,)), start=1):
            # data2 = im.fetchall()
            print(i, "~", *j)

    elif chosen == "3":
        language = input("To see how many city speaking input language name: ").capitalize()
        im.execute("SELECT Count(city.Name) FROM city "
                   "INNER JOIN countrylanguage on countrylanguage.CountryCode = city.CountryCode "
                   "WHERE countrylanguage.Language = ?", (language,))
        city_number = im.fetchall()[0]
        print("It's spoken in the cities of", *city_number)

    elif chosen == "4":
        region = input("Please enter region: ").title()
        language = input("Please enter language: ").capitalize()
        for i, j in enumerate(im.execute("select distinct country.region, country.Name from country,countrylanguage "
                   "where country.Region= ? and country.Code=countrylanguage.CountryCode "
                   "and countrylanguage.Language= ? "
                   "and countrylanguage.IsOfficial='T'", (region, language,)), start=1):
        # countries = im.fetchall()
            if len(j) == 0:
                print(f"{language} language is not official language in this {region} region.")
            else:
                print(f"Officially {language} language speaking countries in the {region} region are: ", i, "~", *j)


    elif chosen == "5":
        for i, j in enumerate(im.execute("SELECT DISTINCT country.continent, COUNT(countrylanguage.Language) "
                   "FROM country, countrylanguage WHERE countrylanguage.CountryCode = country.Code GROUP BY country.continent"), start=1):
        # im.fetchall()
            print(i, "~", *j)

    elif chosen == "q":
        print("Programdan cikiliyor")
        quit()

# "SELECT country.Continent, COUNT(DISTINCT countrylanguage.Language) "
#                    "AS No_Of_Lang_Spoken FROM country "
#                    "INNER JOIN countrylanguage "
#                    "ON countrylanguage.CountryCode = country.Code "
#                    "GROUP BY country.Continent")

# "select  country.Continent,count(DISTINCT countrylanguage.Language) " \
# "from country,countrylanguage where countrylanguage.CountryCode=country.Code group by country.Continent"