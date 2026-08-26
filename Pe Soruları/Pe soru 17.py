from num2words import num2words
toplam = 0
for i in range(1,1001):
    i = num2words(i)
    i = str(i)
    print(i)
    for j in i:
        if j == ' ' or j == '-':
            continue
        else:
            toplam += 1
print(toplam)
