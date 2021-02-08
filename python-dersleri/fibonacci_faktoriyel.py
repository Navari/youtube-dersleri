a, b = 1, 1
i = 2

while i <= 20:
    a, b = b, a + b
    print(b)
    i += 1

def faktoriyel(sayi):
    f = 1
    for i in range(2, sayi + 1):
        f *= i
    return f


while True:
    sayi = int(input("Faktoriyel hesabı için sayı giriniz[Çıkış için 0] : "))
    if sayi > 0:
        print("{0}! : {1}".format(sayi, faktoriyel(sayi)))
    else:
        print("Programdan çıkılıyor")
        break