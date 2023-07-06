#Author By : 
# 1. 5220411304 Ahrenz Dianto
# 2. 5220411314 Firza Mauli
# 3. 5220411315 Restyandito Vega M
# 4. 5220411325 Shandika Sayyid Ammar Pangesty

import random
import os 

def Tahun_Kabisat(tahun):
    if tahun % 4 == 0:
        if tahun % 100 == 0:
            if tahun % 400 == 0:
                return True
            else:
                return False    
        else:
            return True
    else:
        return False

def Level_1(nyawa):
    print("Selamat Datang di Level 1")
    print("")
    score = 0
    jawaban_benar = 0

    for _ in range(10):
        if nyawa == 0:
            print("")
            print("GAME OVER, Nyawa Anda Sudah Habis ")
            return score
        
        bil1 = random.randint(1, 10)
        bil2 = random.randint(1, 10)
        jawaban = bil1 + bil2

        print(f"Berapakah hasil dari {bil1} + {bil2}?")
        jawaban_pemain = int(input("Masukkan Jawaban Anda: "))

        if jawaban_pemain == jawaban:
            print("Jawaban Anda benar!")
            score += 2
            jawaban_benar += 1
        else:
            print(f"Maaf, jawaban Anda salah. Jawaban yang benar adalah {jawaban}.")
            nyawa -= 1
            score -= 0

        print(f"Skor Anda: {score}/20 | Nyawa Anda: {'❤️'' '*nyawa}")

    print(f"Anda berhasil menjawab {jawaban_benar} dari 10 soal dengan benar, skor Anda: {score}/20")
    if jawaban_benar == 10:
        print(f"Selamat Anda Sudah Mengerjakan Soal Di Level Ini Dengan Benar")
    return score


def Level_2(nyawa):
    print(f"Selamat Datang di Level 2")
    print("")
    score = 0
    jawaban_benar = 0
    
    for _ in range(10):
        if nyawa == 0:
            print("")
            print("GAME OVER, Nyawa Anda Sudah Habis ")
            return score
        
        bil1 = round(random.uniform(1, 100),1)
        bil2 = random.randint(1, 10)
        jawaban = bil1 - bil2

        print(f"Berapakah hasil dari {bil1} - {bil2}?")
        jawaban_pemain = float(input("Masukkan Jawaban Anda: "))

        if jawaban_pemain == jawaban:
            print("Jawaban Anda benar!")
            score += 2
            jawaban_benar += 1
        else:
            print(f"Maaf, jawaban Anda salah. Jawaban yang benar adalah {jawaban}.")
            nyawa -= 1
            score -= 0

        print(f"Skor Anda: {score}/20 | Nyawa Anda: {'❤️'' '*nyawa}")

    print(f"Anda berhasil menjawab {jawaban_benar} dari 10 soal dengan benar, skor Anda: {score}/20")
    if jawaban_benar == 10:
        print(f"Selamat Anda Sudah Mengerjakan Soal Di Level Ini Dengan Benar")
    return score


def Level_3(nyawa):
    print(F"Selamat Datang di Level 3")
    print("")
    score = 0
    jawaban_benar = 0
    
    for _ in range(10):
        if nyawa == 0:
            print("")
            print("GAME OVER, Nyawa Anda Sudah Habis ")
            return score
        
        bil1 = round(random.uniform(1, 50),1)
        bil2 = random.randint(1, 10)
        jawaban = bil1 * bil2

        print(f"Berapakah hasil dari {bil1} x {bil2}?")
        jawaban_pemain = float(input("Masukkan Jawaban Anda: "))

        if jawaban_pemain == jawaban:
            print("Jawaban Anda benar!")
            score += 2
            jawaban_benar += 1
        else:
            print(f"Maaf, jawaban Anda salah. Jawaban yang benar adalah {jawaban}.")
            nyawa -= 1
            score -= 0

        print(f"Skor Anda: {score}/20 | Nyawa Anda: {'❤️'' '*nyawa}")

    print(f"Anda berhasil menjawab {jawaban_benar} dari 10 soal dengan benar, skor Anda: {score}/20")
    if jawaban_benar == 10:
        print(f"Selamat Anda Sudah Mengerjakan Soal Di Level Ini Dengan Benar")
    return score


