ogrenci_adi = input("Öğrencinin adını girin: ")
yas = int(input("Öğrencinin yaşını girin: "))
sinav_puani = int(input("Öğrencinin sınav puanını girin: "))
proje_puani = int(input("Öğrencinin proje puanını girin: "))
devamsizlik = int(input("Öğrencinin devamsızlık sayısını girin: "))

if yas >= 18:
    print("Yetişkin Öğrenci")
else:
    print("Yetişkin Olmayan Öğrenci")

if sinav_puani >= 85:
    print("Çok İyi")
elif sinav_puani >= 70:
    print("İyi")
elif sinav_puani >= 50:
    print("Geçti")
else:
    print("Kaldı")

if sinav_puani >= 70 and proje_puani >= 70:
    print("Akademik Olarak Başarılı")
else:
    print("Akademik başarı şartları sağlanmadı")

if sinav_puani >= 90 or proje_puani >= 90:
    print("Üstün Performans Gösterdi")
else:
    print("Üstün Performans Şartı Sağlanmadı")

if devamsizlik <= 5:
    print("Devamsızlık Uygun")
else:
    print("Devamsızlık Fazla")

if sinav_puani >= 85:
    if devamsizlik <= 5:
        print("Takdir adayı")
    else:
        print("Notu yüksek fakat devamsızlığı fazla")