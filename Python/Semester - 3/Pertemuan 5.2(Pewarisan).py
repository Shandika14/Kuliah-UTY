import os
class Komputer:
    def __init__(self, nama, pabrikan, harga, jenis):
        self.nama = nama
        self.pabrikan = pabrikan
        self.harga = harga
        self.jenis = jenis

    def info(self):
        return (f"Nama: {self.nama}\nPabrikan: {self.pabrikan}\nHarga: {self.harga}\nJenis: {self.jenis}")

class Processor(Komputer):
    def __init__(self, nama, pabrikan, harga, jenis, jenis_processor, kecepatan):
        super().__init__(nama, pabrikan, harga, jenis)
        self.jenis_processor = jenis_processor
        self.kecepatan = kecepatan

    def info(self):
        parent_info = super().info()
        return (f"{parent_info}\nJenis Processor: {self.jenis_processor}\nKecepatan: {self.kecepatan} GHz")

class RAM(Komputer):
    def __init__(self, nama, pabrikan, harga, jenis, kapasitas, tipe):
        super().__init__(nama, pabrikan, harga, jenis)
        self.kapasitas = kapasitas
        self.tipe = tipe

    def info(self):
        parent_info = super().info()
        return (f"{parent_info}\nKapasitas RAM: {self.kapasitas} GB\nTipe RAM: {self.tipe}")

class Hardisk(Komputer):
    def __init__(self, nama, pabrikan, harga, jenis, kapasitas, tipe_hardisk):
        super().__init__(nama, pabrikan, harga, jenis)
        self.kapasitas = kapasitas
        self.tipe_hardisk = tipe_hardisk

    def info(self):
        parent_info = super().info()
        return (f"{parent_info}\nKapasitas Hardisk: {self.kapasitas} GB\nTipe Hardisk: {self.tipe_hardisk}")

os.system('cls' if os.name == 'nt' else 'clear')

print("=====| INFORMASI KOMPUTER |=====")
komputer = Komputer("Komputer 1", "Acer", 1000, "PC")
print(komputer.info())
print("")

processor = Processor("Komputer 2", "Intel", 1500, "Laptop", "Intel i7", 2.5)
print(processor.info())
print("")

ram = RAM("Komputer 3", "Kingston", 200, "PC", 16, "DDR4")
print(ram.info())
print("")

hardisk = Hardisk("Komputer 4", "Seagate", 80, "PC", 500, "External")
print(hardisk.info())
