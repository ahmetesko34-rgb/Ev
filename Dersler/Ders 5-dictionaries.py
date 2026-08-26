# SÖZLÜKLER (DICTIONARY) ÖZETİ

# sözlük = anahtar (key) : değer (value) yapısı
# süslü parantez {} kullanılır

sozluk = {
    "isim": "Ahmet",
    "yas": 14,
    "sehir": "İstanbul"
}

print(sozluk)
print(type(sozluk))  # dict


# -------------------
# ELEMANA ERİŞİM
# -------------------

print(sozluk["isim"])  # Ahmet

# get ile erişim (daha güvenli)
print(sozluk.get("yas"))


# -------------------
# DEĞİŞTİRME
# -------------------

sozluk["yas"] = 15
print(sozluk)


# -------------------
# YENİ ELEMAN EKLEME
# -------------------

sozluk["okul"] = "Ortaokul"
print(sozluk)


# -------------------
# ELEMAN SİLME
# -------------------

sozluk.pop("sehir")  # anahtara göre siler
print(sozluk)

# son elemanı siler
sozluk.popitem()
print(sozluk)


# -------------------
# UZUNLUK
# -------------------

print(len(sozluk))


# -------------------
# ANAHTAR / DEĞERLERİ ALMA
# -------------------

print(sozluk.keys())    # sadece anahtarlar
print(sozluk.values())  # sadece değerler
print(sozluk.items())   # ikisi birlikte


# -------------------
# VAR MI KONTROL
# -------------------

print("isim" in sozluk)  # True


# -------------------
# DÖNGÜ İLE GEZME
# -------------------

for anahtar in sozluk:
    print(anahtar, sozluk[anahtar])


# items ile daha temiz

for k, v in sozluk.items():
    print(k, v)


# -------------------
# KOPYALAMA
# -------------------

yeni = sozluk.copy()
print(yeni)


# -------------------
# TEMİZLEME
# -------------------

sozluk.clear()
print(sozluk)  # {}


# -------------------
# İÇ İÇE SÖZLÜK
# -------------------

ogrenciler = {
    "ogr1": {"isim": "Ahmet", "yas": 14},
    "ogr2": {"isim": "Mehmet", "yas": 15}
}

print(ogrenciler["ogr1"]["isim"])  # Ahmet


# -------------------
# ÖNEMLİ NOTLAR
# -------------------

# ✔️ key (anahtar) benzersiz olmalı
# ✔️ key string, int vb olabilir
# ✔️ value her şey olabilir
# ✔️ sözlükler değiştirilebilir (mutable)
