#3 basamaklı sayıların kaç tanesi rakamlarının küplerinin toplamına eşittir(tekte yardımsız doğru)
liste = []
toplam = 0
for sayı in range(100,1000):
    toplam = 0
    for i in str(sayı):
        i = int(i)
        toplam = int(toplam)
        toplam += i**3
    if toplam == sayı:
            liste.append(sayı)
    elif toplam != sayı:
        continue
print(liste)
print(len(liste))



