import sqlite3
vt=sqlite3.connect('world.db')
im=vt.cursor()
kullanici_bilgi="""
1. X ülkesinin başkenti neresidir? (X kullanıcı inputu olacaktır)
2. Y bölgesinde konuşulan tüm dilleri listeleyin.
3. Z dilinin konuşulduğu şehirlerin sayısını bulunuz. 
4. Kullanıcıdan bir A bölgesi(region) ve bir B dili(language) alın. 
5. Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı ile birlikte bulunuz.
6. Cikis icin 'q' seciniz..."""
print(kullanici_bilgi)

while True:
    kullanici_secimi= input("Secim numaralarini giriniz: ")
    if kullanici_secimi=="1":
      try:
        ulke=input("Baskentini ogrenmek istediginiz ulkeyi giriniz: ")
        im.execute("select Capital from country where Name= ?",(ulke,))
        ulke=im.fetchone()[0]
        im.execute("select Name from city where ID = ?",(ulke,))
        sonuc=im.fetchone()[0]
        print(sonuc)
      except:
        print("Boyle bir ulke bulunamadi...")
        continue

    elif kullanici_secimi=="2":
      
      bolge=input("Dillerini ogrenmek istediginiz bolgeyi giriniz: ")
      im.execute("select DISTINCT countrylanguage.Language from country,countrylanguage where country.Region=? and countrylanguage.CountryCode=country.Code",(bolge,))
      ulke=im.fetchall()
      if len(ulke)==0:
        print("Boyle bir bolge bulunamadi...")
        continue
      else:
        print(bolge,"Bolgesinde Konusulan Diller")
        for i in ulke:
          print(i[0])
        
    elif kullanici_secimi=="3":
      
      dil=input("Ogrenmek istediginiz dili giriniz: ")
      im.execute("SELECT count(city.Name) from city,countrylanguage where city.CountryCode=countrylanguage.CountryCode and countrylanguage.Language= ? " ,(dil,))
      dilsayisi = im.fetchone()[0]
      print(dil,"Konusulan Sehir Sayisi: ",dilsayisi)
        
    elif kullanici_secimi=="4":
      bolge= input("Bolge ismi giriniz: ")
      dil= input("Dil ismi giriniz: ")
      im.execute("select country.Name from country,countrylanguage where country.Region= ? and country.Code=countrylanguage.CountryCode and countrylanguage.Language= ? and countrylanguage.IsOfficial='T'",(bolge,dil,))
      ulkeler=im.fetchall()
      if len(ulkeler)>0:
        print(dil,"Dili",bolge,"Bolgesinde Resmi Olarak Konusulan Ulkeler")
        for i in ulkeler:
          print(i[0])
      else:
        print(dil, "dili", bolge, "bölgesindeki hiçbir ülkede resmi dil değildir.")

    elif kullanici_secimi=="5":
      
      print("Tum Kitalarda Konusulan Dil Sayisi")
      im.execute("select  country.Continent,count(DISTINCT countrylanguage.Language) from country,countrylanguage where countrylanguage.CountryCode=country.Code group by country.Continent")
      sonuc=im.fetchall()
      for i in sonuc:
        print(i[0],i[1])
    elif kullanici_secimi=="6":
      print("Cikis yapiliyor..")
      break
