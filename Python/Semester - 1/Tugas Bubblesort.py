#Bubble Sort
def tukar(data1,i,j):
    data1[i],data1[j]= data1[j],data1[i]
def bubblesort(data):
    ubah = True
    sesi = len(data)
    while sesi > 1 and ubah:
        ubah = False
        j = 1
        while j < sesi:
            if data[j]<data[j-1]:
                ubah = True
                tukar(data,j,j-1)
            j+=1
        print(data)
        if not ubah:
            print("Hasil Akhir = %s" %str(data))
        sesi-=1
print("==========================================")
print("Sebelum Bubble Sort")
a=[4,13,67,35,21,77,89,67]
print(a)
print("Setelah Bubble Sort")
bubblesort(a)
print("")

def bubblesort (x):
    for passnum in range(len(x)-1,0,-1):
        for i in range(passnum):
            if x[i]>x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
c =[23,7,32,99,4,14,11,20]
print("===========================================")
print("Sebelum Bubble Sort")
print(c)
print("Setelah Bubbel Sort")
bubblesort(c)
print(c)
print("")


#Selection Sort
def tukar(data3,i,j):
    data3[i],data3[j]=data3[j],data3[i]
def Selection(data):
    perubahan = True
    sesi = 0
    while sesi < len(data)-1 and perubahan:
        perubahan = False
        dataterendah = sesi
        datalanjutan = dataterendah + 1
        while datalanjutan < len(data):
            if data[dataterendah] > data[datalanjutan]:
                dataterendah= datalanjutan
            datalanjutan += 1
        if datalanjutan != sesi:
            tukar(data,dataterendah,sesi)
            perubahan = True
        print(data)
        if not perubahan:
            print("Hasil Akhir = %s" %str(data))
        sesi += 1
print("===============================================")
print("Sebelum Selection Sort")
d = [54,26,13,93,17,77,44,31]
print(d)
print("Setelah Selection Sort")
Selection(d)
print("")

def Selectionsort(data4):
      for slot in range(len(data4)-1):
        position = slot
        for location in range(len(data4)-1,slot,-1):
            if data4[location]<data4[position]:
                position = location

        temp = data4[slot]
        data4[slot] = data4[position]
        data4[position] = temp
e = [54,26,93,17,77,31,44,55,20]
print("============================================")
print("Sebelum Selection Sort")
print(e)
print("Setelah Selection Sort")
Selectionsort(e)
print(e)
print("")

#InsertionSort
def insertionsort(data5):
    for index in range(1, len(data5)):
        x = data5[index]
        y = index - 1
        while y >=0 and data5[y] > x:
            data5[y + 1 ] = data5[y]
            y -= 1
        data5[y + 1] = x
    index = 0
print("====================================================")
panjangList = int(input("Input Panjang List Yang Diinginkan = "))
data5 = []
for i in range(1, panjangList+1):
    angka = int(input("Masukkan Angka Yang Ke %i Untuk List = " %i))
    data5.append(angka)
print("Sebelum Di Insertion Sort")
print(data5)
insertionsort(data5)
print("Setelah Di Insertion Sort")
print(data5)
print("")

def insertion_sort(data6):
    for i in range(1, len (data6)):
        x = data6[i]
        j = i-1
        while j >=0 and x < data6[j] :
                data6[j+1] = data6[j]
                j -= 1
        data6[j+1] = x

g = [12,11,13,5,6]
insertion_sort(g)
print("===============================================")
print("Hasil : ")
for i in range(len(g)):
    print("%d" %g[i])
print("")

# Quick Sort
def quicksort(alist):
  quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
 if first<last:
    splitpoint = partition(alist,first,last)
    quickSortHelper(alist,first,splitpoint-1)
    quickSortHelper(alist,splitpoint+1,last)
def partition(alist,first,last):
  pivotvalue = alist[first]
  leftmark = first+1
  rightmark = last
  done = False
  while not done:
    while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
      leftmark = leftmark + 1
    while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
      rightmark = rightmark - 1
    if rightmark < leftmark:
       done = True
    else:
       temp = alist[leftmark]
       alist[leftmark] = alist[rightmark]
       alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
print("===============================================")
print("Sebelum Quick Sort")
print(alist)
print("Setelah Quick Sort")
quicksort(alist)
print(alist)
print("")

def partition(l, bwh, atas):
  pivot = l[bwh]
  pos_batas = bwh+1
  for j in range(bwh+1,atas):
    if l[j] < pivot:
      l[pos_batas],l[j] = l[j],l[pos_batas]
      pos_batas += 1
  l[pos_batas-1],l[bwh] = l[bwh],l[pos_batas-1]
  return pos_batas

def quicksort(l, bwh, atas):
    if atas<= bwh:
     return
    q = partition(l, bwh, atas)
    quicksort(l, bwh, q-1)
    quicksort(l, q, atas)
    return l
angka = [34,21,45,32,12,31,19,23,54,31,25,27]
print("===============================================")
print('Sebelum Sort:',angka)
quicksort(angka,0,len(angka))
print('Setelah Sort:',angka)
print("")

