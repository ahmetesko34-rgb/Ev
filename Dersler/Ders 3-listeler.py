# LİSTELER (LIST) ÖZETİ

# liste = birden fazla veriyi tek yerde tutar
# köşeli parantez [] kullanılır

liste = [1, 2, 3, 4]
print(liste)
print(type(liste))  # list


# farklı türde veri tutabilir

karisik = [1, "Ahmet", 3.14, True]
print(karisik)


# index (eleman alma)
# 0'dan başlar

meyveler = ["elma", "armut", "muz"]

print(meyveler[0])  # elma
print(meyveler[1])  # armut


# sondan alma

print(meyveler[-1])  # muz
print(meyveler[-2])  # armut


# liste değiştirme

meyveler[0] = "çilek"
print(meyveler)


# slicing (parçalama)

sayilar = [10, 20, 30, 40, 50]

print(sayilar[0:3])  # [10, 20, 30]
print(sayilar[2:])   # [30, 40, 50]
print(sayilar[:3])   # [10, 20, 30]


# listeye eleman ekleme

liste = [1, 2, 3]

liste.append(4)  # sona ekler
print(liste)


# araya ekleme

liste.insert(1, 99)  # index 1'e 99 ekler
print(liste)


# eleman silme

liste.remove(99)  # değere göre siler
print(liste)

liste.pop()  # sondan siler
print(liste)

liste.pop(0)  # indexe göre siler
print(liste)


# uzunluk bulma

liste = [1, 2, 3, 4]
print(len(liste))


# eleman var mı kontrol

print(2 in liste)   # True
print(10 in liste)  # False


# listeyi sıralama

sayilar = [5, 2, 9, 1]

sayilar.sort()
print(sayilar)  # küçükten büyüğe

sayilar.sort(reverse=True)
print(sayilar)  # büyükten küçüğe


# listeyi ters çevirme

sayilar.reverse()
print(sayilar)


# liste kopyalama

liste1 = [1, 2, 3]
liste2 = liste1.copy()

liste2.append(4)

print(liste1)
print(liste2)


# listeyi temizleme

liste = [1, 2, 3]
liste.clear()
print(liste)  # []


# liste birleştirme

a = [1, 2]
b = [3, 4]

print(a + b)  # [1, 2, 3, 4]


# liste içinde döngü (temel)

liste = [10, 20, 30]

for i in liste:
    print(i)


# önemli not:
# listeler DEĞİŞTİRİLEBİLİR (mutable)

liste = [1, 2, 3]
liste[0] = 100
print(liste)  # değişir ✔️