# Bintang Pola Jam Pasir
print("======= Bintang Pola Jam Pasir =======")
n = int (input("Masukkan Batas : "))
i=1
j=n
while i<=n:
     print((i*' ')+j*'* ')
     j=j-1
     i=i+1

i=1
j=n
while i<=n:
     print((j*' ')+i*'* ')
     j=j-1
     i=i+1

# ASCENDING
print(" ")
print("====== Looping Nama Dengan Ascending =====")
nama = ['S','H','A','N','D','I','K','A',' ','S','A','Y','Y','I','D', ' ','A','M','M','A','R',' ','P','A','N','G','E','S','T','Y']
for i in nama:
    print (i)

# DISCENDING
print(" ")
print("===== Looping Nama Dengan Descending =====")
nama.reverse()
for i in nama:
    print (i)


