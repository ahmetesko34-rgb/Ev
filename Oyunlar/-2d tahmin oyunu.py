import turtle
import random
import time
kalem = turtle.Turtle()
kalem.hideturtle()
kalem.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")
pencil = turtle.Turtle()
pencil.hideturtle()
pencil.speed(0)
screen.setup(width=1000, height=1000)
# ANA MENÜ
def anamenü():
    global puan,döngü,denemesayisi,bitti,a,b
    bitti = False
    a = 1
    b = 0
    denemesayisi = 0
    puan = 100
    döngü = True
    kalem.penup()
    kalem.goto(-300, 300)
    kalem.pendown()
    kalem.color("purple")
    kalem.write("Tahmin Etme Oyunu", font=("Arial", 50, "normal"))
    renkler = ['green', 'yellow', 'red']
    zorluklar = ['Kolay', 'Orta', 'Zor']
    for i in range(3):
        kalem.color(renkler[i])
        kalem.penup()
        kalem.goto(-200, 150 - 50 * i)
        kalem.pendown()
        kalem.write(zorluklar[i], font=("Arial", 30, "bold"))
anamenü()
# OYUN EKRANI
secim = ''
sayi = 0
bitti = False
denemesayisi = 0
puan = 100
a = 1
def tiklama(x, y):
    global secim,sayi,bitti,denemesayisi,puan,yenilgi,a,b,tahmin,z
    # KOLAY
    if -200 <= x <= -80 and 150 <= y <= 200:
        secim = "Kolay"
        sayi = random.randint(1, 50)
        b = 50
        z = 10
        kalem.color('green')
        kalem.clear()
        kalem.penup()
        kalem.goto(-300, 300)
        kalem.pendown()
        kalem.write(f'Zorluk:{secim}', font=("Arial", 40, "normal"))

        pencil.color('yellow')
        pencil.penup()
        pencil.goto(50, 300)
        pencil.pendown()
        pencil.write(f'Puan:{puan}', font=("Arial", 40, "normal"))

        tahmin = int(screen.textinput("Tahmin", "1-50 arasındaki sayıyı tahmin et:"))


    # ORTA
    elif -200 <= x <= -80 and 100 <= y <= 140:
        secim = "Orta"
        sayi = random.randint(1, 100)
        b = 100
        z = 15
        kalem.color('yellow')
        kalem.clear()
        kalem.penup()
        kalem.goto(-300, 300)
        kalem.pendown()
        kalem.write(f'Zorluk:{secim}', font=("Arial", 40, "normal"))


        pencil.color('yellow')
        pencil.penup()
        pencil.goto(50, 300)
        pencil.pendown()
        pencil.write(f'Puan:{puan}', font=("Arial", 40, "normal"))
        tahmin = int(screen.textinput("Tahmin", "1-100 arasındaki sayıyı tahmin et:"))

    # ZOR
    elif -200 <= x <= -80 and 50 <= y <= 90:
        secim = "Zor"
        sayi = random.randint(1, 200)
        b = 200
        z = 20
        kalem.color('red')
        kalem.clear()
        kalem.penup()
        kalem.goto(-300, 300)
        kalem.pendown()
        kalem.write(f'Zorluk:{secim}', font=("Arial", 40, "normal"))


        pencil.color('yellow')
        pencil.penup()
        pencil.goto(50, 300)
        pencil.pendown()
        pencil.write(f'Puan:{puan}', font=("Arial", 40, "normal"))

        tahmin = int(screen.textinput("Tahmin", "1-200 arasındaki sayıyı tahmin et:"))
    puan = 100 - (denemesayisi - 1) * z
    bitti = True
    denemesayisi +=1
screen.onscreenclick(tiklama)
# Oyun Loop
döngü = True
def dongu(d):
    if döngü:
        screen.ontimer(d, 100)

def tekraroynama(p,t):
    global döngü
    if -300 <= p <= 740 and 0 <= t <= 40:
        kalem.clear()
        pencil.clear()
        anamenü()
        döngü = True
        screen.onscreenclick(tiklama)
        oyunloop()
def oyunloop():
    global bekleniyor,tahmin,kazanmak,a,b,denemesayisi,döngü
    if bitti:
        if tahmin is not None:
            if tahmin < sayi:
                a = tahmin
                kalem.penup()
                kalem.goto( -300, -denemesayisi * 50 +50)
                kalem.pendown()
                kalem.color('orange')
                kalem.write(f'{denemesayisi}. deneme, Sayı tahmininden daha büyük', font=("Arial", 30, "normal"))
                time.sleep(2)
                tahmin = int(screen.textinput('Tahmin', f'{a}-{b} arasındaki sayıyı tahmin et:'))
            elif tahmin > sayi:
                b = tahmin
                kalem.penup()
                kalem.goto( -300, -denemesayisi * 50 +50)
                kalem.pendown()
                kalem.color('orange')
                kalem.write(f'{denemesayisi}. deneme, Sayı tahmininden daha küçük', font=("Arial", 30, "normal"))
                time.sleep(2)
                tahmin = int(screen.textinput('Tahmin', f'{a}-{b} arasındaki sayıyı tahmin et:'))
            elif tahmin == sayi:
                kalem.penup()
                kalem.goto( -300, -denemesayisi * 50 +50)
                kalem.pendown()
                kalem.color('green')
                kalem.write(f'{denemesayisi}. denemede Kazandınız!', font=("Arial", 30, "normal"))
                time.sleep(3)
                döngü = False
            puan = 100 - denemesayisi * z

            pencil.clear()
            pencil.color('yellow')
            pencil.penup()
            pencil.goto(50, 300)
            pencil.pendown()
            pencil.write(f'Puan:{puan}', font=("Arial", 40, "normal"))

            # Yenilgi
            if puan <= 0:
                kalem.penup()
                kalem.goto(-300, 0)
                kalem.pendown()
                kalem.color('red')
                kalem.write('Yenildiniz', font=("Arial", 30, "normal"))
                time.sleep(3)
                döngü = False
            denemesayisi += 1
    if döngü == False:
        kalem.clear()
        pencil.clear()
        kalem.penup()
        kalem.goto(-300, 0)
        kalem.pendown()
        kalem.color('yellow')
        kalem.write('Tekrar Oynamak İstermisin?',font=("Arial", 40, "normal"))
        screen.onscreenclick(tekraroynama)

    elif döngü:
        screen.ontimer(oyunloop, 100)
oyunloop()
turtle.done()
