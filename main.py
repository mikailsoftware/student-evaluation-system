ogrenci_adi = input("Ogrencinin adini girin: ")

yas = int(input("Ogrencinin yasini girin: "))

sinav_puani = int(input("Ogrencinin sinav puanini girin: "))

proje_puani = int(input("Ogrencinin proje puanini girin: ")) 

devamsizlik = int(input("Ogrencinin devamsizlik sayisini girin: ")) 

if yas >= 18:

    print("Yetiskin Ogrenci")

else:

    print("Yetiskin Olmayan Ogrenci")

if sinav_puani >= 85:

    print("Cok Iyi")

elif sinav_puani >= 70:

    print("Iyi") 

elif sinav_puani >= 50:

    print("Gecti")

else:

    print("Kaldi")

if sinav_puani >= 70 and proje_puani >= 70:

    print("Akademik Olarak Basarili")

else:

    print("Akademik basari sartlari saglanmadi")

if sinav_puani >= 90 or proje_puani >= 90:

    print("Ustun Performans Gosterdi")

else:

    print("Ustun Performans Sarti Saglanmadi")

if devamsizlik <= 5:

    print("Devamsizlik Uygun")

else:

    print("Devamsizlik Fazla")

if sinav_puani >= 85:

    if devamsizlik <= 5:

        print("Takdir adayi")

    else:

        print("Notu yuksek fakat devamsizligi fazla")