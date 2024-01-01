class Penentuan_Batas_Nilai():
    def __init__ (self):
        self.nilai = 10
        self._batas = 10

    def cek_nilai(self):
        if self.nilai == self._batas:
            print(f'Sepuluh')
        else:
            print(f'Bukan Sepuluh')

Penentuan = Penentuan_Batas_Nilai()
Penentuan.cek_nilai()