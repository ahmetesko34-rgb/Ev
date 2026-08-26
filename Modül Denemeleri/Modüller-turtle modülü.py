# ==================================================
# TURTLE MODÜLÜ (grafik çizim modülü)
# ==================================================

# Turtle:
# Python'da ekranda çizim yapmayı sağlar
# Kaplumbağa mantığıyla çalışır:
# ileri git, geri git, dön, çiz

# ==================================================
# MODÜLÜ İÇE AKTARMA
# ==================================================

import turtle

# ekran oluştur
ekran = turtle.Screen()

# kaplumbağa oluştur
kalem = turtle.Turtle()


# ==================================================
# TEMEL HAREKETLER
# ==================================================

kalem.forward(100)   # 100 birim ileri
kalem.backward(50)   # geri
kalem.right(90)      # sağa dön
kalem.left(45)       # sola dön


# ==================================================
# ŞEKİL ÇİZME
# ==================================================

# Kare
for i in range(4):
    kalem.forward(100)
    kalem.right(90)

# Üçgen
for i in range(3):
    kalem.forward(100)
    kalem.left(120)


# ==================================================
# KALEM KONTROLLERİ
# ==================================================

kalem.penup()      # çizmeyi bırak
kalem.goto(50, 50) # yeni konuma git
kalem.pendown()    # tekrar çiz

# kalınlık
kalem.pensize(5)

# renk
kalem.color("blue")


# ==================================================
# DOLGU
# ==================================================

kalem.begin_fill()
kalem.color("red")

for i in range(4):
    kalem.forward(100)
    kalem.right(90)

kalem.end_fill()


# ==================================================
# HIZ AYARI
# ==================================================

kalem.speed(1)   # yavaş
kalem.speed(10)  # hızlı


# ==================================================
# DAİRE
# ==================================================

kalem.circle(50)


# ==================================================
# YAZI YAZMA
# ==================================================

kalem.write("Merhaba", font=("Arial", 16, "bold"))


# ==================================================
# EKRAN AYARLARI
# ==================================================

ekran.bgcolor("black")   # arka plan rengi
kalem.color("white")


# ==================================================
# TIKLAYINCA KAPAT
# ==================================================

ekran.exitonclick()


# ==================================================
# KISA ÖZET
# ==================================================

# Turtle:
# grafik çizimi için kullanılır

# forward()   -> ileri
# backward()  -> geri
# right()     -> sağ
# left()      -> sol
# penup()     -> kalemi kaldır
# pendown()   -> kalemi indir
# color()     -> renk
# circle()    -> daire
# goto()      -> konum değiştir

# ==================================================
# PROJE FİKİRLERİ
# ==================================================

# - Kare / yıldız çizme
# - Spiral
# - İsim yazdırma
# - Mini oyun
# - Fraktal çizim