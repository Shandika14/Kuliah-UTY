import datetime

nominal_pinjaman_list = ["Rp. 10.000.000", "Rp. 15.000.000", "Rp. 20.000.000", "Rp. 25.000.000"
                         "Rp. 30.000.000", "Rp. 35.000.000", "Rp. 40.000.000"]
tanggal = datetime.date.today()
def Kopersi_Simpan_Pinjam():
        pilihan="Y"
        while pilihan=="Y":
         print("""
                =================================
                Koperasi Simpan Pinjam Dika
                Nominal Pinjaman Yang Tersedia 
                =================================
                A. Rp. 10.000.000
                B. Rp. 15.000.000
                C. Rp. 20.000.000
                D. Rp. 25.000.000
                E. Rp. 30.000.000
                =================================
                """)
         pinjaman=str(input("Pilih Nominal Pinjaman Yang Anda Inginkan :"))
         if pinjaman == "A":
                nominal_pinjaman = nominal_pinjaman_list[0]
                tenor = (12)
                bunga = int(10000000/tenor*0.08)
                cicilan = int(10000000/tenor)
                jumlah_pengembalian= int((cicilan+bunga)*tenor)
         elif pinjaman == "B" :
                nominal_pinjaman = nominal_pinjaman_list[1]
                tenor = (18)
                bunga = int(15000000/tenor*0.08)
                cicilan = int(15000000*bunga*tenor)
                jumlah_pengembalian= int((cicilan+bunga)*tenor)
         elif pinjaman == "C" :
                nominal_pinjaman = nominal_pinjaman_list[2]
                tenor = (24)
                bunga = int(20000000/tenor*0.08)
                cicilan = int(20000000*bunga*tenor)
                jumlah_pengembalian= int((cicilan+bunga)*tenor)
         elif pinjaman == "D" :
                nominal_pinjaman = nominal_pinjaman_list[3]
                tenor = (24)
                bunga = int(25000000/tenor*0.08)
                cicilan = int(25000000*bunga*tenor)
                jumlah_pengembalian= int((cicilan+bunga)*tenor)
         elif pinjaman == "E" :
                nominal_pinjaman = nominal_pinjaman_list[4]
                tenor = (24)
                bunga = int(30000000/tenor*0.08)
                cicilan = int(30000000/tenor)
                jumlah_pengembalian= int((cicilan+bunga)*tenor)
         else:
                nominal_pinjaman = "-"
                tenor = "-"
                bunga = "-"
                cicilan = "-"
                jumlah_pengembalian = "-"
                print("Nominal Tidak Tersedia!!")
                Kopersi_Simpan_Pinjam()
                
         print("*****************************")
         print("Koperasi Simpan Pinjam Dika")
         print("*****Rincian Pinjaman*****")
         print("*****************************")
         print("Tanggal             : ", tanggal)
         print("Pinjaman            :", nominal_pinjaman)
         print("Tenor               :", tenor, "Bulan")
         print("Bunga               : Rp. ", bunga)
         print("Cicilan             : Rp. ", cicilan)
         print("Jumlah Pengembalian : Rp. ", jumlah_pengembalian)
         print("")
         pilihan=input("Apakah anda ingin melihat rincian yang lain ? Y/N =")

Kopersi_Simpan_Pinjam()