def Level_4(nyawa):
    print(F"Selamat Datang di Level 4")
    print("")
    score = 0
    jawaban_benar = 0
    
    for _ in range(10):
        if nyawa == 0:
            print("")
            print("GAME OVER, Nyawa Anda Sudah Habis ")
            return score
        
        bil1 = random.randint(1, 100)
        bil2 = random.randint(1, 100)
        pertanyaan = bil1 * bil2

        print(f"Berapakah hasil dari {pertanyaan} ÷ {bil2}?")
        jawaban_pemain = int(input("Masukkan Jawaban Anda: "))

        if jawaban_pemain == bil1:
            print("Jawaban Anda benar!")
            score += 2
            jawaban_benar += 1
        else:
            print(f"Maaf, jawaban Anda salah. Jawaban yang benar adalah {bil1}.")
            nyawa -= 1
            score -= 0

        print(f"Skor Anda: {score}/20 | Nyawa Anda: {'❤️'' '*nyawa}")
    
    print(f"Anda berhasil menjawab {jawaban_benar} dari 10 soal dengan benar, skor Anda: {score}/20")
    if jawaban_benar == 10:
        print(f"Selamat Anda Sudah Mengerjakan Soal Di Level Ini Dengan Benar")
    return score


def Level_5(nyawa):
    print(F"Selamat Datang di Level 5")
    print("")
    score = 0
    jawaban_benar = 0
    
    for _ in range(10):
        if nyawa == 0:
            print("")
            print("GAME OVER, Nyawa Anda Sudah Habis ")
            return score
        
        bil1 = random.randint(1, 100)
        bil2 = random.randint(1, 10)
        jawaban = bil1 % bil2

        print(f"Berapakah hasil dari {bil1} % {bil2}?")
        jawaban_pemain = int(input("Masukkan jawaban Anda: "))

        if jawaban_pemain == jawaban:
            print("Jawaban Anda benar!")
            score += 2
            jawaban_benar += 1
        else:
            print(f"Maaf, jawaban Anda salah. Jawaban yang benar adalah {jawaban}.")
            nyawa -= 1
            score -= 0

        print(f"Skor Anda: {score}/20 | Nyawa Anda: {'❤️'' '*nyawa}")

    print(f"Anda berhasil menjawab {jawaban_benar} dari 10 soal dengan benar, skor Anda: {score}/20")
    if jawaban_benar == 10:
        print(f"Selamat Anda Sudah Mengerjakan Soal Di Level Ini Dengan Benar")
    return score
    

def main():
    os.system('cls')
    print("===== SELAMAT DATANG DI HELL QUIZ =====")
    while True:
        nama = input("Masukkan Nama Anda: ")
        tahun_lahir = int(input("Masukkan Tahun Lahir Anda: "))

        if Tahun_Kabisat(tahun_lahir):
            print(f"Selamat {nama}! Tahun kelahiran Anda ({tahun_lahir}) Adalah Tahun Kabisat!")
            nyawa = 5
            print(f"Karena Tahun Kelahiran Anda Adalah Tahun Kabisat Nyawa Anda {'❤️'' '*nyawa}")
        else:
            print(f"Maaf {nama}, Tahun kelahiran Anda ({tahun_lahir}) bukan tahun kabisat.")
            nyawa = 3
            print(f"Karena Tahun Kelahiran Anda Bukan Tahun Kabisat Nyawa Anda {'❤️'' '*nyawa}")
        total_skor = 0
        while True:
            print("\nMain Menu: \n1. Keluar \n2. Restart \n3. Pilih level")
            opsi = input("Pilih Menu Yang Anda Inginkan: ")

            if opsi == "1":
                print("Terima Kasih Telah Bermain!")
                exit()
            elif opsi == "2":
                break
            elif opsi == "3":
                while True:
                    print("")
                    print("\nSilahkan Pilih Level Yang Anda Inginkan:")
                    print("1. Level 1 (Penjumlahan)")
                    print("2. Level 2 (Pengurangan)")
                    print("3. Level 3 (Perkalian)")
                    print("4. Level 4 (Pembagian)")
                    print("5. Level 5 (Mod)")
                    print("6. Total Skor")
                    print("7. Main Menu")

                    level = input("Masukkan Level Yang Anda Inginkan: ")
                    if level == "1":
                        skor_level = Level_1(nyawa)
                        total_skor += skor_level
                        print("Level 1 (Penjumlahan)")
                        continue
                    elif level == "2":
                        skor_level = Level_2(nyawa)
                        total_skor += skor_level
                        print("Level 2 (Pengurangan)")
                        continue
                    elif level == "3":
                        skor_level = Level_3(nyawa)
                        total_skor += skor_level
                        print("Level 3 (Perkalian)")
                        continue
                    elif level == "4":
                        skor_level = Level_4(nyawa)
                        total_skor += skor_level
                        print("Level 4 (Pembagian)")
                        continue
                    elif level == "5":
                        skor_level = Level_5(nyawa)
                        total_skor += skor_level
                        print("Level 5 (Mod)")
                        continue
                    elif level == "6":
                        continue
                    else:
                        print("Maaf, Pilihan Level Tidak Valid.")

                print("")
                print(f"Skor Total Anda Dari Semua Level Yang Telah Dimainkan: {total_skor}/100")
                exit()

if __name__ == '__main__':
    main()

