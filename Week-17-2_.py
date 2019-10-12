import sqlite3 as sql
import time

vt = sql.connect('world.db')
cur = vt.cursor()
print("""
    1--» Find the capital city
    2--» Spoken languages in the country
    3--» Number of cities of the language
    4--» Check if the language is spoken in the regeion
    5--» See numbers of languages spoken in the continent 

    """)

while True:
    sel=input("Please type your selection: ")

    if sel == "1":
        a = input("Type country name to find for the capital city :")
        cur.execute(
                "SELECT city.name FROM country INNER JOIN city ON country.capital=city.id where country.name = ?", (a,))
        vt.commit()
        print(cur.fetchall())
    elif sel == "2":
        a = input("Type Country to find for the spoken languages :")
        cur.execute(
                "SELECT countrylanguage.language FROM country INNER JOIN countrylanguage ON country.code=countrylanguage.countrycode where country.name = ?",
                (a,))
        vt.commit()
        print(cur.fetchall())
    elif sel == "3":
       a = input("Type language to find number of cities where it is spoken :")
       cur.execute(
                "SELECT COUNT (city.name) FROM city INNER JOIN countrylanguage ON "
                "countrylanguage.countrycode=city.countrycode where countrylanguage.language = ?",
                (a,))
       vt.commit()
       print(cur.fetchall())
    elif sel == "4":
        a = input("Type Region :")
        cur.execute("Select region from country")
        vt.commit()
        d = cur.fetchall()
        b = input("Type Language:")
        cur.execute(
                "SELECT country.name FROM country INNER JOIN countrylanguage ON "
                "countrylanguage.countrycode=country.code where country.region= ? AND countrylanguage.language = ?",
                (a, b))
        vt.commit()
        a = cur.fetchall()
        if len(a) > 0:
            print(a)
        elif len(a) < 1:
                print("The language is not an official in the region")
    elif sel=="5":
        print(" Numbers of spoken languages in the continent")
        cur.execute(
            "SELECT country.Continent,COUNT(DISTINCT countrylanguage.Language) from country,countrylanguage where countrylanguage.CountryCode=country.Code group by country.Continent")
        vt.commit()
        lang = cur.fetchall()
        for i in lang:
            print(i[1], i[0])
    elif sel == "Q" or sel == "q":
        print("Prg sonlandırılıyor!..")
        time.sleep(1)
        print("görüşmek üzere...")
        break
