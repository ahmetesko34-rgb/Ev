
sayı = 2
liste = []
while True:
    asal = True
    for i in range(2,int(sayı ** 0.5)+ 1):
        if sayı % i == 0:
            asal = False
            break
    if asal == True:
        liste.append(sayı)
        if len(liste) == 10001:
            break
    sayı +=1
print(liste[10000])


