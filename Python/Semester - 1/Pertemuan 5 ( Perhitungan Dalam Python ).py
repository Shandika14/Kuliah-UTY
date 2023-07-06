# No 1
print("======Program Perulangan Perhitungan Bilangan Berpangkat======")
print("")
a = int(input("Masukkan Bilangan :"))
for i in range(a):
    hasil = i**2
    print(hasil)

# No 2
print("")
print("=====Program Perulangan Bintang Pola Segitiga=====")
print("")
b = 11
for i in range(0, b):
    for j in range(0, i):
        print(' ', end=' ')
    for k in range(0,b):
        print('*',end=' ')
    b-=2
    print('')

print("Program Menghitung Luas Lingkaran")
phi = 3.14
r = int (input("r= "))
luaslingkaran = phi*r*r 

print ("Luas Lingkaran = ", luaslingkaran)
