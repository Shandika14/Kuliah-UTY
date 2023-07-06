# Class Node untuk membuat Node pada Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class LinkedList untuk membuat Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Fungsi untuk menambahkan elemen ke Linked List
    def addNode(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    # Fungsi untuk mencetak Linked List
    def printList(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    # Fungsi untuk mengurutkan Linked List dari kecil ke besar
    def sortAscending(self):
        current = self.head
        index = None
        if self.head is None:
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next

    # Fungsi untuk mengurutkan Linked List dari besar ke kecil
    def sortDescending(self):
        current = self.head
        index = None
        if self.head is None:
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.data < index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next

# Membuat Linked List
llist = LinkedList()

# Menambahkan elemen ke Linked List
llist.addNode(23)
llist.addNode(43)
llist.addNode(12)
llist.addNode(71)
llist.addNode(87)

# Mencetak Linked List sebelum diurutkan
print("Data sebelum diurutkan:")
llist.printList()

# Mengurutkan Linked List dari kecil ke besar dan mencetaknya
llist.sortAscending()
print("Data setelah diurutkan dari kecil ke besar:")
llist.printList()

# Mengurutkan Linked List dari besar ke kecil dan mencetaknya
llist.sortDescending()
print("Data setelah diurutkan dari besar ke kecil:")
llist.printList()
