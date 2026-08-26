# DÖNGÜLER (LOOPS) ÖZETİ

# döngü = bir işlemi tekrar tekrar yapma

# -------------------
# WHILE DÖNGÜSÜ
# -------------------

# koşul doğru olduğu sürece çalışır

i = 1

while i <= 5:
    print(i)
    i += 1  # artırmazsan sonsuz döngü olur ❗


# sonsuz döngü örneği

# while True:
#     print("sonsuz")  # dikkatli ol!


# -------------------
# FOR DÖNGÜSÜ
# -------------------

# belirli sayıda tekrar için kullanılır

for i in range(5):
    print(i)  # 0 1 2 3 4


# başlangıç - bitiş

for i in range(1, 6):
    print(i)  # 1 2 3 4 5


# artış miktarı

for i in range(1, 10, 2):
    print(i)  # 1 3 5 7 9


# -------------------
# LİSTE İLE FOR
# -------------------

liste = [10, 20, 30]

for i in liste:
    print(i)


# -------------------
# STRING İLE FOR
# -------------------

metin = "Ahmet"

for harf in metin:
    print(harf)


# -------------------
# BREAK
# -------------------

# döngüyü tamamen durdurur

for i in range(10):
    if i == 5:
        break
    print(i)


# -------------------
# CONTINUE
# -------------------

# o turu atlar, devam eder

for i in range(5):
    if i == 2:
        continue
    print(i)


# -------------------
# ELSE (döngü ile)
# -------------------

for i in range(3):
    print(i)
else:
    print("Bitti")


# -------------------
# İÇ İÇE DÖNGÜ
# -------------------

for i in range(3):
    for j in range(2):
        print(i, j)


# -------------------
# KULLANICI İLE WHILE
# -------------------

while True:
    sifre = input("Şifre gir: ")

    if sifre == "1234":
        print("Doğru")
        break
    else:
        print("Yanlış")


# -------------------
# ÖNEMLİ NOTLAR
# -------------------

# ✔️ while → koşula bağlı
# ✔️ for → sayıya/listeye bağlı
# ✔️ break → tamamen durdurur
# ✔️ continue → o turu atlar
# ✔️ i += 1 unutursan sonsuz döngü olur ❗