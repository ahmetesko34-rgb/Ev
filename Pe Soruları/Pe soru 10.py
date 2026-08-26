
liste = []
sayı=2
liste.append(2)
while True:
    asal = True
    for i in range(2,int(sayı**0.5)+ 1):
        if sayı % i == 0:
            asal = False
            break
    if asal:
        liste.append(sayı)
        if sayı == 2000000:
            break
    sayı+=1
print(sum(liste))
