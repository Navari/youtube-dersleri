from tkinter import *
import sqlite3
from tkinter import ttk,messagebox

baglanti = sqlite3.connect("ogrenci_isleri.db")
im = baglanti.cursor()
im.execute("CREATE TABLE IF NOT EXISTS ogrenci(name TEXT, branch TEXT, section TEXT, roll TEXT, cgpa FLOAT)")

def insert_data(name, branch, section, roll, cgpa):
    im.execute("INSERT INTO ogrenci(name, branch, section, roll, cgpa) VALUES (?,?,?,?,?)", (name, branch, section, roll, cgpa))
    messagebox.showinfo("Başarılı", "Öğrenci ekleme işlemi başarılı")
    baglanti.commit()
    baglanti.close()

def insert():
    add_window = Tk()
    add_window.title("Öğrenci Ekle")
    Label(add_window).grid(row=0, column=0, columnspan=2)
    Label(add_window, text="Öğrenci Adı").grid(row=1, column=0)
    name_entry = Entry(add_window, width=50)
    name_entry.grid(row=1, column=1)
    Label(add_window, text="Şube").grid(row=2, column=0)
    branch_entry = Entry(add_window, width=50)
    branch_entry.grid(row=2, column=1)
    Label(add_window, text="Bölüm").grid(row=3, column=0)
    section_entry = Entry(add_window, width=50)
    section_entry.grid(row=3, column=1)
    Label(add_window, text="Okul Numarası").grid(row=4, column=0)
    roll_entry = Entry(add_window, width=50)
    roll_entry.grid(row=4, column=1)
    Label(add_window, text="AGNO:").grid(row=5, column=0)
    cgpa_entry = Entry(add_window, width=50)
    cgpa_entry.grid(row=5, column=1)

    Button(add_window, text="Ekle", activebackground="grey", activeforeground="white", command=lambda: submit()).grid(row=6, column=0, columnspan=2, pady=10)

    def submit():
        name = name_entry.get()
        branch = branch_entry.get()
        section = section_entry.get()
        roll = roll_entry.get()
        cgpa = cgpa_entry.get()
        insert_data(name, branch, section, roll, cgpa)
        add_window.destroy()

    add_window.mainloop()

def display():
    display_window = Tk()
    display_window.title("Öğrenciler")
    table = ttk.Treeview(display_window)
    table["columns"] = ["one", "two", "three", "four", "five"]
    table.heading("one", text="Öğrenci Adı")
    table.heading("two", text="Şube")
    table.heading("three", text="Bölüm")
    table.heading("four", text="Öğrenci No")
    table.heading("five", text="AGNO")

    data = im.execute("SELECT rowid,* FROM ogrenci")
    i = 0
    for ogrenci in data:
        table.insert('', i, text="Öğrenci : " + str(ogrenci[0]), values=(ogrenci[1], ogrenci[2], ogrenci[3], ogrenci[4], ogrenci[5]))
        i += 1
    table.pack()
    baglanti.close()

def update():
    update_window = Tk()
    update_window.title("Öğrenci güncelleme işlemi")
    Label(update_window, text="Bir öğrenci id seçiniz güncellemek istediğiniz").grid(row=0, column=0, sticky=W, padx=10, columnspan=2)
    o_id = Entry(update_window, width=50)
    o_id.grid(row=1, column=0, sticky=W, padx=10, columnspan=2)
    Label(update_window, text="Yeni değerleri giriniz : ").grid(row=2, column=0, sticky=W, padx=10, pady=10, columnspan=2)
    Label(update_window, text="İsim").grid(row=3, column=0, sticky=W, padx=10, pady=10)
    o_name = Entry(update_window, width=50)
    o_name.grid(row=3, column=1, sticky=W, padx=10, pady=10)
    Label(update_window, text="Şube").grid(row=4, column=0, sticky=W, padx=10, pady=10)
    o_branch = Entry(update_window, width=50)
    o_branch.grid(row=4, column=1, sticky=W, padx=10, pady=10)
    Label(update_window, text="Bölüm").grid(row=5, column=0, sticky=W, padx=10, pady=10)
    o_section = Entry(update_window, width=50)
    o_section.grid(row=5, column=1, sticky=W, padx=10, pady=10)
    Label(update_window, text="Öğrenci No").grid(row=6, column=0, sticky=W, padx=10, pady=10)
    o_roll = Entry(update_window, width=50)
    o_roll.grid(row=6, column=1, sticky=W, padx=10, pady=10)
    Label(update_window, text="AGNO").grid(row=7, column=0, sticky=W, padx=10, pady=10)
    o_agno = Entry(update_window, width=50)
    o_agno.grid(row=7, column=1, sticky=W, padx=10, pady=10)

    Button(update_window, text="Güncelle",
           activebackground="grey",
           activeforeground="white", command=lambda: submit()).grid(row=8, column=0, padx=0, pady=0, columnspan=2)
    def submit():
        oid = o_id.get()
        oname = o_name.get()
        obranch = o_branch.get()
        osection = o_section.get()
        oagno = o_agno.get()
        oroll = o_roll.get()
        im.execute("UPDATE ogrenci SET name = ?, branch = ?, section = ?, roll = ?, cgpa = ? WHERE rowid = ?", (oname, obranch, osection, oroll, oagno, oid))
        baglanti.commit()
        baglanti.close()
        messagebox.showinfo("Başarılı", "Öğrenci güncelleme işlemi başarılı")
        update_window.destroy()
    update_window.mainloop()

def delete():
    delete_window = Tk()
    delete_window.title("Öğrenci silme işlemi")
    Label(delete_window, text="Öğrenci ismini giriniz ").grid(row=0, column=0, padx=10, pady=10)
    d_name = Entry(delete_window, width=50)
    d_name.grid(row=0, column=1, padx=10, pady=10)
    Button(delete_window, text="Öğrenciyi sil", activebackground="grey", activeforeground="white",
           command=lambda: submit()).grid(row=1, column=0, columnspan=2)
    Label(delete_window).grid(row=2, column=0, columnspan=2)
    def submit():
        dname = d_name.get()
        im.execute("DELETE FROM ogrenci WHERE name = ?", (dname,))
        baglanti.commit()
        baglanti.close()
        messagebox.showinfo("Başarılı", "Öğrenci silme işlemi başarıyla tamamlandı")
        delete_window.destroy()
    delete_window.mainloop()