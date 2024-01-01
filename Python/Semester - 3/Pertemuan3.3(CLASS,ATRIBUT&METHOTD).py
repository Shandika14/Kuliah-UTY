class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def info(self):
        print("Nama Menu = " +self.nama+ " Harga = Rp. " +str(self.harga))
    
    def memesan(self):
        print("Makanan Dipesan")


Menu1 = Menu("Nasi Goreng", 10000)
Menu2 = Menu("Mie Goreng", 8000)

print("=====| MENU |=====")
Menu1.info()
Menu2.info()
Menu1.memesan()

class Mahasiswa:
    def __init__(self, nama, npm, prodi):
        self.nama = nama
        self.npm = npm
        self.prodi = prodi
        self.mahasiswa_baru = []

    def info(self):
        print(f"Nama Mahasiswa : " +self.nama+ " - NPM = " +str(self.npm)+ " Prodi = " +str(self.prodi))

    def tambah_mahasiswa(self, mahasiswa_baru):
        self.mahasiswa_baru.append(mahasiswa_baru)
        print(f'{self.nama} {self.npm} {self.prodi}')
    
Mahasiswa1 = Mahasiswa("Dika", 5220411325, "Informatika")
Mahasiswa2 = Mahasiswa("Rafli", 5220112344, "Sistem Informasi")

print("")
Mahasiswa1.info()
Mahasiswa2.info()


class Buku:
    def __init__(self, judul, pengarang, tahun_terbit,no_isbn):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.no_isbn = no_isbn


    def info(self):
        print(f"Judul  : " +str(self.judul))
        print(f"Pengarang : " +str(self.pengarang))
        print(f"Tahun Terbit : " +str(self.tahun_terbit))
        print(f"No ISBN : " +str(self.no_isbn))

Buku1 = Buku("Harry Potter", "Tj", 1991, 1222212)
Buku2 = Buku("Laskar Pelangi", "Andrea Hirata", 1990, 22222222)

print("")
print("=====| DAFTAR BUKU |=====")
Buku1.info()
print("")
Buku2.info()
print("")


class Mobile_Legend:
    def __init__(self, rank, nama_hero, jenis_hero):
        self.rank = rank
        self.nama_hero = nama_hero
        self.jenis_hero = jenis_hero

    def info(self):
        print(f"Rank = " +str(self.rank))
        print(f"Hero = " +str(self.nama_hero))
        print(f"Role = " +str(self.jenis_hero))

    def dead(self):
        print(f"{self.nama_hero} Killed By Enemy")

Hero1 = Mobile_Legend("Legends", "Miya", "Marksman")
Hero2 = Mobile_Legend("Epic", "Alucard", "Fighter")
Hero3 = Mobile_Legend("Epic", "Franco", "Tank")
Hero4 = Mobile_Legend("Epic", "Nana", "Support")

Hero1.info()
print("")
Hero2.info()
print("")
Hero3.info()
print("")
Hero4.info()
print("")

Hero1.dead()
