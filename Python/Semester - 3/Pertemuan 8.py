import os
os.system('cls' if os.name == 'nt' else 'clear')

class Kalkulator:
    def __init__(self,x,y):
        self.A = x
        self.B = y
        print("A = "+str(x)+" ,B = "+str(y))

    def Tambah(self):
        self.hasil = self.A + self.B
        print("A+B = "+str(self.hasil))

    def Kurang(self):
        self.hasil = self.A - self.B
        print("A-B = "+str(self.hasil))

    def Kali(self):
        self.hasil = self.A * self.B
        print("AxB = "+str(self.hasil))

    def Bagi(self):
        if self.B == 0:
            print("Pembagian Dengan Nol")
        else:
            self.hasil = self.A / self.B
            print("A/B = "+str(self.hasil))

Object1 = Kalkulator(1,2)
Object1.Tambah()
Object1.Kurang()
Object1.Kali()
Object1.Bagi()
Object2 = Kalkulator(2,0)
Object2.Bagi()
    

    
