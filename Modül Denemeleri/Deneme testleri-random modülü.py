#1 ile 10 arasında bir sayı üret
import random
import time
print(random.randint(1,10))
#listeden rastgele eleman seç
meyveler = ["elma", "muz", "çilek", "karpuz"]
print(random.choice(meyveler))
#0 veya 1 üret
print(random.randint(0,1))
#5 kere zar at
for i in range(1,6):
    zar = random.randint(1, 6)
    time.sleep(1)
    print(f'{i}. zar {zar} geldi')
#listeyi karıştır
sayilar = [1,2,3,4,5]
random.shuffle(sayilar)
print(sayilar)
#4 haneli sayı üret
random.randint(1000,9999)
#tahmin etme oyunu
sayi = random.randint(1,100)
tahmin = int(input("1 ile 100 arasındaki sayıyı tahmin et: "))
if tahmin < sayi:
    print(f'tahmininiz sayıdan daha küçük. sayı: {sayi} ')
elif tahmin > sayi:
    print(f'tahmininiz sayıdan daha büyük. sayı: {sayi} ')
elif tahmin == sayi:
    print('tahmininiz doğru!')





