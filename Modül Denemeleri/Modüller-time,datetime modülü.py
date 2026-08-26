# ==================================================
# TIME + DATETIME MODÜLÜ
# ==================================================

import time
import datetime

# Epoch time (1970'ten beri saniye)
print(time.time())

# Programı bekletme
time.sleep(2)

# Kod çalışma süresi ölçme
baslangic = time.time()

for i in range(1000000):
    pass

bitis = time.time()
print("Geçen süre:", bitis - baslangic)

# Şu anki tarih ve saat
simdi = datetime.datetime.now()
print(simdi)

# Sadece tarih
print(datetime.date.today())

# Yıl / ay / gün
print(simdi.year)
print(simdi.month)
print(simdi.day)

# Saat / dakika / saniye
print(simdi.hour)
print(simdi.minute)
print(simdi.second)

# Özel tarih oluşturma
ozel = datetime.datetime(2026, 5, 1, 15, 30)
print(ozel)

# Tarih formatlama
print(simdi.strftime("%d/%m/%Y"))
print(simdi.strftime("%H:%M:%S"))

# Tarih farkı
yarin = simdi + datetime.timedelta(days=1)
print(yarin)
