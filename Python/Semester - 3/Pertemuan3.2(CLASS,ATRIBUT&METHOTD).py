class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi


    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi
    

Segitiga1 = Segitiga(5, 10)
Segitiga2 = Segitiga(10, 15)

print("Hasil dari luas segitiga 1 :", Segitiga1.hitung_luas())
print("Hasil dari luas segitiga 2 :", Segitiga2.hitung_luas())