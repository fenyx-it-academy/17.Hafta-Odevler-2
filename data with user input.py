import sqlite3 as sq

datab = sq.connect("C:/Users/nazmi/OneDrive/Desktop/pycoders/17.Hafta-Odevler/world.db")

cur = datab.cursor()

print("""
Press 1 to find out capital city of a country.
Press 2 to find out languages spoken in a region.
Press 3 to find out how many cities is speak a language.
Press 4 to find out which language is spoken in a region officially.
Press 5 to find out how many languages is spoken in each continent.
Press q to quit
""")
    
while True:
    operation = input("\nPlease enter the operation number:").strip().lower()
    if operation == "1":
        cntr = input("\nPlease enter country name which you want to find its capital city:").title().strip()
        ans = cur.execute("SELECT city.name FROM country INNER JOIN city ON country.capital = city.id WHERE country.name = ?", (cntr,))
        ans = ans.fetchall()
        if len(ans) == 0:
            print("No result")
        else:
            print(f"Capital city of {cntr} is", ans[0])
            continue
    elif operation == "2":
        region = input("\nPlease enter the region name to find out the languages spoken there:").title().strip()
        ans = cur.execute("SELECT countrylanguage.Language FROM countrylanguage INNER JOIN country ON countrylanguage.CountryCode = country.Code WHERE country.Region = ?", (region,))
        ans = ans.fetchall()
        if len(ans) == 0:
            print("No result")
        for i in set(ans):
            print(i[0], end = "  ")
        continue
    elif operation == "3":
        lng = input("\nPlease enter language name to find out how many cities speaks that language:").title().strip()
        ans = cur.execute("SELECT countrylanguage.Language, count(city.name) FROM countrylanguage INNER JOIN city ON countrylanguage.CountryCode = city.CountryCode WHERE countrylanguage.Language = ?", (lng,))
        print(lng,"===>",ans.fetchone()[1])
        continue
    elif operation == "4":
        lng = input("\nPlease enter language name to find out how many country speaks that language in a region officially:").title().strip()
        region = input(f"\nPlease enter region name to find out number of country which speaks {lng} officially:").title().strip()
        ans = cur.execute("SELECT country.Name FROM countrylanguage INNER JOIN country ON countrylanguage.CountryCode = country.Code WHERE Region = ? and countrylanguage.Language = ? and countrylanguage.IsOfficial = 'T'", (region,lng))
        ans = ans.fetchall()
        if len(ans) > 0:
            for i in ans:
                print(i[0], end = "  \n")
                continue
        else:
            print(f"\n{lng} is not a official language in {region}.")
    elif operation == "5":
        ans = cur.execute("SELECT country.Continent, count(DISTINCT countrylanguage.Language) FROM country LEFT JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY Continent")
        for i in ans.fetchall():
            print(i[0],"===>",i[1])
        continue
    elif operation == "q":
        break
    else:
        print("Please enter again.")
