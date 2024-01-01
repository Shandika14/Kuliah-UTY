import os
os.system('cls' if os.name == 'nt' else 'clear')

class Kendaraan:
    def __init__(self, merk, tahun_pembuatan):
        self.merk = merk
        self.tahun_pembuatan = tahun_pembuatan

    def InformasiKendaraan(self):
        print("Merk Kendaraan : ",self.merk)
        print ("Tahun Pembuatan : " ,self.tahun_pembuatan)

class Mobil(Kendaraan):
    def __init__(self, merk, tahun_pembuatan, jenis_bahan_bakar):
        super().__init__(merk, tahun_pembuatan)
        self.jenis_bahan_bakar = jenis_bahan_bakar

    def InformasiKendaraan(self):
        print('Mobil')
        super().InformasiKendaraan()
        print(f"Jenis Bahan Bakar : {self.jenis_bahan_bakar}")

class Motor(Kendaraan):
    def __init__(self, merk, tahun_pembuatan, kapasitas_mesin):
        super().__init__(merk, tahun_pembuatan)
        self.kapasitas_mesin = kapasitas_mesin

    def InformasiKendaraan(self):
        print("")
        print("Motor")
        super().InformasiKendaraan()
        print(f"Kapasitas Mesin : {self.kapasitas_mesin} CC")

class ManajemenKendaraan:
    def __init__(self):
        self.daftar_kendaraan = []

    def tambah (self, kendaraan):
        self.daftar_kendaraan.append(kendaraan)

    def InformasiKendaraan (self):
        print("======| Informasi Kendaraan |======")
        for kendaraan in self.daftar_kendaraan:
            kendaraan.InformasiKendaraan()

Manajemen_kendaraan = ManajemenKendaraan()
mobil1 = Mobil("Toyota", 2020, "Bensin")
motor1 = Motor("Yamaha", 2023, 250)

Manajemen_kendaraan.tambah(mobil1)
Manajemen_kendaraan.tambah(motor1)

Manajemen_kendaraan.InformasiKendaraan()

