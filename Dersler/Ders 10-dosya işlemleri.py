# ---------------- PYTHON DOSYA İŞLEMLERİ ----------------

# Dosya işlemleri:
# Dosya oluşturma, okuma, yazma, silme vb.

# open() fonksiyonu ile dosya açılır


# ---------------- DOSYA AÇMA ----------------

# open(dosya_adi, mod)

# modlar:
# "r"  -> oku
# "w"  -> yaz (eskiyi siler)
# "a"  -> sona ekle
# "x"  -> yeni dosya oluştur
# "rb" -> binary oku


# ---------------- DOSYA OKUMA ----------------

dosya = open("test.txt", "r")

icerik = dosya.read()

print(icerik)

dosya.close()

# ⚠️ close unutulmamalı


# ---------------- SATIR SATIR OKUMA ----------------

dosya = open("test.txt", "r")

print(dosya.readline())   # ilk satır
print(dosya.readline())   # ikinci satır

dosya.close()


# ---------------- TÜM SATIRLARI LİSTEYE ALMA ----------------

dosya = open("test.txt", "r")

satirlar = dosya.readlines()

print(satirlar)

dosya.close()


# ---------------- DOSYAYA YAZMA ----------------

dosya = open("test.txt", "w")

dosya.write("Merhaba")

dosya.close()

# ⚠️ "w" eski içeriği siler


# ---------------- DOSYANIN SONUNA EKLEME ----------------

dosya = open("test.txt", "a")

dosya.write("\nYeni satır")

dosya.close()


# ---------------- DOSYA OLUŞTURMA ----------------

dosya = open("yeni.txt", "x")

dosya.close()

# ⚠️ dosya varsa hata verir


# ---------------- WITH KULLANIMI ----------------

# En güvenli yöntem budur

with open("test.txt", "r") as dosya:
    print(dosya.read())

# otomatik close olur


# ---------------- DOSYA VAR MI KONTROLÜ ----------------

import os

if os.path.exists("test.txt"):
    print("Dosya var")
else:
    print("Dosya yok")


# ---------------- DOSYA SİLME ----------------

import os

os.remove("test.txt")


# ---------------- KLASÖR OLUŞTURMA ----------------

import os

os.mkdir("deneme")


# ---------------- KLASÖR SİLME ----------------

import os

os.rmdir("deneme")


# ---------------- ÖNEMLİ NOTLAR ----------------

# read()       -> tamamını okur
# readline()   -> tek satır okur
# readlines()  -> liste şeklinde alır

# w -> sıfırlar
# a -> ekler
# r -> okur

# with open() kullanmak daha iyidir