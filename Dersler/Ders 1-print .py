print('Hello World') #İçindeki şeyi yazar
print("Ahmet'in Kalemi") #içinde ' olan string (metin) bozulur o yüzden çift tırnak yapıyoruz
print('Ahmet\'in kalemi')  #üstteki gibi ama çift tırnak kullanmamıza gerek yok, ters slashla onu kod olarak görmezden gelebiliriz
print("""Ahmet 
Nasılsın?""") # burda 3 tane çift tırnak direk noktasından virgülüne, boşluğuna kadar her şeyi tam alır
print('Ahmetin\nevi') # burda alt kodu alt satıra taşımak yerine yani enter yerine ters slash + n aynı işlevi yapar
print('Ahmet\tevi')  # burda üstteki gibi ama t boşluk koyuyor genellikle gereksiz. t yi tab olarak algılar
mesaj = 'Merhaba'
print(mesaj) #mesaj neye eşitse aynen onu yazar
mesaj2 = 'Dünya'
print(mesaj + mesaj2) #burda ikisini birleştirir ama boşluk koymaz birleşik yazar
print(mesaj + ' ' + mesaj2) #burda aradaki yeri boşluk olarak sayar ve artık boşluklu bir yazımız olur
print(mesaj[0])  # burda mesajın yani merhaba yazısının ilk harfini alır KODLAMADA HARFLER SIFIRDAN BAŞLAR.
print(mesaj[-1]) # burdada sondan ilkini alır
print(mesaj[0:4]) #burda ilk 3 ünü yani mer'i alır 0:4 ün ilkini alır ama ikincisini almaz
print(mesaj[::4]) #burda mesajı 4 er 4 er alır yani m h ve a yı alır
print(mesaj[::-1]) #bu direk o mesajı tersten yazdırır
print(mesaj.upper())  #bu bütün mesajın harflerini büyütür
print(mesaj.lower())  #bu bütün mesajın harflerini küçültür
print(mesaj.capitalize()) #mesajın ilk kelimesinin baş harfini büyütür
print(mesaj.title())  #her kelimenin ilk harfini büyük yapar
print(mesaj.startswith('Mer')) #bu kelime mer ile başlıyomu diye kontrol eder, büyük harf küçük harf önemlidir.
print(mesaj.endswith('Mer')) #buda sonu mer ile bitiyomu diye bakar büyük harf küçük harf önemlidir
print(len(mesaj)) #bu,yazının kaç harften oluştuğunu gösterir
print(len(mesaj + mesaj2)) # bu iki yazının kaç harften oluştuğunu bulup birbiriyle toplar
print(mesaj*10) #bu 10 kere mesaj yazdırır
isim = 'Ali'       ;             yas = '20'
print('{} , {} yaşındadır'.format(isim,yas)) # burda ne olduğunu bende bilmiyorum anla işte  ali 20 yaşındadır yazıyor. sırası önemli
print(f'{isim} , {yas} dedi')  #burda f üstteki gibi çalışır ve yazan şu ali , 20 dedi.




