# Author By:
# 522411325-Shandika Sayyid Ammar Pangesty
import random
import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


def bubble_sort(llist):
    if llist.head is None or llist.head.next is None:
        return llist
    sorted = False
    while not sorted:
        sorted = True
        current = llist.head
        while current.next:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                sorted = False
            current = current.next
    return llist


def filter_adults(llist, max_adult_age):
    if llist.head is None:
        return LinkedList(), LinkedList(), LinkedList()
    adults = LinkedList()
    non_adults = LinkedList()
    exceeded_age = LinkedList()
    current = llist.head
    while current:
        if current.data < 300:
            non_adults.insert(current.data)
        elif current.data > max_adult_age:
            exceeded_age.insert(current.data)
        else:
            adults.insert(current.data)
        current = current.next
    return adults, non_adults, exceeded_age


def print_menu():
    print("")
    print("Menu:")
    print("1. Tampilkan Data Umur Ayam")
    print("2. Urutkan Data Umur Ayam")
    print("3. Saring Data Ayam Dewasa dan Belum Dewasa")
    print("4. Keluar")


if __name__ == '__main__':
    os.system('cls')
    arr = []
    max_adult_age = 600
    ayam_list = LinkedList()
    print("|===========================================|")
    print("|=====| PROGRAM PENGECEKAN UMUR AYAM |======|")
    print("|===========================================|")
    while True:
        print_menu()
        choice = input("Pilih Menu: ")
        if choice == '1':
            arr = [random.randint(1, 1000) for _ in range(20)]
            ayam_list = LinkedList()
            for ayam in arr:
                ayam_list.insert(ayam)
            print("===> Data Umur Ayam <===")
            print(arr)
        elif choice == '2':
            sorted_ayam_list = bubble_sort(ayam_list)
            sorted_arr = []
            current = sorted_ayam_list.head
            while current:
                sorted_arr.append(current.data)
                current = current.next
            print("===> Data Umur Ayam Setelah Diurutkan <===")
            print(sorted_arr)

        elif choice == '3':
            adults_list, non_adults_list, exceeded_age_list = filter_adults(ayam_list, max_adult_age)
            adults_arr = []
            current = adults_list.head
            while current:
                adults_arr.append(current.data)
                current = current.next
            print("===> Data Umur Ayam yang Dewasa <===")
            print(adults_arr)
            print("")
            non_adults_arr = []
            current = non_adults_list.head
            while current:
                non_adults_arr.append(current.data)
                current = current.next
            print("===> Data Umur Ayam yang Belum Dewasa <===")
            print(non_adults_arr)
            print("")
            exceeded_age_arr = []
            current = exceeded_age_list.head
            while current:
                exceeded_age_arr.append(current.data)
                current = current.next
            print("===> Data Umur Ayam yang Melebihi Batas Umur <===")
            print(exceeded_age_arr)

        elif choice == '4':
            print("Terima Kasih Telah Menggunakan Program Ini.")
            print("======| PROGRAM CLOSED |======")
            exit()

        else:
            print("Pilihan Tidak Valid. Silakan Pilih Menu Yang Tersedia.")