# Marge Sort
def merge_sort(list_bilangan):
    jumlah_bilangan = len(list_bilangan)
    if jumlah_bilangan > 1:
        posisi_tengah = len(list_bilangan)//2
        potongan_kiri = list_bilangan[:posisi_tengah]
        potongan_kanan = list_bilangan[posisi_tengah:]

        merge_sort(potongan_kiri)
        merge_sort(potongan_kanan)

        jumlah_bilangan_kiri = len(potongan_kiri)
        jumlah_bilangan_kanan = len(potongan_kanan)
        c_all,c_kiri,c_kanan = 0,0,0
        print('Sebelum Merge:',list_bilangan)
        print('Potongan Sebelum Merge:',potongan_kiri,':',potongan_kanan)
        while c_kiri < jumlah_bilangan_kiri or c_kanan < jumlah_bilangan_kanan:
            if c_kiri == jumlah_bilangan_kiri:
                list_bilangan[c_all] = potongan_kanan[c_kanan]
                c_kanan = c_kanan + 1   
            elif c_kanan == jumlah_bilangan_kanan:
                list_bilangan[c_all] = potongan_kiri[c_kiri]
                c_kiri = c_kiri + 1
            elif potongan_kiri[c_kiri] >= potongan_kanan[c_kanan]:
                list_bilangan[c_all] = potongan_kiri[c_kiri]
                c_kiri = c_all + 1
            else:
                list_bilangan[c_all] = potongan_kanan[c_kanan]
                c_kanan = c_kanan + 1
            c_all = c_all + 1
            print('Setelah Merge:',list_bilangan)
            print()

angka = [6,5,3,1,8,7,2,4]
print('Sebelum Sort:',angka)
print("")
merge_sort(angka)
print('Setelah Sort:',angka)
print("")

# Radix Sort
def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = n - 1
    while i>=0:
        index = (arr[i] / exp1)
        output[count[int(index % 10)]-1] = arr[i]
        count[int(index % 10)] -=1
        i -= 1

    i=0
    for i in range(0, len(arr)):
        arr[i]= output[i]

def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10
arr = [170,45,75,90,802,24,2,66]
radixSort(arr)
for i in range(len(arr)):
    print(arr[i])
print("")
        
# Sequential Search
Data = [10,4,2,3,7,1,6,8]
caridata = int(input("Masukkan Nilai Yang Dicari:"))
ditemukan = False
for i in range(0, len(Data)):
    print(Data[i])
    if Data[i] == caridata:
        ditemukan = True
        break
if ditemukan:
    print("Data Ditemukan!!")
else:
    print("Data Tidak Ditemukan!!")
print("")

# Linear Search
def linearSearch(Data,list):
    ditemukan = False
    posisi = 0
    while posisi < len(list) and not ditemukan:
        if list[posisi] == Data:
            ditemukan = True
        posisi = posisi + 1
    return ditemukan
tas = ['Buku','Pensil','Pulpen','Note Book','Laptop','Handphone']
Data = input("Apa Yang Ingin Kamu Cari Didalam Tas ?")
temukanitem = linearSearch(Data,tas)
if temukanitem:
    print("Ya, Benda Tersebut Berada Didalam Tas")
else:
    print("Oops, Benda Tersebut Tidak Berada Didalam Tas")
print("")

# Linear Search Dengan Sentinel
Data= [114,110,77,112,65,80,80,90,113,109,110,89,108,85,87,65,90,95,100]
caridata = 109
jumlah = len(Data)
Data.append(caridata)
index = 0
while Data[index] != caridata:
    index+=1

if index < jumlah:
    print('Nilai',caridata,'Ditemukan Pada Index',index)
else:
    print('Nilai',caridata,'Tidak Ditemukan')
print("")

# Binary Search
Data = [1,3,4,6,7,8,10,13,14,18,19,21,24,3,7,40,45,71]
caridata= 7
print('Mencari Nilai',caridata,'Dengan Binary Search','Pada List',Data)
ditemukan = False
batas_awal = 0
batas_akhir = len(Data) - 1
while not ditemukan and batas_awal <= batas_akhir:
    pos_cari = batas_awal + (batas_akhir-batas_awal)//2
    print('Posisi Pencarian: index', pos_cari,'Dengan Nilai',Data[pos_cari])
    if Data[pos_cari] == caridata:
        ditemukan = True
    elif Data[pos_cari] > caridata:
        batas_akhir = pos_cari-1
    else:
        batas_awal = pos_cari+1

if ditemukan:
    print('Nilai',caridata,'Ditemukan Pada Index',pos_cari)
else:
    print('Nilai',caridata,'Tidak Ditemukan')

def binarySearch(data, posisi, x, cari):
    if x >= posisi:
        mid = posisi + (x - posisi) // 2
        if data[mid] == cari:
            return mid
        
        elif data[mid] > cari:
            return binarySearch(data, posisi, mid-1, cari)

        else:
            return binarySearch(data, mid+1, x, cari)
    else:
        return -1

data =[2,3,4,10,40]
cari = int(input("Masukkan Data Yang Akan Dicari="))
result = binarySearch(data,0,len(data)-1,cari)
if result != -1:
    print("Data Ditemukan!")
else:
    print("Data Tidak Ditemukan!")
print("")

#InterpolationSearch
def interpolationSearch(arr, bwh, atas, x):
    if (bwh <= atas and x >= arr[bwh] and x <= arr[atas]):
        pos = bwh + ((atas - bwh) // (arr[atas] - arr[bwh]) *
                    (x - arr[bwh]))
 
        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                       atas, x)
        if arr[pos] > x:
            return interpolationSearch(arr, bwh,
                                       pos - 1, x)
    return -1

arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)

x = 18
index = interpolationSearch(arr, 0, n - 1, x)
 
if index != -1:
    print("Data Ditemukan Pada Index", index)
else:
    print("Data Tidak Ditemukan")