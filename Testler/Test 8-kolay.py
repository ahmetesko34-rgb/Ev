metin = input('Hangi harfin kaç kere kullanıldığı hesaplamamız için bir metin giriniz: ')
sözlük = dict()
for harf in metin:
    if harf in sözlük:
        sözlük[harf] += 1
    else:
        sözlük[harf] = 1
for harf,adet in sözlük.items():
    print(f'{harf}: {adet}')