#isilah bagian yang di garis bawahi tersebut untuk membenarkan program sesuai yang diperintah
def ganti_ending(kalimat, kata_lama, kata_baru):
    if kalimat.endswith(kata_lama):
        i = len(kata_lama)
        kalimat_baru = kalimat[:-i] + kata_baru
        return kalimat_baru
"""
HINT

1. Gunakan fungsi untuk mengambil kata terakhir dari suatu kalimat
2. Gunakan panjang dari kata yang akan diganti untuk menempatkan kata baru
"""

print(ganti_ending("Aku Ingin pergi", 'pergi', 'makan'))

"""
Output Seharusnya seperti ini

Aku Ingin makan
"""