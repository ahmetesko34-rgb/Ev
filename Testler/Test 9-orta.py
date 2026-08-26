#ilk 10000 asal sayının kaç tanesi 3 ile başlar 7 ile biter(yapıldı +10 yardım)
liste = []
sayı = 3
liste.append(2)
sayı = int(sayı)
while True:
    asal = True
    for i in range(2,int(sayı**0.5) +1):
        if sayı % i == 0:
            asal = False
            break
    if asal == True:
        liste.append(sayı)
        if len(liste) == 10000:
            break
    sayı += 1
liste37 = []
for asal in liste:
    strasal = str(asal)
    if strasal.startswith("3") and strasal.endswith("7"):
        liste37.append(strasal)
print(liste37)
print(len(liste37))












