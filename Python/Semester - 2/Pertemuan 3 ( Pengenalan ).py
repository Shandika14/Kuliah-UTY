#******
#list
#****

#Menggambil dan melakukan output setiap item
Angka = [1,2,3,4,5]
for item in Angka :
    print(item)
print("")
    
#Menghapus data 4 pada list menggunakan index 
Angka.pop(3)
print(Angka)
print("")

#Menghapus data 4 dengan spesifik nilai pada data 
Angka.remove(3)
print(Angka)
print("")

#Mengganti nomor handphone india menjadi indonesia
No_Hp = ["+108563423", "+62901921", "+102384", "+10490211"]
print(No_Hp)
for i in range(len(No_Hp)) :
    if No_Hp[i].startswith("+10"):
        No_Hp[i] = "+62" + No_Hp[i][3:]
print(No_Hp)
print("")

#Mengganti nomer hp india menjadi indonesia dengan list baru
No_Hp_Indonesia = []
for item in No_Hp:
    if item.startswith("+10"):
        No_Hp_Indonesia.append(item.replace("+10", "+62"))
    else :
        No_Hp_Indonesia.append(item)
print(No_Hp_Indonesia)
print("")


# ***
# DICTIONARY
# ***

Buku = {
    'Indonesia' : {
        "Judul" : "Laskar Pelanggi",
        "Halaman" : 30   
    },
    'Amerika' : {
        "Judul" : "Harry Potter",
        "Halaman" : 50
    }
}
print(Buku['Amerika']['Judul'])
print("")
for key in Buku :  
    print(f"{key} -> {Buku[key]}")
    
    
for negara, info in Buku.items():
    print("Key Pertama :")
    print(negara)
    print("-----------\n")
    print(type(info))
    # Judul = info['Judul']
    # Halaman = info['Halaman']
    # print(f'{negara} -> {Judul} dan punya {Halaman} Halaman')