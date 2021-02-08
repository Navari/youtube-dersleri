"""
for döngüsü,
while döngüsü
"""

for i in range(0, 10):
    print(i, end=",")

for i in range(0, 10, 2):
    print(i, end=",")

for i in range(0, 100, 5):
    print(i, end=",")

i = 0

while i < 10:
    print(i, end=",")
    i += 1


kanal = "Celalettin yılmaz python öğreniyorum kanalına hoş geldiniz"

for harf in kanal:
    print(5*harf, end="-")

turkce = "ÜĞİŞÇÖüğışçö"

for turkce_harf in turkce:
    if turkce_harf in kanal:
        print(f"türkçe karakter : {turkce_harf} var")
    else:
        print(f"türkçe karakter {turkce_harf} yok")

i = 0

for turkce_harf in turkce:
    if not turkce_harf in kanal:
        print(f"{turkce_harf} yok")
    else:
        print(f"{turkce_harf} var")

