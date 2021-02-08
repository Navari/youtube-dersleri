from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import sqlite3 as sql

root = Tk()
root.title("Todo Listesi")
root.geometry("400x250+500+300")

baglanti = sql.connect("todo.db")
im = baglanti.cursor()
im.execute("create table if not exists tasks (title, text)")

task = []


def cikis():
    root.destroy()


def gorev_ekle():
    yazi = e1.get()
    if len(yazi) == 0:
        messagebox.showinfo("Görev Boş", "Lütfen görevi doldurup eklemeyi deneyin")
    else:
        task.append(yazi)
        im.execute("INSERT INTO tasks values(?, ?)", (yazi, yazi))
        e1.delete(0, "end")
        listeyi_guncelle()


def listeyi_sil():
    t.delete(0, "end")


def listeyi_guncelle():
    listeyi_sil()
    for i in task:
        t.insert('end', i)


def db_getir():
    while (len(task) != 0):
        task.pop()
    for row in im.execute("SELECT title from tasks"):
        task.append(row[0])

def birini_sil():
    try:
        val = t.get(t.curselection())
        if val in task:
            task.remove(val)
            listeyi_guncelle()
            im.execute("DELETE FROM tasks WHERE title = ?", (val,))
    except:
        messagebox.showinfo("Silinemedi", "Bilinemeyen bir hata oluştu")

def hepsini_sil():
    mb = messagebox.askyesno("Hepsi Silinecek","Emin misiniz ?")
    if mb:
        while (len(task) != 0):
            task.pop()
        im.execute("DELETE FROM tasks")
        listeyi_guncelle()

l1 = ttk.Label(root, text="To-Do List")
l2 = ttk.Label(root, text="Görev adını giriniz :")
e1 = ttk.Entry(root, width=21)
t = Listbox(root, height=11, selectmode='SINGLE')
b1 = ttk.Button(root, text="Görev Ekle", width=20, command=gorev_ekle)
b2 = ttk.Button(root, text="Sil", width=20, command=birini_sil)
b3 = ttk.Button(root, text="Hepsini Sil", width=20, command=hepsini_sil)
b4 = ttk.Button(root, text="Çıkış", width=20, command=cikis)

db_getir()
listeyi_guncelle()

l1.place(x=50, y=10)
l2.place(x=50, y=50)
e1.place(x=50, y=80)
b1.place(x=50, y=110)
b2.place(x=50, y=140)
b3.place(x=50, y=170)
b4.place(x=50, y=200)
t.place(x=220, y=50)

root.mainloop()

baglanti.commit()
baglanti.close()
