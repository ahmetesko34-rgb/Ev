#Asalmı Değilmi (yaptım, 3 tane ipucu alarak)1
sayı = int(input('Asal olup olmadığını öğrenmek istediğiniz sayıyı giriniz: '))
asal = True
for i in range(2,sayı):
    if sayı %i == 0: asal = False
    break
if asal == True:
    print(f'{sayı} asaldır')
elif asal == False:
    print(f'{sayı} asal değildir')
