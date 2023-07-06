class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
 
    def add_node_at_index(self, index, data):
        new_node = Node(data)
 
        # Jika linked list masih kosong
        if self.head is None:
            self.head = new_node
            return
 
        # Jika ingin menambahkan di awal
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
 
        # Mencari posisi node sebelumnya
        curr_node = self.head
        i = 0
        while i < index - 1 and curr_node is not None:
            curr_node = curr_node.next
            i += 1
 
        # Jika indeks diluar batas
        if curr_node is None:
            print("Indeks melebihi batas")
            return
 
        # Menambahkan node pada indeks tertentu
        new_node.prev = curr_node
        new_node.next = curr_node.next
        if curr_node.next is not None:
            curr_node.next.prev = new_node
        curr_node.next = new_node
 
    def delete_node_at_index(self, index):
        # Jika linked list masih kosong
        if self.head is None:
            print("List kosong")
            return
 
        # Jika ingin menghapus node pertama
        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return
 
        # Mencari posisi node
        curr_node = self.head
        i = 0
        while i < index and curr_node is not None:
            curr_node = curr_node.next
            i += 1
 
        # Jika indeks diluar batas
        if curr_node is None:
            print("Indeks melebihi batas")
            return
 
        # Menghapus node pada indeks tertentu
        if curr_node.prev is not None:
            curr_node.prev.next = curr_node.next
        if curr_node.next is not None:
            curr_node.next.prev = curr_node.prev
 
    def print_list(self):
        # Menampilkan isi dari linked list
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

# Membuat objek dari Doubly Linked List
dll = DoublyLinkedList()

# Menambahkan node pada indeks 0
dll.add_node_at_index(0, 10)

# Menambahkan node pada indeks 1
dll.add_node_at_index(1, 20)

# Menambahkan node pada indeks 2
dll.add_node_at_index(2, 30)

# Menampilkan isi dari linked list
dll.print_list()

# Menghapus node pada indeks 1
dll.delete_node_at_index(1)

# Menampilkan isi dari linked list
dll.print_list()
