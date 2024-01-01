import os 
os.system('cls' if os.name == 'nt' else 'clear')

class Perusahaan:
    def __init__(self, nama_perusahaan, tahun_berdiri, alamat):
        self.__nama_perusahaan = nama_perusahaan
        self.__tahun_berdiri = tahun_berdiri
        self.__alamat = alamat

    def informasi_perusahaan(self):
        print()
        print(f"Perusahaan : {self.__nama_perusahaan}")
        print(f"Tahun Berdiri : {self.__tahun_berdiri}")
        print(f"Alamat : {self.__alamat}")

class Departemen(Perusahaan):
    def __init__(self, nama_departemen, kepala_departemen, jumlah_pegawai):
        super().__init__("ABC Corp", 2000, "Jl. Raya No. 123")
        self.__nama_departemen = nama_departemen
        self.__kepala_departemen = kepala_departemen
        self.__jumlah_pegawai = jumlah_pegawai
        self._total_pengeluaran_gaji = 0

    def hitung_pengeluaran_gaji(self):
        self._total_pengeluaran_gaji = self.__jumlah_pegawai * 5000
        return self._total_pengeluaran_gaji

class Pegawai:
    def __init__(self, nama, alamat, tanggal_gabung, gaji):
        self.nama = nama
        self.alamat = alamat
        self.tanggal_gabung = tanggal_gabung
        self.gaji = gaji

class ManajerDepartemen(Pegawai):
    def __init__(self, nama, alamat, tanggal_gabung, gaji, bonus, jumlah_proyek_ditangani):
        super().__init__(nama, alamat, tanggal_gabung, gaji)
        self.bonus = bonus
        self.jumlah_proyek_ditangani = jumlah_proyek_ditangani

def tampilkan_informasi(objek):
    if isinstance(objek, Departemen):
        print(f"Total Pengeluaran Gaji Departemen {objek._Departemen__nama_departemen} : ${objek.hitung_pengeluaran_gaji()}")
    elif isinstance(objek, ManajerDepartemen):
        print("____________________________________________________")
        print()
        print(f"\nNama Pegawai : {objek.nama}")
        print(f"Alamat: {objek.alamat}")
        print(f"Tanggal Gabung : {objek.tanggal_gabung}")
        print(f"Gaji : {objek.gaji}")
        print()


perusahaan1 = Perusahaan("ABC Corp", 2000, "Jl. Raya No. 123")
departemen_it1 = Departemen("IT", "Jono", 50)
manajer_it1 = ManajerDepartemen("BAIHAQI", "Jl. Bawal No. 1", "23-05-2020", 8000, 2000, 5)

perusahaan2 = Perusahaan("SOSRO Company", 1945, "Jl. Ahmad Yani No. 1")
departemen_it2 = Departemen("F&B", "Andre", 100)
manajer_it2 = ManajerDepartemen("Lutfi", "Jl. Mawar No. 69", "01-10-2018", 10000, 3000, 10)

perusahaan3 = Perusahaan("XYZ Corp", 2013, "Jl. Otista Raya No.101")
departemen_it3 = Departemen("IT", "Andri", 150)
manajer_it3 = ManajerDepartemen("Victor", "Jl. Cengkeh No.11", "05-02-2017", 15000, 4000, 15)

perusahaan1.informasi_perusahaan()
tampilkan_informasi(departemen_it1)
tampilkan_informasi(manajer_it1)

perusahaan2.informasi_perusahaan()
tampilkan_informasi(departemen_it2)
tampilkan_informasi(manajer_it2)

perusahaan3.informasi_perusahaan()
tampilkan_informasi(departemen_it3)
tampilkan_informasi(manajer_it3)