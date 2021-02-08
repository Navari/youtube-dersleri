import random

sayilar = []

maksimum = 20

print(random.randrange(1,maksimum))

for i in range(10):
    sayi = random.randrange(1, maksimum)
    while sayi in sayilar:
        print("aynı değer var")
        sayi = random.randrange(1, maksimum)
    sayilar += [sayi]

print(sayilar)