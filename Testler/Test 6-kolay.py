#5 sayının en küçüğünü ve en büyüğünü yazdırma. yardımsız doğru
liste = []
for i in range(1,6):
    sayı = int(input(f'{i}. Sayıyı giriniz '))
    liste.append(sayı)
    liste.sort()
print(liste)
a = liste[0]
b = liste[4]
print(f"En büyüğü {b}")
print(f"En küçüğü {a}")






