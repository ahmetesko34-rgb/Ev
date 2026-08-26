#Pozitif Bölen bulma (ilk hatasız, yardımsız yaptığım kod)
sayı = int(input('Kaç tane pozitif tam böleni olduğunu bulmak istediğiniz sayıyı giriniz: '))
liste = []
for i in range(1,sayı + 1):
    if sayı % i == 0:
        liste.append(i)
print(f'{sayı} sayısının {len(liste)} tane böleni vardır.')
istek = (input('Bu bölenlerin hangi sayılar olduğunu öğrenmek istermisiniz. İstiyorsanız: Evet, İstemiyorsanız: Hayır giriniz: '))
if istek == 'Evet':
    print(liste)
elif istek == 'Hayır':
    print('Bizi tercih ettiğiniz için teşekkürler!')





