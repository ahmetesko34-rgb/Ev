# INTEGER VE FLOAT ÖZETİ

# integer (int) = tam sayılar
# örnek: -5, 0, 10, 999

sayi1 = 10
sayi2 = -3

print(sayi1)
print(type(sayi1))  # int olduğunu gösterir


# float = ondalıklı sayılar
# örnek: 3.14, -0.5, 10.0

sayi3 = 3.14
sayi4 = -2.5

print(sayi3)
print(type(sayi3))  # float olduğunu gösterir


# kullanıcıdan veri alma (input her zaman string verir)
sayi = input("Bir sayı gir: ")
print(type(sayi))  # str çıkar


# int'e çevirme
sayi = int(input("Bir tam sayı gir: "))
print(sayi)
print(type(sayi))  # artık int


# float'a çevirme
sayi = float(input("Ondalıklı sayı gir: "))
print(sayi)
print(type(sayi))  # float


# matematik işlemleri

a = 10
b = 3

print(a + b)   # toplama
print(a - b)   # çıkarma
print(a * b)   # çarpma
print(a / b)   # bölme (sonuç her zaman float olur)


# tam bölme (floor division)
print(a // b)  # sadece tam kısmı alır


# kalan bulma (mod)
print(a % b)   # kalan verir


# üs alma
print(a ** b)  # 10 üzeri 3


# int ve float birlikte kullanımı
x = 5
y = 2.0

print(x + y)   # sonuç float olur


# sayı yuvarlama
z = 3.7
print(int(z))  # 3 yapar (aşağı yuvarlar)


# string → int hatası örneği
# print(int("ahmet"))  # hata verir ❌


# doğru kullanım
print(int("5"))  # çalışır ✔️