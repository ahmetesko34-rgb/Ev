#tekte hatasız yardımsız
İlkSayı = int(input('İlk sayıyı giriniz '))
İkinciSayı = int(input('İkinci sayıyı giriniz '))
İşlem = input("""Yapacağınız işlemi giriniz.
(Toplama: +, Çıkarma: -, Çarpma: x, Bölme: /)""")

if İşlem =='+':
    print('sonuç:' +str(İlkSayı+İkinciSayı))
elif İşlem =='-':
    print('sonuç:' +str(İlkSayı-İkinciSayı))
elif İşlem =='x':
    print('sonuç:' +str(İlkSayı*İkinciSayı))
elif İşlem =='/':
    print('sonuç:' +str(İlkSayı/İkinciSayı))


