from tkinter import *

pencere = Tk()

def giris_yap():
    yazi = entry.get()
    if yazi == "python":
        label.config(text="Giriş yapıldı")
        entry.destroy()
        button.destroy()
    else:
        label.config(text="Giriş yapılamadı")

label = Label(pencere)
label.config(text="Şifrenizi giriniz", font=("Arial", 16))
label.place(x=10, y=10)

entry = Entry(pencere)
entry.place(x=10, y=50)

button = Button(pencere)
button.config(text="Giriş Yap", bg="green", fg="white", command=giris_yap)
button.place(x=10, y=90)

mainloop()