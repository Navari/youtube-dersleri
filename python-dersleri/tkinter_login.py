# coding:utf-8
"""
Author: Edgar
"""
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import json


window = Tk()
window.title("Welcome")
window.geometry("500x400")
window.resizable(width=False, height=False)
image = Image.open("./welcome.jpg")
img = ImageTk.PhotoImage(image, size=10)
c = Canvas(window, width=500, height=200)
c.create_image(250, 0, image=img, anchor=N)

img_2 = Image.open("./sign_up.jpg")
img_2 = ImageTk.PhotoImage(img_2)
c.pack()


username_label = Label(window, font='Monaco 12', text="username:")
passwd_label = Label(window, font='Monaco 12', text='password:')

username_label.place(x=40, y=220)
passwd_label.place(x=40, y=260)

welcome = Label(window, font="monaco 12", text='Welcome here to learn python !')
welcome.place(x=250, y=320, anchor=N)
username = StringVar()
passwd = StringVar()
username_entry = Entry(window, font='Monaco 10', width=20, textvariable=username)
passwd_entry = Entry(window, font='Monaco 10', width=20, textvariable=passwd, show='*')

username_entry.place(x=150, y=225)
passwd_entry.place(x=150, y=265)


# 提交登录
def login():
    user = username.get()
    password = passwd.get()
    if str(user) and str(password):
        try:
            with open('./data.json', 'r') as file:
                data = json.load(file)
                if user in data:
                    if password == data[user]:
                        messagebox.showinfo(title='Successfully', message="Login in susscessfully")
                    else:
                        messagebox.showerror(title='Error', message='password is wrong')
                else:
                    flag = messagebox.askyesno(title='sign up',
                                               message='You have not signed up, do you want to sign up')
                    if flag:
                        sign_up()
                    else:
                        window.destroy()
        except:
            with open('./data.json', 'w') as file:
                admin = {"admin": "Cyberist"}
                json.dump(admin, file)
                if user == 'admin' and password == 'Cyberist':
                    messagebox.showinfo(title='Successfully', message="Login in susscessfully")
                else:
                    messagebox.showerror(title='Error', message='password is wrong')
    else:
        messagebox.showerror(title="Error", message='Fill in all the blank')


def sign_up():
    def write_in():
        if str(new_passwd.get()) and str(new_user.get()) and str(new_passwd_confirm.get()):
            if new_passwd_confirm.get() == new_passwd.get():
                try:
                    file = open("./data.json", "r")
                    data = json.load(file)
                    file.close()
                    if str(new_user.get()) in data:
                        messagebox.showinfo(title='Error', message='The username has been signed')
                    else:
                        user = str(new_user.get())
                        passwd = new_passwd.get()
                        data[user] = passwd
                        with open('./data.json', 'w') as file:
                            json.dump(data, file)
                        messagebox.showinfo(message="Sign up finished", title='Successfully')
                        win.destroy()
                except Exception as e:
                    pass
            else:
                messagebox.showerror(title='Error', message='The confirmed password is not right !')
        else:
            messagebox.showerror(title='Error', message='Fill in all the blank !')

    win = Toplevel()
    win.title("Sign up")
    win.geometry('400x300')
    win.wm_attributes('-topmost', -1)

    win_c = Canvas(win)
    win_c.create_image(190, 150, image=img_2)
    win_c.pack()

    prompt = Label(win, text='Cyberist -- a python learner', font='Monaco 8')
    prompt.place(x=100, y=270)

    user_label = Label(win, text='username:', font='monaco 10', bg=None)
    pwd_label = Label(win, text='password:', font='monaco 10')
    pwd_confirm_label = Label(win, text='confirm:', font='monaco 10')

    user_label.place(x=20, y=180)
    pwd_label.place(x=20, y=210)
    pwd_confirm_label.place(x=20, y=240)

    new_user = StringVar()
    new_passwd = StringVar()
    new_passwd_confirm = StringVar()

    user_entry = Entry(win, font='Monaco 12', width=20, textvariable=new_user)
    passwd_entry = Entry(win, font='Monaco 12', width=20, textvariable=new_passwd, show='*')
    passwd_confirm_entry = Entry(win, font='Monaco 12', width=20, textvariable=new_passwd_confirm, show='*')

    tmp_username = username.get()
    new_user.set(tmp_username)

    user_entry.place(x=100, y=180)
    passwd_entry.place(x=100, y=210)
    passwd_confirm_entry.place(x=100, y=240)
    sign_up_button = Button(win, text='sign up', font='Monaco 10', command=write_in)
    sign_up_button.place(x=310, y=210)


login_button = Button(window, width=8, text='Login in', font='Monaco 10', borderwidth=1, command=login)

sign_up_buttom = Button(window, width=8, text='Sign up', font='Monaco 10', borderwidth=1, command=sign_up)

login_button.place(x=360, y=260)
sign_up_buttom.place(x=360, y=220)

window.mainloop()
