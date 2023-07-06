def data_diri():
    print("Program input data diri")
    a = input("input Nama :")
    b = input("input asal :")
    c = input("input kelas :")
    d = int(input("input NPM : "))
    e = int(input("input Tanggal Lahir: "))
 
    print("Nama =", a)
    print("asal =", b)
    print("Kelas =", c)
    print("NPM =", d)
    print("Tanggal Lahir =", e)

print("Program Fungsi")
data_diri()
print("")


def perhitungan_angka():
    print("Program Perhitungan Angka :")
    f =int(input("input angka pertama :"))
    g =int(input("input angka kedua :"))
    h =int(input("input angka ketiga :"))
    i =int(input("input angka keempat :"))
    return f*g*h*i

print("Hasil perhitungan angka =", perhitungan_angka())
print("")


def menghitung_luas_persegi():
    print("Program Menghitung Luas Persegi")
    s =int(input("input Sisi :"))
    return s*s

print("Luas Persegi =", menghitung_luas_persegi())
print("")


def perhitungan_angka_decimal():
    print("Program Perhitungan Angka Decimal")
    j =float(input("input angka pertama :"))
    k =float(input("input angka kedua :"))
    m =float(input("input angka ketiga :"))
    return j*k+m

print("Hasil Perhitungan Angka Decimal", perhitungan_angka_decimal())
print("")
