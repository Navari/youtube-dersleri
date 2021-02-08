"""
if, elif, else kullanımı
menülü bir örnek
"""

yas = int(input("Yaşınızı giriniz : "))

if yas < 20:
    print("daha gençsiniz")
elif yas < 30:
    print("orta yaşlısınız")
elif yas < 40:
    print("ömrün yarısındasınız")
else:
    print(" ölüm yakındır")

print("--- Menü ---")
print("1- Yaşa göre doğum tarihi hesaplama")
print("2- Doğum tarihine göre yaş hesaplama")

secim = int(input("Seçimiz : "))

if secim == 1:
    yas = int(input("Yaşınız : "))
    print("Doğum tarihiniz {}".format(2021 - yas))
elif secim == 2:
    dogum_tarihi = int(input("Doğum Tarihiniz :"))
    print("Yaşınız : {}".format(2021- dogum_tarihi))
else:
    print("Seçiminiz yanlış")