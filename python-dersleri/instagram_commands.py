from tkinter import *
from tkinter import messagebox
from instagram_private_api import Client, ClientCompatPatch

username = ""
password = ""

def login(username, password):
    try:
        api = Client(username, password)
        results = api.feed_timeline()
        items = results.get('items', [])
        for item in items:
            print(item)
            media = ClientCompatPatch.media(item)
            print(media['code'])
    except:
        messagebox.showinfo("Hata", "Instagram girişi hatalı lütfen kullanıcı adı şifrenizi kontrol ediniz")