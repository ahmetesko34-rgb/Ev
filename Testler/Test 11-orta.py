#İlk 100 fibonacci sayısı(hatasız 1 ipucuyla yapıldı)

liste = []
liste.append(1)
liste.append(1)
for i in range(2,100):
    liste.append(liste[i-1]+liste[i-2])
print(liste)