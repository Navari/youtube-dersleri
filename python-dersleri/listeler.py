"""
listeler ve for kullanımı
List
Tuple,
set,
dictionary
"""

message = "Merhaba arkadaşlar, benim adım celalettin".split()

print(message)
print(message[0])

list1 = [1, 2, 3, 4, 5, 'celalettin', True]

print(list1[0])
print(f"listenin eleman sayısı : {len(list1)}")

list1 = [1, 2, 3, 4, 5, ['merhaba', 'dünya', 6, 7],  'celalettin', True]
print(list1)
print(list1[5][0])

str = "Merhaba arkadaşlar, benim adım celalettin"
harfler = list(str)
print(harfler[5])

colors = ["blue", "red", "green", "yellow", "darkblue"]

for color in colors:
    print(color)

for i in range(len(colors)):
    print("{0} . renk : {1}".format(i + 1, colors[i]))

print("----- Menü -----")
print("1- Elbise rengim listede var mı ?")
secim = int(input("Seçiminiz: "))

if secim == 1:
    elbise_rengi = input("Elbise Renginiz : ")
    if elbise_rengi in colors:
        print("Evet elbise renginiz listede var ")
    else:
        print("Elbise renginiz listede maalesef yok")
else:
    print("seçiminiz yanlış")