import itertools
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perm = itertools.permutations(sayilar)
for i,p in enumerate(perm):
    if i == 999999:
        print(p)
        break
