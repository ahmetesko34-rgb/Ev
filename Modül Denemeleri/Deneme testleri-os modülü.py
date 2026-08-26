import os
#bulunduğum klasördeki şeyleri listele
print(os.listdir())
#şu an hangi klasördeyim
print(os.getcwd())
#yeni klasör oluştur
os.mkdir("deneme")
#klasör sil
os.rmdir('deneme')
#klasör varmı yokmu
liste = []
for i in os.listdir():
    liste.append(i)
if 'deneme' in liste:
    print('Klasör var')
else:
    print('Klasör yok')
########################
klasor = "deneme"
if os.path.exists(klasor):
    print("Klasör var")
else:
    print("Klasör yok")
#bir dosyanın boyutunu yazdır
print(os.path.getsize("Deneme testleri-os modülü.py"))
#sadece .py olanları al
liste = []
for dosya in os.listdir():
    kontrol = os.path.splitext(dosya)
    if kontrol[1] == '.py':
        liste.append(dosya)
for i in liste:
    print(i)
#kullanıcının girdiği klasöre geç
#klasor2 = input('Klasör yolu gir: ')
#os.chdir(klasor2)
#print(os.getcwd())
#kaç dosya olduğunu say
print(len(os.listdir()))
#dosyaların ilk harfini büyük yapma
for dosya in os.listdir():
    os.rename(dosya,dosya.capitalize())
#dosyamı klasörmü
#isim = input('İsmini gir: ')
#if os.path.isfile(isim):
#    print('Bu bir dosyadır')
#elif os.path.isdir(isim):
#    print('Bu bir klasördür')
#else:
#    print('Bulunamadı')
#tüm .txt leri listeye ekle
liste3 = []
for dosya in os.listdir():
    if dosya.endswith(".txt"):
        liste3.append(dosya)
#klasördeki tüm dosyaların toplam boyutu
boyut = 0
for dosya in os.listdir():
    if os.path.isfile(dosya):
        boyut += os.path.getsize(dosya)
print(boyut)
#klasördeki en büyük dosya
enbuyuksize = 0
for dosya in os.listdir():
    if os.path.isfile(dosya):
        size=os.path.getsize(dosya)
        if size > enbuyuksize:
            enbuyuk = dosya
            enbuyuksize = size
print(enbuyuk)
#yedek adında bir klasör yoksa oluştur
if 'yedek' not in os.listdir():
    os.mkdir('yedek')
os.rmdir('yedek')
#Bulunduğum klasördeki tüm dosyaları numaralandırarak yazdır
a = 1
for i in os.listdir():
    print(f'{a}. {i}')
    a += 1






