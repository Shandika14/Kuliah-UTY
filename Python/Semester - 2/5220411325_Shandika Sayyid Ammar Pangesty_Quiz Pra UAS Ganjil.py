class Node:
    def __init__(self, nama=None, tujuan=None, nokursi=None):
        self.nama = nama
        self.tujuan = tujuan
        self.nokursi = nokursi
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_data(self, nama, tujuan, nokursi):
        new_node = Node(nama, tujuan, nokursi)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_data_by_index(self, index):
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 0

        while current and count != index:
            prev = current
            current = current.next
            count += 1

        if current is None:
            return

        prev.next = current.next

    def add_data_at_index(self, index, nama, tujuan, nokursi):
        new_node = Node(nama, tujuan, nokursi)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        prev = None
        count = 0

        while current and count != index:
            prev = current
            current = current.next
            count += 1

        if current is None:
            return

        prev.next = new_node
        new_node.next = current

    def display_data(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        current = self.head
        while current:
            print("Nama    : ", current.nama)
            print("Tujuan  : ", current.tujuan)
            print("No Kursi: ", current.nokursi)
            print()
            current = current.next

# Program Utama
linked_list = LinkedList()

while True:
    print("\n======Program Input Data Tiket Travel======")
    print("\nMenu:")
    print("1. Menambahkan data")
    print("2. Menghapus data")
    print("3. Menambahkan data pada elemen ke-x")
    print("4. Menampilkan data")
    print("5. Keluar")

    choice = int(input("Masukkan pilihan: "))

    if choice == 1:
        nama = input("Masukkan Nama: ")
        tujuan = input("Masukkan Tujuan Anda: ")
        nokursi = input("Masukkan No Kursi: ")
        linked_list.add_data(nama, tujuan, nokursi)
        print("Data berhasil ditambahkan.")

    elif choice == 2:
        index = int(input("Masukkan index data yang ingin dihapus: "))
        linked_list.delete_data_by_index(index)
        print("Data berhasil dihapus.")

    elif choice == 3:
        nama = input("Masukkan Nama: ")
        tujuan = input("Masukkan Tujuan Anda:")
        nokursi = input("Masukkan No Kursi Anda: ")
        index = int(input("Masukkan posisi elemen yang ingin ditambahkan: "))
        linked_list.add_data_at_index(index, nama, tujuan, nokursi)
        print("Data berhasil ditambahkan pada elemen ke-%d." % index)

    elif choice == 4:
        print("\nData Tiket Travel:")
        linked_list.display_data()

    elif choice == 5:
        print("Anda Sudah Keluar Dari Program.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")