sözlük = {1: 1}
def zincirbulma(n):
    if n in sözlük:
        return sözlük[n]
    zincir = 1
    sayı = n
    while True:
        if sayı % 2 == 0:
            sayı = sayı // 2
            zincir += 1
            if sayı == 1:
                break
        else:
            sayı = sayı * 3 + 1
            zincir += 1
    return zincir
maxzincir= 0
maxsayı= 0
for i in range(1,1000000):
    uzunluk = zincirbulma(i)
    if uzunluk > maxzincir:
        maxzincir= uzunluk
        maxsayı = i
print(maxsayı, maxzincir)

