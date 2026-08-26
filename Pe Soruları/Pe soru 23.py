import math
sayi = 1
liste = []
while sayi < 28124:
    geciciliste = set()
    geciciliste.add(1)
    for i in range(2,int(math.sqrt(sayi)) + 1):
        if sayi % i == 0:
            geciciliste.add(i)
            i = sayi // i
            geciciliste.add(i)
    listetoplami = sum(geciciliste)
    if listetoplami > sayi:
        liste.append(sayi)
    sayi += 1
sayilarintoplami = set()
for i in liste:
    for j in liste:
        toplam = i + j
        if toplam not in sayilarintoplami:
            sayilarintoplami.add(toplam)
sonliste = []
for i in range(1,28124):
    if i in sayilarintoplami:
        continue
    else:
        sonliste.append(i)
print(sum(sonliste))





