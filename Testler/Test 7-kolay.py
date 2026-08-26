#Sayının tamkare olup olmadığını kontrol eder. doğru yaptık 1 ipuculu
sayı = int(input('Tamkare olup olmadığını kontrol ediceğiniz sayıyı giriniz: '))
sayı = sayı ** 0.5
if sayı == int(sayı):
    print('Bu tamkare bir sayıdır')
else:
    print('Bu tamkare bir sayı değildir')




