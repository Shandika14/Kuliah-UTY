def Mengubah_Kata_Kunci(kalimat, kata):
    hasil = []
    for pesan in kalimat:
        if pesan.lower() == "aku ingat dia":
            continue
        for kunci in kata:
            if kunci.lower() in pesan.lower():
                pesan = pesan.replace(kunci, kunci.upper())
        hasil.append(pesan)
    return hasil
pesan = ["Aku Suka Hari ini", "Aku Benci Ketika terjatuh", "Orang yang Baik adalah orang yang membantumu semangat" ,
             "Aku Ingat Dia", "Senyum mu menyegarkan hati"]
kata_kunci = ["Suka", "Benci", "Baik", "hati"]
     
#isilah bagian yang di garis bawahi tersebut untuk membenarkan program sesuai yang diperintah            
hasil = Mengubah_Kata_Kunci(pesan, kata_kunci)
for pesan in hasil:
    print(pesan)
#hint 
    # gunakan perulangan untuk mengambil datanya
    # gunakan pengkodisian untuk mencari data yang diinginkan

"""
Output Nya seharusnya seperti ini 
Aku SUKA Hari ini
Aku BENCI Ketika terjatuh
Orang yang BAIK adalah orang yang membantumu semangat
Senyum mu menyegarkan HATI
"""