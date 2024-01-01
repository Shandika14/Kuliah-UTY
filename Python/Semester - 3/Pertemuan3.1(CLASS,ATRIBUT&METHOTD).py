

class Anjing:
    def __init__(self, nama, umur, warna):
        self.nama = nama
        self.umur = umur
        self.warna = warna

    def menggonggong(self):
        print("guk..... gukk....")

        
    def info(self):
        print("Nama Anjing = " +self.nama+ ",umurnya = " +str(self.umur)+ "tahun, warnanya = " +str(self.warna))

    def berlari(self):
        print("Cepat..... Sekali")


Anjing1 = Anjing("Dogie", 19, "Merah")

Anjing1.menggonggong()
Anjing1.info()
Anjing1.berlari()

# objek1 = Anjing("dugdug",2,"belang putih")
# objek2 = Anjing("dogdog", 3, "putih")
# print(objek1.nama)
# print(objek1.umur)
# print(objek1.warna)

# t = 'Nama () ,umur() tahun, warna {}'.format(objek1.nama,objek1.umur,objek1.warna)
# print(t)