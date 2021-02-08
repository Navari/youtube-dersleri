import sqlite3 as sql

vt = sql.connect("sqlite_dersleri")
im = vt.cursor()

# im.execute("CREATE TABLE IF NOT EXISTS kullanicilar (username, password)")

# lst = [("deneme", "123456"), ("celalettin", "yilmaz"), ("yılmaz","celalettin")]
#
# for kullanici in lst:
#     im.execute("""
#         INSERT INTO kullanicilar VALUES (?, ?)
#     """, kullanici)
#

# im.execute("SELECT * FROM kullanicilar")
# veriler = im.fetchall()
#
# for veri in veriler:
#     print(veri)

# im.execute("""SELECT * FROM kullanicilar WHERE password = "123456" """)
# veri = im.fetchone()
# print(veri)

# im.execute("""UPDATE kullanicilar SET password = "asdasd" WHERE password = "123456" """)

im.execute("""DELETE FROM kullanicilar WHERE password="1234" """)

vt.commit()
vt.close()