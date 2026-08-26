toplam1 = 0
for i in range(1,101):
    toplam1 += i
toplamınınkaresi = toplam1 ** 2
toplam2 = 0
for i in range(1,101):
    toplam2 += i ** 2
print(f'{toplamınınkaresi -  toplam2}')