#100 basamaklı ilk fibonaccı sayısını bulma ( yapıldı 1 ipucu hatasız)-
liste = []
liste.append(1)
liste.append(1)
index = 2
while True:
    sayı = (liste[index-1]+liste[index-2])
    liste.append(sayı)
    geçiciliste = []
    for i in str(sayı):
        geçiciliste.append(i)
    if len(geçiciliste) == 100:
        print(sayı)
        print(len(str(sayı)))
        break
    index += 1



