sayı = 0
for i in range(999,99,-1):
    for j in range(999,99,-1):
        çarpma = i * j
        if str(çarpma) == str(çarpma)[::-1]:
            if çarpma > sayı:
                sayı = çarpma
print(sayı)
