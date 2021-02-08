from tkinter import *
import instagram_commands as ic

root = Tk()
root.title("INSTAGRAM VERİLERİNİ KAYDETME UYGULAMASI")

l1 = Label(root, text="INSTAGRAM GİRİŞİ YAPINIZ").grid(row=0, column=0, padx=10, pady=10, columnspan=2)
l2 = Label(root, text="Instagram Kullanıcı Adınız").grid(row=1, column=0, padx=10, pady=10)
e1 = Entry(root, width=20)
e1.grid(row=1, column=1, padx=10, pady=10)
l3 = Label(root, text="Instagram Şifreniz").grid(row=2, column=0, padx=10, pady=10)
e2 = Entry(root, width=20, show="*")
e2.grid(row=2, column=1, padx=10, pady=10)
Button(root, text="Giriş Yap", bg="blue", fg="white", command=lambda: ic.login(e1.get(), e2.get())).grid(row=3, column=0, padx=10, pady=10, columnspan=2)

root.mainloop()