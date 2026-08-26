#turtle ile 100 birim ileri git
import turtle
import random
ekran = turtle.Screen()
kalem = turtle.Turtle()
kalem.forward(100)
kalem.clear()
kalem.penup()
kalem.goto(0, 0)
kalem.pendown()
#kare çiz
for i in range(4):
    kalem.forward(100)
    kalem.left(90)
kalem.clear()
kalem.penup()
kalem.goto(0, 0)
kalem.pendown()
#üçgen çiz
for i in range(3):
    kalem.forward(100)
    kalem.left(120)
kalem.clear()
kalem.penup()
kalem.goto(0, 0)
kalem.pendown()
#kaldır, bi yere git , indir
kalem.penup()
kalem.goto(100, 100)
kalem.pendown()
kalem.forward(100)
kalem.clear()
kalem.penup()
kalem.goto(0, 0)
kalem.pendown()
#5 farklı renkte çiz
renklistesi = ['purple','red','blue','gray','green']
for i in renklistesi:
    kalem.pencolor(i)
    kalem.forward(100)
    kalem.left(90)
kalem.clear()
kalem.penup()
kalem.goto(0, 0)
kalem.pendown()
#yıldız çizimi
for i in range(5):
    kalem.forward(100)
    kalem.left(144)
kalem.clear()
kalem.penup()
kalem.goto(0, 0)
kalem.pendown()
#spiral desen
x = 10
while True:
    kalem.forward(x)
    kalem.left(90)
    kalem.speed(x)
    x += 10
    if x > 1000:
        break
kalem.clear()
kalem.penup()
kalem.goto(0, 0)
kalem.pendown()
#random renkte spiral
renklistesi = ['purple','red','blue','gray','green']
y = 10
z = 1
while True:
    renk = random.choice(renklistesi)
    kalem.pencolor(renk)
    kalem.forward(y)
    kalem.left(90)
    kalem.speed(z)
    y += 10
    z += 1
    if y == 1000:
        break
kalem.clear()
kalem.penup()
kalem.goto(0, 0)
kalem.pendown()
#kalem rastgele yerlere çizim yapsın
def kare():
    for i in range(4):
        kalem.forward(30)
        kalem.left(90)
def ucgen():
    for i in range(3):
        kalem.forward(30)
        kalem.left(120)
def yildiz():
    for i in range(5):
        kalem.forward(30)
        kalem.left(144)
cizimsayisi = 0
list = [kare,ucgen,yildiz]
while cizimsayisi < 10:
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    cizim = random.choice(list)
    kalem.penup()
    kalem.goto(x, y)
    kalem.pendown()
    cizim()
    cizimsayisi += 1







turtle.done()