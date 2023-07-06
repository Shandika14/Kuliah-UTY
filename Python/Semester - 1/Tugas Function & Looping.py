hargasewa1 = 75000
hargasewa2 = 80000
hargasewa3 = 90000
hargasewa4 = 100000
hargasewa5 = 110000

def data_customer ():
          Nama = input ("Nama Customer : ")
          Domisili = input ("Domisili : ")
          Jaminan = input("Jaminan :")
          Status = input("Status : ")
          Jenis_Member = input ("Jenis Member : ")

def jenis_motor ():
        Motor1 = "Matic"
        Motor1_1 = "Beat"
        Motor1_2 = "Vario"
        Motor1_3 = "Aerox"
        Motor1_4 = "Nmax"
        Motor1_5 = "PCX"

        Motor2 = "Kopling"
        Motor2_1 = "Vixion"
        Motor2_2 = "KLX"
        Motor2_3 = "CRF"
        Motor2_4 = "CBR"
        Motor2_5 = "ZX25"

        print("======Jenis Motor======")
        print(Motor1, " : ")
        print(Motor1_1)
        print(Motor1_2)
        print(Motor1_3)
        print(Motor1_4)
        print(Motor1_5)
        print ("")
        print(Motor2, " : ")
        print(Motor2_1)
        print(Motor2_2)
        print(Motor2_3)
        print(Motor2_4)
        print(Motor2_5)

        jenis_motor = input("Jenis Motor :")

def batas_waktu ():
        print("")
        print("======Batas Waktu======")
        batas_waktu = int(input("Batas Waktu Rental : "))
        if(batas_waktu == 1):
                print("Biaya Rental Motor = ", hargasewa1)
        elif(batas_waktu == 2):
                print("Biaya Rental Motor = ", hargasewa2)
        elif(batas_waktu == 3):
                print("Biaya Rental Motor = ", hargasewa3)
        elif(batas_waktu == 4):
                print("Biaya Rental Motor = ", hargasewa4)
        elif(batas_waktu == 5):
                print("Biaya Rental Motor = ", hargasewa5)
        else:
                print("ANDA SALAH INPUT!!!")
                    
def lama_rental_1():
    print("")   
    print("======Paket Rental 1======")    
    print("TEKAN ANGKA 0(Nol) JIKA INI BUKAN PAKET PERMINTAAN ANDA!")    
    print ("Lama Rental 1-7 Hari")
    lama_rental = int(input("Lama Waktu Anda Rental Motor Paket 1 :"))
    if(lama_rental >= 1 and lama_rental <= 2): 
            Harga1_1 = hargasewa1 + 50000
            print("Harga Dengan Durasi Rental 1-2 Hari : ", Harga1_1)
    elif(lama_rental >= 3 and lama_rental <= 4):
            Harga1_2 = hargasewa2 + 75000
            print("Harga Dengan Durasi Rental 3-4 Hari :", Harga1_2)
    elif(lama_rental >=5 and lama_rental <=6):
            Harga1_3 = hargasewa3 + 100000
            print("Harga Dengan Durasi Rental 5-6 Hari :", Harga1_3)
    elif(lama_rental >=7):
            Harga1_4 = hargasewa4 + 150000
            print("Harga Dengan Durasi Rental 7 Hari :", Harga1_4)
    else:
            print("MELEWATI PAKET!!")
                     
def lama_rental_2():
    print("")   
    print("======Paket Rental 2======")    
    print("TEKAN ANGKA 0(Nol) JIKA INI BUKAN PAKET PERMINTAAN ANDA!")    
    print ("Lama Rental 1-7 Hari")
    lama_rental = int(input("Lama Waktu Anda Rental Motor Paket 2 :"))
    if(lama_rental >= 1 and lama_rental <= 2): 
            Harga2_1 = hargasewa1 + 50000
            print("Harga Dengan Durasi Rental 1-2 Hari : ", Harga2_1)
    elif(lama_rental >= 3 and lama_rental <= 4):
            Harga2_2 = hargasewa2 + 75000
            print("Harga Dengan Durasi Rental 3-4 Hari :", Harga2_2)
    elif(lama_rental >=5 and lama_rental <=6):
            Harga2_3 = hargasewa3 + 100000
            print("Harga Dengan Durasi Rental 5-6 Hari :", Harga2_3)
    elif(lama_rental >=7):
            Harga2_4 = hargasewa4 + 150000
            print("Harga Dengan Durasi Rental 7 Hari :", Harga2_4)
    else:
            print("MELEWATI PAKET!!")

