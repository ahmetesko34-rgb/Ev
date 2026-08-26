# ---------------- PYTHON MODÜLLER (MODULES) ----------------

# Modül: İçinde hazır fonksiyonlar / değişkenler olan dosya
# Amaç: Hazır kodları kullanmak, kodu bölmek ve düzenli yapmak

# ---------------- MODÜL İÇE AKTARMA ----------------

import math  # tüm modülü alır

print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.14...


# ---------------- BELİRLİ ŞEYİ ALMA ----------------

from math import sqrt, pi

print(sqrt(25))  # 5.0
print(pi)


# ---------------- TAKMA İSİM (ALIAS) ----------------

import math as m

print(m.sqrt(36))


# ---------------- TÜMÜNÜ ALMA (ÖNERİLMEZ) ----------------

from math import *

print(sqrt(49))

# ⚠️ neden önerilmez:
# isim çakışması olabilir


# ---------------- KENDİ MODÜLÜNÜ YAZMA ----------------

# örnek: hesap.py dosyası oluştur

# hesap.py
def topla(a, b):
    return a + b

def carp(a, b):
    return a * b

# başka dosyada kullanma:

import hesap

print(hesap.topla(3, 5))


# ---------------- MODÜL NEREDEN GELİR? ----------------

# 1. Python içinden (math, random, datetime)
# 2. Senin yazdığın
# 3. İnternetten (pip ile)

# örnek:
import random

print(random.randint(1, 10))


# ---------------- PIP (DIŞ MODÜL YÜKLEME) ----------------

# terminal / cmd:
# pip install numpy

# sonra:
# import numpy


# ---------------- __name__ KULLANIMI ----------------

# modül direkt çalıştırılırsa:
if __name__ == "__main__":
    print("Bu dosya direkt çalıştı")

# başka dosyadan import edilirse:
# bu kısım çalışmaz


# ---------------- KISA ÖZET ----------------

# import → modül ekler
# from → içinden parça alır
# as → kısaltma yapar
# modüller → hazır kod kütüphanesi