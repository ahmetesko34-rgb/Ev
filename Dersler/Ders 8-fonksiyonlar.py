# ---------------- FONKSİYONLAR (FUNCTIONS) ----------------

# Fonksiyon: Belirli bir işi yapan kod bloğu
# Amaç: Kod tekrarını azaltmak

# ---------------- TEMEL KULLANIM ----------------

def selam_ver():
    print("Merhaba")  # fonksiyon içindeki işlem


selam_ver()  # fonksiyonu çağırma


# ---------------- PARAMETRE (DIŞARIDAN VERİ ALMA) ----------------

def selam_ver(isim):
    print("Merhaba", isim)  # parametre kullanımı


selam_ver("Ahmet")


# ---------------- RETURN (GERİ DEĞER DÖNDÜRME) ----------------

def topla(a, b):
    return a + b  # sonucu geri döndürür


sonuc = topla(3, 5)
print(sonuc)


# print vs return farkı

def a():
    print(5)  # sadece ekrana yazdırır


def b():
    return 5  # değeri dışarı verir


print(a())  # None döner
print(b())  # 5 döner


# ---------------- BİRDEN FAZLA PARAMETRE ----------------

def carp(a, b):
    return a * b


print(carp(4, 5))


# ---------------- DEFAULT PARAMETRE ----------------

def selam(isim="Misafir"):
    print("Merhaba", isim)


selam()  # Misafir
selam("Ahmet")  # Ahmet

# ---------------- GLOBAL / LOCAL ----------------

x = 10  # global değişken


def deneme():
    x = 5  # local değişken
    print(x)


deneme()  # 5
print(x)  # 10


# ---------------- FONKSİYON İÇİNDE FONKSİYON ----------------

def dis():
    def ic():
        print("İç fonksiyon")

    ic()


dis()


# ---------------- BOŞ FONKSİYON ----------------

def bos():
    pass  # hata vermesin diye boş bırakılır


# ---------------- ÖRNEK (ASAL KONTROL) ----------------

def asal_mi(sayi):
    if sayi < 2:
        return False

    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False

    return True


print(asal_mi(7))  # True

# ---------------- KISA ÖZET ----------------

# def -> fonksiyon oluşturur
# parametre -> veri alır
# return -> veri döndürür
# fonksiyonlar kodu düzenler ve kısaltır