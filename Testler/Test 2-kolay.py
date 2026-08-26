#Sayının rakamları toplamını bulma (başka bir mantıktan gittiğimden yapamadım :/)
sayı = (input('Rakamları toplamını bulmak istediğiniz sayıyı giriniz: '))
toplam = 0
for i in sayı :
    toplam += int(i)
print(f'{toplam} ')