sayi1 = 100
sayi2 = 5

# print(f"{sayi1/sayi2}")

try:
    sonuc = sayi1 / sayi2
    print(sonuc)
except ZeroDivisionError:
    print(" bir sayı sıfıra bölünemez")
except:
    print("belirlenemeyen bir hata oluştu")
finally:
    print("tüm işlemler bitti")