for a in range (1,1000):
    for b in range (a+1,1000):
        c = 1000-a-b
        if c ** 2 == a**2 + b**2:
            if a+b+c==1000:
                sayı = a*b*c
                print(sayı)