def lama_rental_3():
    print("")    
    print("======Paket Rental 3======")    
    print("TEKAN ANGKA 0(Nol) JIKA INI BUKAN PAKET PERMINTAAN ANDA!")    
    print ("Lama Rental 1-7 Hari")
    lama_rental = int(input("Lama Waktu Anda Rental Motor Paket 3 :"))
    if(lama_rental >= 1 and lama_rental <= 2): 
            Harga3_1 = hargasewa1 + 50000
            print("Harga Dengan Durasi Rental 1-2 Hari : ", Harga3_1)
    elif(lama_rental >= 3 and lama_rental <= 4):
            Harga3_2 = hargasewa2 + 75000
            print("Harga Dengan Durasi Rental 3-4 Hari :", Harga3_2)
    elif(lama_rental >=5 and lama_rental <=6):
            Harga3_3 = hargasewa3 + 100000
            print("Harga Dengan Durasi Rental 5-6 Hari :", Harga3_3)
    elif(lama_rental >=7):
            Harga3_4 = hargasewa4 + 150000
            print("Harga Dengan Durasi Rental 7 Hari :", Harga3_4)
    else:
            print("MELEWATI PAKET!!")

def lama_rental_4():
    print("")   
    print("======Paket Rental 4======")    
    print("TEKAN ANGKA 0(Nol) JIKA INI BUKAN PAKET PERMINTAAN ANDA!")    
    print ("Lama Rental 1-7 Hari")
    lama_rental = int(input("Lama Waktu Anda Rental Motor Paket 4 :"))
    if(lama_rental >= 1 and lama_rental <= 2): 
            Harga4_1 = hargasewa1 + 50000
            print("Harga Dengan Durasi Rental 1-2 Hari : ", Harga4_1)
    elif(lama_rental >= 3 and lama_rental <= 4):
            Harga4_2 = hargasewa2 + 75000
            print("Harga Dengan Durasi Rental 3-4 Hari :", Harga4_2)
    elif(lama_rental >=5 and lama_rental <=6):
            Harga4_3 = hargasewa3 + 100000
            print("Harga Dengan Durasi Rental 5-6 Hari :", Harga4_3)
    elif(lama_rental >=7):
            Harga4_4 = hargasewa4 + 150000
            print("Harga Dengan Durasi Rental 7 Hari :", Harga4_4)
    else:
            print("MELEWATI PAKET!!")

def lama_rental_5():
    print("")   
    print("======Paket Rental 5======")    
    print("TEKAN ANGKA 0(Nol) JIKA INI BUKAN PAKET PERMINTAAN ANDA!")    
    print ("Lama Rental 1-7 Hari")
    lama_rental = int(input("Lama Waktu Anda Rental Motor Paket 5 :"))
    if(lama_rental >= 1 and lama_rental <= 2): 
            Harga5_1 = hargasewa1 + 50000
            print("Harga Dengan Durasi Rental 1-2 Hari : ", Harga5_1)
    elif(lama_rental >= 3 and lama_rental <= 4):
            Harga5_2 = hargasewa2 + 75000
            print("Harga Dengan Durasi Rental 3-4 Hari :", Harga5_2)
    elif(lama_rental >=5 and lama_rental <=6):
            Harga5_3 = hargasewa3 + 100000
            print("Harga Dengan Durasi Rental 5-6 Hari :", Harga5_3)
    elif(lama_rental >=7):
            Harga5_4 = hargasewa4 + 150000
            print("Harga Dengan Durasi Rental 7 Hari :", Harga5_4)
    else:
            print("MELEWATI PAKET!!")

def main():
        print("=========Rental Motor Dika=========")
        print("")
        print("Silahkan Input Identitas Anda")
        data_customer()
        print("")
        jenis_motor ()
        batas_waktu ()
        lama_rental_1 ()
        lama_rental_2 ()
        lama_rental_3 ()
        lama_rental_4 ()
        lama_rental_5 ()


main ()
