liste = []
i = 2
while True:
    asal = True
    for a in range(2,int(i**0.5 + 1)):
        if i % a == 0:
            asal = False
            break
    if asal == True:
        if  600851475143 % int(i) == 0:
            liste.append(i)
    if i > 10000:
        break
    i = i + 1
liste.sort(reverse=True)
print(liste[0])
print(liste)














