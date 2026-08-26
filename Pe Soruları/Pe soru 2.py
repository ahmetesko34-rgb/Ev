liste = []
liste.append(1)
liste.append(1)
index = 2
while True:
    sayı = (liste[index - 1] + liste[index - 2])
    if sayı > 4000000 :
        break
    else:
        liste.append(sayı)
    index += 1
newliste = []
for i in liste :
    if i % 2 == 0 :
        newliste.append(i)
print(sum(newliste))




