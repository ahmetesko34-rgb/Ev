# ==================================================
# RANDOM MODÜLÜ (rastgele işlemler)
# ==================================================

import random

# Rastgele tam sayı
print(random.randint(1, 10))
# 1 ile 10 arasında sayı verir

# Ondalıklı rastgele sayı
print(random.random())
# 0.0 ile 1.0 arası

# Belirli listeden seçim
liste = ["Python", "Java", "C++"]
print(random.choice(liste))

# Birden fazla rastgele seçim
print(random.choices(liste, k=2))

# Listeyi karıştırma
sayilar = [1, 2, 3, 4, 5]
random.shuffle(sayilar)
print(sayilar)

# Rastgele örnek seçme
print(random.sample(sayilar, 3))

# Rastgele float aralık
print(random.uniform(1, 5))
