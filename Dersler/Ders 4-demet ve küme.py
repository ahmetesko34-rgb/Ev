# DEMET (TUPLE) VE KÜME (SET) ÖZETİ

# -------------------
# TUPLE (DEMET)
# -------------------

# tuple = değiştirilemeyen liste (immutable)

demet = (1, 2, 3, 4)
print(demet)
print(type(demet))  # tuple


# tek elemanlı tuple

tek = (5,)  # virgül önemli!
print(type(tek))


# index ile erişim

print(demet[0])  # 1
print(demet[-1]) # 4


# slicing

print(demet[1:3])  # (2, 3)


# tuple değiştirilemez ❌

# demet[0] = 10  # hata verir


# tuple birleştirme

a = (1, 2)
b = (3, 4)

print(a + b)  # (1, 2, 3, 4)


# tuple uzunluk

print(len(demet))


# tuple içinde arama

print(2 in demet)  # True


# -------------------
# SET (KÜME)
# -------------------

# set = sırasız, tekrar etmeyen veri yapısı

kume = {1, 2, 3, 3, 4}
print(kume)  # tekrar eden silinir


# boş set

bos = set()
print(type(bos))  # set


# set'e eleman ekleme

kume.add(5)
print(kume)


# eleman silme

kume.remove(2)  # varsa siler
print(kume)

kume.discard(10)  # yoksa hata vermez


# set uzunluk

print(len(kume))


# set içinde kontrol

print(3 in kume)  # True


# -------------------
# KÜME İŞLEMLERİ
# -------------------

a = {1, 2, 3}
b = {3, 4, 5}

# birleşim (union)
print(a | b)  # {1,2,3,4,5}

# kesişim (intersection)
print(a & b)  # {3}

# fark (difference)
print(a - b)  # {1,2}

# ters fark
print(b - a)  # {4,5}


# -------------------
# ÖNEMLİ FARKLAR
# -------------------

# tuple:
# ✔️ sıralı
# ✔️ değiştirilemez
# ✔️ index var

# set:
# ❌ sırasız
# ❌ index yok
# ✔️ tekrar eden yok
# ✔️ hızlı arama


# -------------------
# KULLANIM
# -------------------

# tuple → sabit veriler
koordinat = (10, 20)

# set → tekrarları silmek
liste = [1, 2, 2, 3]
kume = set(liste)
print(kume)  # {1,2,3}