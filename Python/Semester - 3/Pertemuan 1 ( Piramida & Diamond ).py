def tpiramida():
    print("=====| Piramida Bintang |=====")
    tinggi_piramida = int(input("Masukkan Tinggi Piramida : "))
    for i in range(tinggi_piramida):
        for j in range(1 - tinggi_piramida):
            print(" ", end="")
        for k in range(i):
            print("*", end="")
        print()
        
    for i in range(tinggi_piramida):
        for j in range(i - tinggi_piramida):
            print(" ", end="")
        for k in range(tinggi_piramida - i):
            print("*", end="")
        print()
tpiramida()        

def print_diamond():
    print("=====| Diamond Angka |=====")
    n = int(input("Masukkan Tinggi Diamond : "))
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(1, i + 1):
            print(k, end="")
        for l in range(i - 1, 0, - 1):
            print(l, end="")
        print()
        
    for i in range(n - 1, 0, -1):
        for j in range(n-i):
             print(" ", end="")
        for k in range(1, i + 1):
            print(k, end="")
        for l in range(i - 1, 0, - 1) :
            print(l, end="")
        print()
print_diamond()        