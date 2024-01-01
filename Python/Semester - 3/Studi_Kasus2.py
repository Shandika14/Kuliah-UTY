import os 

class Konser:
    def __init__(self, nama_konser, tanggal, tempat, harga_tiket):
        self.nama_konser = nama_konser
        self.tanggal = tanggal
        self.tempat = tempat
        self.harga_tiket = harga_tiket

    def informasi_konser(self):
        print(f"Konser : {self.nama_konser}\nTanggal : {self.tanggal}\nTempat : {self.tempat}\nHarga Tiket : {self.harga_tiket}\n")
        print()

class Tiket:
    def __init__(self, nomor_tiket, kategori, status):
        self.nomor_tiket = nomor_tiket
        self.kategori = kategori
        self.status = status

    def pesan_tiket(self):
        if self.status == "Tersedia":
            print(f"Nomor Tiket: {self.nomor_tiket}\nKategori : {self.kategori}\nStatus : {self.status}")
            print(f"Tiket {self.nomor_tiket} ({self.kategori}) berhasil dipesan.")
            self.status = "Terjual"
            print(f"Nomor Tiket: {self.nomor_tiket}\nKategori: {self.kategori}\nStatus: {self.status}\n")

class TiketVIP(Tiket):
    def __init__(self, nomor_tiket, status):
        super().__init__(nomor_tiket, "VIP", status)


class TiketReguler(Tiket):
    def __init__(self, nomor_tiket, status):
        super().__init__(nomor_tiket, "Regular", status)

def informasi_tiket_polimorfik(tiket):
        tiket.pesan_tiket()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    konser_neck_deep = Konser("NECK DEEP", "25 Februari 2023", "Stadium XYZ", 100000)
    konser_neck_deep.informasi_konser()
    tiket_vip1 = TiketVIP("VIP001", "Tersedia")
    tiket_vip2 = TiketVIP("VIP002", "Tersedia")
    tiket_reguler1 = TiketReguler("Reg001", "Tersedia")
    tiket_reguler2 = TiketReguler("Reg002", "Tersedia")

    tiket_vip1.pesan_tiket()
    print("\n_______________________\n")
    tiket_reguler1.pesan_tiket()
    print("\n__________________________\n")

    tiket_vip2.pesan_tiket()
    print("\n_______________________\n")
    tiket_reguler2.pesan_tiket()
    print("\n__________________________\n")


    informasi_tiket_polimorfik(tiket_vip1)
    informasi_tiket_polimorfik(tiket_reguler1)
    informasi_tiket_polimorfik(tiket_vip2)
    informasi_tiket_polimorfik(tiket_reguler2)