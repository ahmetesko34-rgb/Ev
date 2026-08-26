#faktöriyel bulma  1 ipucu ile yapıldı
sayı = int(input('Faktoriyelini bulmak istediğiniz sayıyı giriniz: '))
liste = []
for i in range(1,sayı + 1):
    liste.append(i)
sonuç = 1
for l in liste:
    sonuç*=l
print(sonuç)
