import math
toplam = 0
a = 1
while True:
    bolensayisi = 0
    sayi = toplam + a
    toplam += a
    a+=1
    for i in range(1,int(math.sqrt(sayi))+ 1):
        if sayi % i == 0:
            bolensayisi += 2
    if bolensayisi > 500:
        break
print(sayi)
print(bolensayisi)

