import sqlite3

with sqlite3.connect("UTY.db") as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Mahasiswa1(NPM integer PRIMARY KEY,Nama text NOT NULL,Prodi text); """)
cursor.execute(""" INSERT INTO Mahasiswa1(NPM,Nama,Prodi) VALUES(1,"Alfa","08123456")""")
db.commit()

cursor.execute(""" INSERT INTO Alamatku2(id,firstname,phonenumber) VALUES(2,"Beta","08888888")""")
db.commit()

cursor.execute(""" INSERT INTO Alamatku2(id,firstname,phonenumber) VALUES(3,"Charly","08111111")""")
db.commit()

cursor.execute(""" INSERT INTO Alamatku2(id,firstname,phonenumber) VALUES(4,"Delta","081222222")""")
db.commit()

db.close()


