def mencari_potongan_kata():
    teks = "Tomat merupakan salah satu jenis sayuran yang banyak digemari dan ditanam di indonesia. Hal ini dikarenakan tomat memiliki banyak manfaat"
            
    pesan = ["Aku Suka Hari ini", "Aku Benci Ketika terjatuh", "Orang yang Baik adalah orang yang membantumu semangat" ,
            "Aku Ingat Dia", "Senyum mu menyegarkan hati"]
   
    #isilah bagian yang di garis bawahi tersebut untuk membenarkan program sesuai yang diperintah        
    posisi_kata = 0
    for i in range(len(pesan)):
        if "Suka" in pesan[i]:
            posisi_kata = i
    potongan_kata = teks[6:17]
            
    for kata in pesan:
        if kata == pesan[posisi_kata]:
            print(kata)
        
    """
    HINT

    1. Gunakan List yang ada
    2. Gunakan slicing untuk mengambil potongan Kata
    3. Gunakan pengkodisian untuk mencocokan
    """
mencari_potongan_kata()

"""
Output Seharusnya akan tampil seperti ini
Aku Suka Hari ini
"""
