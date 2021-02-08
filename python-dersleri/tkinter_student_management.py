from tkinter import *
import ogrenci_islemleri as sd

anaSayfa = Tk()
anaSayfa.title("..::OKUL YÖNETİMİ SİSTEMİ::..")

l1 = Label(anaSayfa, text="OKUL YÖNETİMİ SİSTEMİ", font=("Georgia", 30, "bold"))
l1.pack(padx= 100, pady= 50)

b1 = Button(anaSayfa, text="Öğrenci Ekle", activebackground="grey", command=lambda: sd.insert(), activeforeground="white", padx=200, pady=25)
b1.pack()
b2 = Button(anaSayfa, text="Öğrenciyi Güncelle", activebackground="grey", command=lambda: sd.update(), activeforeground="white", padx=185, pady=25)
b2.pack()
b3 = Button(anaSayfa, text="Öğrenci Detayına Git", activebackground="grey", command=lambda: sd.display(), activeforeground="white", padx=180, pady=25)
b3.pack()
b4 = Button(anaSayfa, text="Öğrenciyi Sil", activebackground="grey", command=lambda: sd.delete(), activeforeground="white", padx=200, pady=25)
b4.pack()
b5 = Button(anaSayfa, text="Öğrenci Ara", activebackground="grey", activeforeground="white", padx=200, pady=25)
b5.pack()

l2 = Label(anaSayfa, text="\n")
l2.pack()

anaSayfa.mainloop()
