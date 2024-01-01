class mahasiswa:
    def __init__(self, nama, npm, jurusan):
        self.nama = nama        
        self.npm = npm
        self.jurusan = jurusan
        self.mata_kuliah = []
    
    def tambah_mata_kuliah(self, mata_kuliah):
        self.mata_kuliah.append(mata_kuliah)
        print(f'{self.nama} telah mengambil mata kuliah {mata_kuliah}')

    def tampilkan_info(self):
        print(f'Mahasiswa : {self.nama}')
        print(f'NPM : {self.npm}')
        print(f'jurusan : {self.jurusan}')
        print(f'Mata kuliah yang diambil :')
        for mata_kuliah in self.mata_kuliah:
            print(f'- {mata_kuliah}')

mahasiswa1 = mahasiswa('Dika', '522011325', 'informatika')
mahasiswa2 = mahasiswa('Flask', '522011315', 'informatika')

mahasiswa1.tambah_mata_kuliah("Pemrograman Berbasis Objek")
mahasiswa2.tambah_mata_kuliah("Pemrograman Web")

mahasiswa1.tampilkan_info()
mahasiswa2.tampilkan_info()