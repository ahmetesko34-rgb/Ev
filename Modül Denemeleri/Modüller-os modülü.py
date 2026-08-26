# ==================================================
# OS MODÜLÜ (işletim sistemi işlemleri)
# ==================================================

import os

# Bulunduğun klasör
print(os.getcwd())

# Klasördeki dosyalar
print(os.listdir())

# Yeni klasör oluşturma
# os.mkdir("YeniKlasor")

# Klasör silme
# os.rmdir("YeniKlasor")

# Dosya var mı?
print(os.path.exists("dosya.txt"))

# Dosya boyutu
# print(os.path.getsize("dosya.txt"))

# Yol birleştirme
print(os.path.join("klasor", "dosya.txt"))

# Sistem komutu çalıştırma
# Windows:
# os.system("cls")

# Dosya listesi:
# os.system("dir")

# Linux/Mac:
# os.system("clear")
