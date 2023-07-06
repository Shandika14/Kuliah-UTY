pilihan="Y"
while pilihan=="Y":
    print("""
    ==============================
            Rahardian Coffe
        List Menu Minuman Kopi 
    ==============================
    A. ES Kopi Susu   : Rp 11.000
    B. ES Kopi Coklat : Rp 12.000
    C. ES Kopi Hitam  : Rp 11.000
    D. Ice Americano  : Rp 14.000
    ==============================
    """)
    pesan=str(input("masukkan list abjad menu kopi ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "A":
        listnama= "ES Kopi Susu"
        harga=(11000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "B":
        listnama= "ES Kopi Coklat"
        harga = (12000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "C":
        listnama= "ES Kopi Hitam"
        harga=int(11000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "D":
        listnama= "ES Americano"
        harga=int(14000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkaPn abjad menu yang tersedia silahkan ulangi kembali Y/N =")
 
    print("==========================")
    print("     Rahardian Coffe     ")
    print("==========================")
    print("Menu         :",listnama)
    print("Jumlah Pesan :", jumlahpesan, "CUP")
    print("Harga        : Rp.", harga)
    print("Diskon       : Rp.", diskon)
    print("PPN          : Rp.", ppn)
    print("==========================")
    print("Jumlah Bayar : Rp.", totalharga)
    print("==========================")
    pilihan=input("apakah anda ingin order kembali Y/N =")