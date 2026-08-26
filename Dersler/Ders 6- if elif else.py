# IF - ELIF - ELSE ÖZETİ

# if = eğer
# elif = değilse ama şuysa
# else = hiçbirisi değilse

# -------------------
# BASİT IF
# -------------------

yas = 15

if yas > 10:
    print("Büyüksün")


# -------------------
# IF - ELSE
# -------------------

yas = 8

if yas > 10:
    print("Kullanabilirsin")
else:
    print("Kullanamazsın")


# -------------------
# IF - ELIF - ELSE
# -------------------

yas = 10

if yas > 10:
    print("Kullanabilirsin")
elif yas == 10:
    print("Sınırdasın")
else:
    print("Kullanamazsın")


# -------------------
# KARŞILAŞTIRMA OPERATÖRLERİ
# -------------------

# >  büyük
# <  küçük
# >= büyük eşit
# <= küçük eşit
# == eşit mi
# != eşit değil mi


# -------------------
# AND - OR KULLANIMI
# -------------------

yas = 15
puan = 80

if yas > 10 and puan > 70:
    print("Geçtin")

if yas > 10 or puan > 70:
    print("Şartlardan biri sağlandı")


# -------------------
# INPUT İLE KULLANIM
# -------------------

yas = int(input("Yaşını gir: "))

if yas >= 18:
    print("Ehliyet alabilirsin")
else:
    print("Alamazsın")


# -------------------
# İÇ İÇE IF (NESTED)
# -------------------

yas = 20
ehliyet = True

if yas >= 18:
    if ehliyet:
        print("Araba kullanabilirsin")
    else:
        print("Ehliyetin yok")
else:
    print("Yaşın küçük")


# -------------------
# KISA IF (TEK SATIR)
# -------------------

yas = 20

print("Büyük") if yas > 18 else print("Küçük")


# -------------------
# ÖNEMLİ NOTLAR
# -------------------

# ✔️ girinti (TAB) çok önemli
# ✔️ if'ten sonra : koyulur
# ✔️ koşul True ise çalışır
# ✔️ False ise else çalışır