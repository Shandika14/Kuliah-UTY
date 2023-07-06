def pemilihan_laptop():
    print("===========Program Pemilihan Laptop==========")
    laptop = str(input("Masukkan Nama Laptop Yang Diinginkan : "))
    if laptop == "HP 14S DQ5000TU":
        print("Harga Laptop Ini 11jt")
        print("Prosesor Intel Core i5")
        print("RAM 8GB")
        print("SSD 512GB")
        print("OS Windows 11 HOME")
    elif laptop == "HP OMEN 16":
        print("Harga Laptop Ini 30jt")
        print("Prosesor Intel Core i9")
        print("RAM 32 GB")
        print("SSD 1TB")
        print("OS Windows 11 HOME")
    elif laptop == "ACER NITRO 5":
        print("Harga Laptop Ini 13jt")
        print("Prosesor Intel Core i5")
        print("RAM 8GB")
        print("SSD 512GB")
        print("OS Windows 11 HOME")
    else:
        print("Tidak Ada Laptop Yang Cocok")
    
    print("")
    print("=====Perulangan=====")
    count = 0
    while count < 4:
        print(laptop, end=' ')
        count = count + 1
    print("")
    print("")
    
    print("=====List=====")
    x = [laptop, 'Harga 30 Jt', 'Core i9', 'RAM 32Gb', 'SSD 1TB', 'OS Windows 11 Home']
    print(x)
    print("")
    
    print("=====Tuple=====")
    Data = tuple(laptop)
    Subdata1 = tuple('Harga Laptop 30 Jt')
    Subdata2 = tuple('Prosesor Intel Core i9')
    Subdata3 = tuple('RAM 32 GB')
    print(Data)
    print(Subdata1)
    print(Subdata2)
    print(Subdata3)
    print("")
    
    print("=====Dictionary=====")
    dict_data = {
        'Nama Laptop': laptop,
        'Harga': '30 Jt',
        'Prosesor': 'Intel Core i9',
        'RAM': '32Gb',
        'SSD': '1TB',
    }
    print("dict_data['Nama Laptop']: ", dict_data['Nama Laptop'])
    print("dict_data['Harga']: ", dict_data['Harga'])
    print("dict_data['Prosesor']: ", dict_data['Prosesor'])
    print("dict_data['RAM']: ", dict_data['RAM'])

pemilihan_laptop()
