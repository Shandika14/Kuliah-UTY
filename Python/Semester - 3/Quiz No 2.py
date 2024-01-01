class UTY:
    def __init__(self):
        self.s1 = "UNIVERSITAS "
        self.s2 = "TEKNOLOGI "
        self.s3 = "YOGYAKARTA "

    def buat_pesan(self):
        s4  = self.s1 + self.s2 + self.s3
        return s4
    
    def cetak_pesan(self):
        s4 = self.buat_pesan()
        print(f'{self.s2} OF {self.s3} UNIVERSITY')


KALIMAT = UTY()
PESAN = KALIMAT.buat_pesan()

print(PESAN)
KALIMAT.cetak_pesan()
