"""
print fonksiyonu
print end parametresi,
print sep parametresi,
print * parametresi,
print escape karakteri,
print format,
input veri almak,
input alınan veriyi yazdırmak
"""

print("merhaba dünya")

print("merhaba ", end="dünya")
print("merhaba", "dünya", sep=" ")
print(*"merhaba dünya", sep=" ")
print("merhaba arkadaşlar bugün \"input ve print \" fonksiyonlarını inceleyeceğiz")
print("merhaba arkadaşlar bugün \ninput ve print \n fonksiyonlarını inceleyeceğiz")
str = "Merhaba {}"
print(str.format("celalettin"))

isim = input("isim giriniz : ")
print("hoş geldiniz ", end=isim)