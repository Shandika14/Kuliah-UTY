import os

class Kalkulator:
    def __init__(self, x, y):
        self.A = x
        self.B = y
        print("A = " + str(x) + " ,B = " + str(y))

    def Tambah(self):
        self.hasil = self.A + self.B
        print("A + B = " + str(self.hasil))

    def Kurang(self):
        self.hasil = self.A - self.B
        print("A - B = " + str(self.hasil))

    def Kali(self):
        self.hasil = self.A * self.B
        print("A x B = " + str(self.hasil))

    def Bagi(self):
        if self.B == 0:
            print("Pembagian Dengan Nol")
        else:
            self.hasil = self.A / self.B
            print("A / B = " + str(self.hasil))

class KalkulatorAdvanced(Kalkulator):
    def Modulus(self):
        if self.B == 0:
            print("Modulus Dengan Nol Tidak Terdefinisi")
        else:
            self.hasil = self.A % self.B
            print("A % B = " + str(self.hasil))

    def Persentase(self):
        self.hasil = (self.A * self.B) / 100
        print(str(self.A) + " persen dari " + str(self.B) + " = " + str(self.hasil))

    def Pangkat(self):
        self.hasil = self.A ** self.B
        print("A^B = " + str(self.hasil))

    def AkarKuadratA(self):
        if self.A < 0:
            print("Akar kuadrat dari nilai negatif tidak terdefinisi")
        else:
            self.hasil = self.A ** 0.5
            print("Akar kuadrat dari A = " + str(self.hasil))

class MenuKalkulator:
    @staticmethod
    def tampilkan_menu():
        print("=========================")
        print("\n=== Kalkulator Menu ===")
        print("=========================")
        print("1. Tambah ")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Modulus")
        print("6. Persentase")
        print("7. Pangkat")
        print("8. Akar Kuadrat A")
        print("9. Ganti Angka")
        print("10. Keluar")

    @staticmethod
    def buat_objek():
        os.system('cls' if os.name == 'nt' else 'clear')
        x = int(input("Masukkan Nilai A: "))
        y = int(input("Masukkan Nilai B: "))
        return KalkulatorAdvanced(x, y)

menu_kalkulator = MenuKalkulator()
daftar_objek = [KalkulatorAdvanced(1, 2)]
objek_aktif = daftar_objek[0]

while True:
    menu_kalkulator.tampilkan_menu()
    pilihan = input("Silahkan Pilih Operasi Yang Anda Inginkan: ")
    if pilihan == '1':
        objek_aktif.Tambah()
    elif pilihan == '2':
        objek_aktif.Kurang()
    elif pilihan == '3':
        objek_aktif.Kali()
    elif pilihan == '4':
        objek_aktif.Bagi()
    elif pilihan == '5':
        objek_aktif.Modulus()
    elif pilihan == '6':
        objek_aktif.Persentase()
    elif pilihan == '7':
        objek_aktif.Pangkat()
    elif pilihan == '8':
        objek_aktif.AkarKuadratA()
    elif pilihan == '9':
        objek_aktif = menu_kalkulator.buat_objek()
    elif pilihan == '10':
        print("Terimakasih Sudah Menggunakan Kalkulator Kami")
        print("Have A Nice Day")
        break
    else:
        print("Pilihan Tidak Valid. Silakan Pilih Angka 1-10.")
