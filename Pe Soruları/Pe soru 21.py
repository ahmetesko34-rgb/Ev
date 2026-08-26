def d(n):
    toplam = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            toplam += i
            if i != n // i:
                toplam += n // i
    return toplam

amicable = set()

for a in range(2, 10000):
    b = d(a)
    if b != a and d(b) == a:
        amicable.add(a)
        amicable.add(b)

print(sum(amicable))
print(amicable)


