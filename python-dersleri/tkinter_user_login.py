from tkinter import *
import hashlib
import sqlite3
from tkinter import messagebox

baglanti = sqlite3.connect("hesaplamalar")
im = baglanti.cursor()

root = Tk()
root.geometry("720x480")
title = Label(text="Giriş Ekranı")
title.place(relx=.4, rely=.15)

t = 'CREATE TABLE IF NOT EXISTS kullanicilar (username VARCHAR (32), password VARCHAR (32), userID INTEGER PRIMARY KEY AUTOINCREMENT)'
im.execute(t)
baglanti.commit()


def insertToDb(username, password):
    hashedUsername = username.encode("UTF-8")
    hashedPassword = hashlib.md5(password.encode("UTF-8")).hexdigest()

    im.execute("INSERT INTO kullanicilar(username,password) VALUES (?,?)", (hashedUsername, hashedPassword))
    baglanti.commit()
    print("User Created")
    resultStr.set("Kullanıcı oluşturuldu")

def yeni_kullanici_ekleme_sayfasi():
    global resultStr
    yeniKullanici = Frame(root)
    yeniKullanici.place(relwidth=.9, relheight=.9, relx=.05, rely=.03)

    usernameLabel = Label(yeniKullanici, text="Kullanıcı Adı :")
    usernameEntry = Entry(yeniKullanici, width=30)
    usernameLabel.place(relx=.25, rely=.3)
    usernameEntry.place(relx=.37, rely=.3)

    passwordLabel = Label(yeniKullanici, text="Şifreniz :")
    passwordEntry = Entry(yeniKullanici, width=30, show="*")
    passwordLabel.place(relx=.25, rely=.35)
    passwordEntry.place(relx=.37, rely=.35)

    resultStr = StringVar()
    result = Label(yeniKullanici, textvariable=resultStr)
    result.place(relx=.45, rely=.7)

    enter = Button(yeniKullanici, text="Kayıt Ol", bg="green", fg="white", command=lambda: insertToDb(usernameEntry.get(), passwordEntry.get()))
    enter.place(relx=.40, rely=.4)

    back = Button(yeniKullanici, text="Geri Git", bg="red", fg="white", command=lambda: yeniKullanici.place_forget())
    back.place(relx=.3, rely=.4)

def auth(username, password):
    result_login = StringVar()
    resultLabel = Label(anaSayfa, textvariable=result_login)
    resultLabel.place(relx=.45, rely=.7)
    im.execute("SELECT COUNT(*) FROM kullanicilar")
    count = im.fetchall()
    if count[0][0] == 0:
        print("Databasede kullanıcı yok")
        result_login.set("Kullanıcı yok")
        return
    else:
        eslesenKadi = False
        eslesenSifre = False
        kullaniciId = 0
        hashedPassword = hashlib.md5(password.encode("UTF-8")).hexdigest()
        hashedUsername = username.encode("UTF-8")
        im.execute("SELECT * FROM kullanicilar WHERE username = ?", (hashedUsername,))
        query = im.fetchone()
        try:
            length = len(query)
        except:
            length = 0

        if length > 0:
            eslesenKadi = True
            idnum = query[2]
            if query[1] == hashedPassword:
                eslesenSifre = True
                print("Şifre Eşleşti")
                result_login.set("Kullanıcı Girişi başarılı")
                login_other(idnum)
            else:
                print("Şifre Yanlış")
                result_login.set("Kullanıcı bilgileri hatalı")
        else:
            result_login.set("Kullanıcı bilgileri hatalı")

def login_other(userId):
    anaSayfa.place_forget()
    kullaniciBilgileri = Frame(root)
    menu = Menu(kullaniciBilgileri)
    madde = Menu(menu, tearoff=False)
    madde.add_command(label="Dörtgen", command=lambda: alan_hesapla("dortgen"))
    madde.add_command(label="Üçgen", command=lambda: alan_hesapla("ucgen"))
    madde.add_command(label="Beşgen", command=lambda: alan_hesapla("besgen"))
    menu.add_cascade(label="Alan Hesapla", menu=madde)
    root.config(menu=menu)
    kullaniciBilgileri.place(relwidth=.9, relheight=.9, relx=.05, rely=.03)
    kullaniciBilgileriLabel = Label(text="Kullacı ID : #{}".format(userId))
    kullaniciBilgileriLabel.place(relx=.4, rely=.4)

def alan_hesapla(type):
    newWindow = Tk()
    newWindow.title("Alan Hesaplama")
    newWindow.geometry("480x480")
    alanFrame = Frame(newWindow)
    alanFrame.place(relwidth=.9, relheight=.9, relx=.05, rely=.03)
    print(type)
    if type == "dortgen":
        uzunKenarLabel = Label(alanFrame, text="Uzun kenarı giriniz")
        uzunKenarEntry = Entry(alanFrame, width=30)
        kisaKenarLabel = Label(alanFrame, text="Kısa Kenarı Giriniz")
        kisakenarEntry = Entry(alanFrame, width=30)
        uzunKenarLabel.place(relx=.25, rely=.3)
        uzunKenarEntry.place(relx=.37, rely=.3)
        kisakenarEntry.place(relx=.37, rely=.35)
        kisaKenarLabel.place(relx=.25, rely=.35)
        hesaplaButton = Button(alanFrame, text="Hesapla", bg="blue", fg="white", command=lambda: alan_hesaplama_fonksiyonu(type, int(kisakenarEntry.get()), int(uzunKenarEntry.get())))
        hesaplaButton.place(relx=.4, rely=.45)

def alan_hesaplama_fonksiyonu(type, k1, k2):
    if type == "dortgen":
        alan = k1 * k2
        messagebox.showinfo(title="alan hesaplandı", message="Dörtgenin alanı : {}".format(alan))

anaSayfa = Frame(root)
anaSayfa.place(relwidth=.9, relheight=.9, relx=.05, rely=.03)

usernameLabel = Label(anaSayfa, text="Kullanıcı Adı :")
usernameEntry = Entry(anaSayfa, width=30)
usernameLabel.place(relx=.25, rely=.3)
usernameEntry.place(relx=.37, rely=.3)

passwordLabel = Label(anaSayfa, text="Şifreniz :")
passwordEntry = Entry(anaSayfa, width=30, show="*")
passwordLabel.place(relx=.25, rely=.35)
passwordEntry.place(relx=.37, rely=.35)

enter = Button(anaSayfa, text="Giriş", fg="blue", command=lambda: auth(usernameEntry.get(), passwordEntry.get()))
enter.place(relx=.40, rely=.4)

registerButton = Button(anaSayfa, text="Kayıt Ol", command=yeni_kullanici_ekleme_sayfasi)
registerButton.place(relx=.55, rely=.4)

root.mainloop()
