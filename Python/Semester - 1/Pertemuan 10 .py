import sqlite3
with sqlite3.connect("Diskon.db") as db:
     cursor = db.cursor()

import datetime
tanggal = datetime.datetime.now()
pilihan = "Y"
while pilihan== "Y":
 print("""
    =====================================
               Jenis Member
    =====================================
    A. Silver
    B. Gold
    C. Platinum
    ======================================
    """)
 member =str(input("Input Jenis Member :"))
 nomember=int(input("No Member :"))
 total_belanja=int(input("Total Belanja :Rp."))
 if member == "A":
     jenis_member= "Silver"
     if total_belanja >= 150000:
        diskon = int(total_belanja*0.1)
        bayar = total_belanja-diskon
     else:
        diskon =(0)
        totalharga = total_belanja
 elif member == "B":
     jenis_member= "Gold"
     if total_belanja >= 150000:
        diskon = int(total_belanja * 0.2)
        bayar = total_belanja-diskon
     else:
        diskon =(0)
        totalharga = total_belanja
 elif member == "C":
    jenis_member= "Platinum"
    total_belanja= 150000
    diskon= int(total_belanja*0.3)
    bayar = total_belanja-diskon
 else:
    jenis_member = "-"
    total_belanja = "-"
    diskon = "-"
    bayar = "-"
    pilihan = input(" Member Tidak Ada ")
 print("============================")
 print("======STRUK PEMBAYARAN======")
 print("============================")
 print("Tanggal         :", tanggal)
 Nama_Customer = input("Nama Customer:")
 print("Jenis Member    :",jenis_member)
 print("Total Belanja   :Rp.", total_belanja)
 print("Total Bayar     :Rp.", bayar)
 print("Diskon          :Rp.", diskon)
 print("============================")
 Uang = int(input("Uang Bayar  :Rp."))
 Kembalian = int(Uang-bayar)
 print("Kembalian       :Rp.",Kembalian)
 print("============================")
 pilihan=input("Apakah anda ingin melakukan transaksi lagi ? Y/N =")

 cursor.execute(""" CREATE TABLE IF NOT EXISTS Diskon(No_Member integer PRIMARY KEY,Nama_Customer text,
    Jenis_Member text, Total_Belanja int,Total_Bayar int,Diskon int); """)
 cursor.execute(""" INSERT INTO Diskon(No_Member,Nama_Customer,Jenis_Member,Total_Belanja,Total_Bayar,Diskon) 
    VALUES(?,?,?,?,?,?)""", (nomember,Nama_Customer , jenis_member, total_belanja,bayar,diskon))
 db.commit()

cursor.execute("SELECT * FORM Diskon")
for x in cursor.fetchall():
    print(x)

db.close()
