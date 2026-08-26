#gerçek pe sorusu değil ama aynısı diyebiliriz sadece liste daha kısa
names = ["ZOE","ALICE","BOB","CHARLIE","DAVID","EMMA","FRANK","GRACE","HELEN","IAN"]
names.sort()
x = 0
toplam = 0
while True:
    puanlarıntoplamı = 0
    sıra = x+1
    for i in names[0 + x]:
        puan = ord(i) - 64
        puanlarıntoplamı += puan
    toplam += puanlarıntoplamı*sıra
    x += 1
    if x == 10:
        break
print(toplam)


