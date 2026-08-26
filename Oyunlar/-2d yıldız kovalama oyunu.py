import random
import turtle

screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("black")

#################################################################################
# OYUNCU
#################################################################################

kalem = turtle.Turtle()
kalem.color("white")
kalem.speed(0)
kalem.hideturtle()

hareket = {"w": False, "s": False, "a": False, "d": False}

x = 0
y = 0

def ciz():
    kalem.clear()

    # kafa
    kalem.penup()
    kalem.goto(x, y)
    kalem.pendown()
    kalem.setheading(0)
    kalem.circle(20)

    # burun
    kalem.penup()
    kalem.goto(x, y + 20)
    kalem.pendown()
    kalem.setheading(0)
    kalem.forward(5)
    kalem.right(135)
    kalem.forward(4)

    # ağız
    kalem.penup()
    kalem.goto(x, y + 10)
    kalem.pendown()
    kalem.setheading(0)
    kalem.forward(10)
    kalem.backward(20)

    # göz
    kalem.penup()
    kalem.goto(x + 10, y + 30)
    kalem.pendown()
    kalem.setheading(180)
    kalem.circle(4)

    kalem.penup()
    kalem.goto(x - 10, y + 30)
    kalem.pendown()
    kalem.setheading(180)
    kalem.circle(4)

    # gövde
    kalem.penup()
    kalem.goto(x, y - 2)
    kalem.pendown()
    kalem.setheading(90)
    kalem.backward(30)

    # sağ el
    kalem.penup()
    kalem.goto(x, y - 7)
    kalem.pendown()
    kalem.setheading(-10)
    kalem.forward(20)

    # sol el
    kalem.penup()
    kalem.goto(x, y - 7)
    kalem.pendown()
    kalem.setheading(190)
    kalem.forward(20)

    # sağ bacak
    kalem.penup()
    kalem.goto(x, y - 30)
    kalem.pendown()
    kalem.setheading(80)
    kalem.backward(20)

    # sol bacak
    kalem.penup()
    kalem.goto(x, y - 30)
    kalem.pendown()
    kalem.setheading(100)
    kalem.backward(20)

#################################################################################
# HAREKET
#################################################################################

def bas(event):
    hareket[event] = True

def birak(event):
    hareket[event] = False

#################################################################################
# YILDIZ
#################################################################################

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

kordix = 0
kordiy = 0

def yildiz():
    global kordix, kordiy

    t.clear()

    kordix = random.randint(-250, 250)
    kordiy = random.randint(-250, 250)

    t.penup()
    t.goto(kordix, kordiy)
    t.pendown()

    t.begin_fill()
    t.color("yellow")

    for i in range(5):
        t.forward(30)
        t.right(144)

    t.end_fill()

    screen.ontimer(yildiz, 2500)

#################################################################################
# PUAN
#################################################################################

pencil = turtle.Turtle()
pencil.speed(0)
pencil.hideturtle()

puan = 0
temas = False
cooldown = 0

#################################################################################
# OYUN LOOP
#################################################################################

def update():
    global x, y, puan, temas, cooldown

    # hareket
    if hareket["w"]:
        y += 4
    if hareket["s"]:
        y -= 4
    if hareket["a"]:
        x -= 4
    if hareket["d"]:
        x += 4

    ciz()

    # çarpışma
    dx = x - kordix
    dy = y - kordiy
    mesafe_kare = dx * dx + dy * dy

    if mesafe_kare < 25 * 25 and cooldown == 0:
        puan += 1
        cooldown = 10
        yildiz()

    if cooldown > 0:
        cooldown -= 1

    # puan yazı
    pencil.clear()
    pencil.penup()
    pencil.goto(0, 100)
    pencil.color("white")
    pencil.write(f"Puan: {puan}", font=("Arial", 16, "bold"))

    screen.update()
    screen.ontimer(update, 20)

#################################################################################
# KONTROLLER
#################################################################################

screen.listen()

screen.onkeypress(lambda: bas("w"), "w")
screen.onkeyrelease(lambda: birak("w"), "w")

screen.onkeypress(lambda: bas("s"), "s")
screen.onkeyrelease(lambda: birak("s"), "s")

screen.onkeypress(lambda: bas("a"), "a")
screen.onkeyrelease(lambda: birak("a"), "a")

screen.onkeypress(lambda: bas("d"), "d")
screen.onkeyrelease(lambda: birak("d"), "d")

#################################################################################
# BAŞLAT
#################################################################################

ciz()
yildiz()
update()

turtle.done()