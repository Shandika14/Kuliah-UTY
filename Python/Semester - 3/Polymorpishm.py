import os
os.system('cls' if os.name == 'nt' else 'clear')
class Pegawai:
    jumlah = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Pegawai.jumlah += 1

    def TampilJumlah(self):
        print("Total Pegawai : ", Pegawai.jumlah)

    def TampilPegawai(self):
        print("Nama : ", self.nama)
        print("Gaji : Rp.", self.gaji)
    
    def Tunjangan(self, istri=None, anak=None):
        if anak != None and istri != None:
            total = anak+istri
            print("Tunjagan Anak + Istri : Rp.", total)
        else:
            total = istri
            print("Tunjangan Istri : Rp.", total)

peg1 = Pegawai("Riyanto", 2000)
peg2 = Pegawai("Aria Anggara", 5000)

print("No 1")
peg1.TampilPegawai()
peg2.TampilPegawai()
peg1.Tunjangan(2500,200)
peg2.Tunjangan(2500)

print("Total Pegawai %d" % Pegawai.jumlah)
rataGaji = (peg1.gaji + peg2.gaji) / Pegawai.jumlah
print("Rata-rata Gaji : "+str(rataGaji))


class SegiEmpat():
    def __init__(self, panjang , lebar):
        self.panjang = panjang
        self.lebar = lebar

    def HitungLuas(self):
        print("Luas Segi Empat = ", self.panjang * self.lebar, "M^2")

class BujurSangkar(SegiEmpat):
    def __init__(self,sisi):
        self.side = sisi
        SegiEmpat.__init__(self, sisi, sisi)
    
    def HitungLuas(self):
        print("Luas Bujur Sangkar = ", self.side * self.side, "M^2")

print("")
print("No 2")
b = BujurSangkar(4)
s = SegiEmpat(2,4)
b.HitungLuas()
s.HitungLuas()