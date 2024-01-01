import os
class UTY(object):
    def __init__(self, status, nama, prodi):
        self.nama = nama
        self.status = status
        self.prodi = prodi
    
    def semangat(self):
        print('Indonesia Maju, Indonesia Tumbuh, UTY Hebat')

    def info(self):
        print("--| INFORMASI |--")
        print("Nama         : " + self.nama)
        print("Status       : " + self.status)
        print("Program Studi: " + self.prodi)

class Dosen(UTY):
    def __init__(self, status, nama, prodi, nip):
        super().__init__(status, nama, prodi)
        self.nip = nip
    
    def SemangatDosen(self):
        super().semangat()
        print("Dosen Bermartabat")
    
    def InfoDosen(self):
        self.info()
        print("NIP          : " + str(self.nip))



os.system('cls' if os.name == 'nt' else 'clear')

dosen = Dosen("Dosen", "Thomas", "Informatika", 1234567)
dosen.InfoDosen()
dosen.SemangatDosen()
