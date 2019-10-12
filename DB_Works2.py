import sqlite3 as sql

conn = sql.connect("/Users/HTunctepe/PycharmProjects/PyCoders/17.Hafta Odevler/17.Hafta-Odevler/world.db")
cur = conn.cursor()
country = ''
language = ''

message = """
Press 1 to see the capital of a country\n
Press 2 to see the languages spoken in a region\n
Press 3 to see the number of cities in which a language is spoken\n
Press 4 to see if a language you choose is spoken in a region you select
        and if so to see the countries the language is spoken\n
Press 5 to see all the continents and the number of languages spoken in each continent\n
Press 'q' to exit the program"""
print(message)
while True:
    choice = input("\n\nPlease select a choice from the menu: ")

    if choice == "1":
        country = input("\nEnter the country of which you want to see the capital: ").title()

        cur.execute("SELECT city.Name FROM city, country "
                    "WHERE country.Name = ? "
                    "AND city.ID = country.Capital;", (country,))
        data1 = cur.fetchall()[0]
        print(*data1)

    elif choice == "2":
        country = input("\nEnter the country name to see which languages are spoken: ").capitalize()

        cur.execute("SELECT Language FROM countrylanguage "
                   "INNER JOIN country on country.Code = countrylanguage.CountryCode "
                   "WHERE country.Name = ?", (country,))
        data2 = cur.fetchall()
        for i in data2:
            print(i[0], end=', ')

    elif choice == "3":
        language = input("\nEnter a language to see the count of cities in which the language is spoken: ").title()
        cur.execute("SELECT Count(city.Name) FROM city "
                   "INNER JOIN countrylanguage on countrylanguage.CountryCode = city.CountryCode "
                   "WHERE countrylanguage.Language = ?", (language,))
        no_of_cities = cur.fetchall()[0]
        print(language, 'language is spoken in ', *no_of_cities, "cities.")

    elif choice == "4":
        region = input("\nEnter a region: ").title()
        language = input("\nEnter a language to see if the language is spoken in that "
                         "\nregion and the countries in which the language is spoken: ").title()
        cur.execute("SELECT country.Name FROM country, countrylanguage "
                   "WHERE country.Region = ? "
                   "AND country.Code = countrylanguage.CountryCode "
                   "AND countrylanguage.Language = ? "
                   "AND countrylanguage.IsOfficial ='T'", (region, language,))

        countries = cur.fetchall()
        if len(countries) == 0:
            print("Bu dil bu bolgede resmi dil degil.")
        else:
            print('\nThe countries in which',language, 'language is spoken as an official language: ')
            for i in countries:
                print(i[0], end=', ')



    elif choice == "5":
        cur.execute("SELECT country.Continent, COUNT(DISTINCT countrylanguage.Language) "
                   "AS No_Of_Lang_Spoken FROM country "
                   "INNER JOIN countrylanguage "
                   "ON countrylanguage.CountryCode = country.Code "
                   "GROUP BY country.Continent")
        continents = '';
        no_of_lang = 0
        print("""
     Continent      No Of Languages Spoken
----------------    ----------------------""")

        for i in cur.fetchall():
            continents = i[0]
            no_of_lang = i[1]
            print(str(continents).ljust(28), str(no_of_lang))

    elif choice.lower() == "q":
        print("\nExiting the program...")
        exit()
