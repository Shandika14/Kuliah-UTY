# No 1
class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.__harga = harga

    def info(self):
        print("Nama Menu = " + self.nama + " Harga = Rp. " + str(self.__harga))

    def memesan(self, jumlah=1):
        print(f"{jumlah} {self.nama} Telah Dipesan")

Menu1 = Menu("Nasi Goreng", 10000)
Menu2 = Menu("Mie Goreng", 8000)

print("=====| MENU |=====")
Menu1.info()
Menu2.info()

print("")
pilihan_menu = int(input("Pilih Menu (1 Untuk Nasi Goreng, 2 Untuk Mie Goreng): "))
jumlah_pesan = int(input("Jumlah Yang Akan Dipesan: "))

if pilihan_menu == 1:
    Menu1.memesan(jumlah_pesan)
elif pilihan_menu == 2:
    Menu2.memesan(jumlah_pesan)
else:
    print("Menu Tidak Valid")


# No 2
class Mahasiswa:
    def __init__(self, nama, npm, prodi):
        self.nama = nama
        self.__npm = npm
        self.prodi = prodi
        self.mahasiswa_baru = []

    def info(self):
        print(f"Nama Mahasiswa : {self.nama} - NPM = {self.__npm} Prodi = {self.prodi}")

    def tambah_mahasiswa(self, nama, npm, prodi):
        mahasiswa_baru = Mahasiswa(nama, npm, prodi)
        self.mahasiswa_baru.append(mahasiswa_baru)
        print(f'Mahasiswa Baru Ditambahkan: {nama} - NPM = {npm} Prodi = {prodi}')

print("")
Mahasiswa1 = Mahasiswa("Dika", 5220411325, "Informatika")
Mahasiswa2 = Mahasiswa("Rafli", 5221112344, "Sistem Informasi")

print("=====| DATA MAHASISWA |=====")
Mahasiswa1.info()
Mahasiswa2.info()

while True:
    print("")
    tambah = input("Tambah Mahasiswa Baru (Ya/Tidak): ")
    if tambah.lower() == "ya":
        nama = input("Nama Mahasiswa: ")
        npm = int(input("NPM: "))
        prodi = input("Prodi: ")
        Mahasiswa1.tambah_mahasiswa(nama, npm, prodi)
    else:
        break


# No 3
class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, no_isbn, halaman):
        self.__judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.no_isbn = no_isbn
        self.halaman = halaman


    def info(self):
        print(f"Judul  : " +str(self.__judul))
        print(f"Pengarang : " +str(self.pengarang))
        print(f"Tahun Terbit : " +str(self.tahun_terbit))
        print(f"No ISBN : " +str(self.no_isbn))
        print(f"Jumlah Halaman : " +str(self.halaman))

Buku1 = Buku("Harry Potter", "Tj", 1991, 1222212, "300 Halaman")
Buku2 = Buku("Laskar Pelangi", "Andrea Hirata", 1990, 22222222, "220 Halaman")

print("")
print("=====| DAFTAR BUKU |=====")
Buku1.info()
print("")
Buku2.info()
print("")


# No 4
class Mahasiswa_:
    def __init__(self):
        self.__nilai  = 0

    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai = nilai
            print("Nilai Mahasiswa Telah Diatur ke ", nilai)
        else:
            print("Nilai Tidak Valid, Harus Berada Dalam Rentang 0 Hingga 100")
    
    def get_nilai(self):
        return self.__nilai
    
mahasiswa1 = Mahasiswa_()
nilai_mahasiswa1 = 85
mahasiswa1.set_nilai(nilai_mahasiswa1)

print("Nilai Mahasiswa 1:", mahasiswa1.get_nilai())
mahasiswa1.set_nilai(nilai_mahasiswa1)

mahasiswa2 = Mahasiswa_()
nilai_mahaiswa2 = 110
mahasiswa2.set_nilai(nilai_mahaiswa2)