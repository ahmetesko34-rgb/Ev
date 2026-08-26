import random
import time
while True:
    tercih = input('oyun seviyesini seç; Kolay(1,50):K, Orta(1,100):O, Zor(1,500):Z ').upper()
    if tercih == 'K':
        sayi = random.randint(1, 50)
        a = ('1,50')
    elif tercih == 'O':
        sayi = random.randint(1, 100)
        a = ('1,100')
    elif tercih == 'Z':
        sayi = random.randint(1, 500)
        a = ('1,500')
    else:
        print('geçersiz işlem, lütfen kodu tekrar başlatın.')
        break
    mesaj = ['zor sayı tuttum, bilebilirsen bil', 'işin çok zor', 'şanslı günündesin sayı kolay', 'bol şans!']
    tahminmesaji = ['İlk denemen!', 'İkinci denemen,', 'Üçüncü denemen, yakında deneme hakkın biticek,',
                    'Dördüncü denemen ve son 2 hakkın kaldı,', 'Buda son hakkın,']
    tahminsayisi = 1
    b = 0
    while True:
        time.sleep(1)
        if tahminsayisi == 6:
            print(f'oyunu kaybettin sayı:{sayi}')
            tekraristeği = input('tekrar oynamak istermisin? Evet:E, Hayır:H ').upper()
            break
        puan = max(0, 100 - (tahminsayisi - 1) * 20)
        randommesaj = random.choice(mesaj)
        if tahminsayisi == 1:
            tahmin = input(f'{tahminmesaji[b]} {a} arasındaki sayıyı tahmin et, {randommesaj}: ')
        elif tahminsayisi > 1:
            tahmin = input(f'{tahminmesaji[b]} sayıyı tahmin et: ')
        tahmin = int(tahmin)
        if tahmin < sayi:
            print('tahminin, sayıdan daha küçük')
        elif tahmin > sayi:
            print('tahminin sayıdan daha büyük')
        else:
            print(f'tahminin doğru! oyunu kazandın. tahmin sayın:{tahminsayisi}  puanın:{puan}')
            tekraristeği = input('tekrar oynamak istermisin? Evet:E, Hayır:H ').upper()
            break
        b += 1
        tahminsayisi += 1
    if tekraristeği == 'E':
        continue
    elif tekraristeği == 'H':
        break




