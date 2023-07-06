# ***
# STRING 
# ***
print("*****Pertemuan Ke-2*****")
Nama =  "Shandika"
NIM =  5220411325
Kelas = "6" 
Hobi = "Main Game"

print("Nama Saya :", Nama)
print("NIM       :", NIM)
print("Kelas     :", Kelas)
print("Hobi      :", Hobi)
print("")

#Style print
print("Nama Saya {}".format(Nama))
print("")

#Mengubah Kata Menjadi Huruf Kapital
print(Nama.upper())
print("")

#Mengubah Kata Menjadi Huruf Kecil
print(Nama.lower())
print("")

Nama_Lengkap = "Shandika Sayyid Ammar Pangesty"
#Mengganti Kata
print(Nama_Lengkap.replace("Sayyid", "Ammar"))
print("")

#Mencari Panjang Array
print(len(Nama_Lengkap))
print("")

#Mencari Awalan Kata
No_Hp = "+6281277335313"
if No_Hp.startswith("+62"):
    print(No_Hp, " ( Ini Nomor Dari Indonesia )")
print("")

#Mencari Akhiran Kata
Email = "Shandika.ap@gmail.com"
if Email.endswith("gmail.com"):
    print(Email, "( Ini Adalah Gmail )")
print("")

#Memecah Kalimat Menjadi Kata
Kalimat = "Saya Sedang Ngoding"
print(Kalimat.split())
print("")

#Memastikan Untuk Menghapus Spasi diawal dan di Akhir
Kata = "Shandika"
print(Kata.strip())