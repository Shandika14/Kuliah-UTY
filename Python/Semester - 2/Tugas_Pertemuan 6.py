class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def sort_ascending(self):
        current_node = self.head
        while current_node is not None:
            temp_node = current_node.next
            while temp_node is not None:
                if current_node.data > temp_node.data:
                    current_node.data, temp_node.data = temp_node.data, current_node.data
                temp_node = temp_node.next
            current_node = current_node.next

    def sort_descending(self):
        current_node = self.head
        while current_node is not None:
            temp_node = current_node.next
            while temp_node is not None:
                if current_node.data < temp_node.data:
                    current_node.data, temp_node.data = temp_node.data, current_node.data
                temp_node = temp_node.next
            current_node = current_node.next

linked_list = LinkedList()
linked_list.add_node(23)
linked_list.add_node(43)
linked_list.add_node(12)
linked_list.add_node(71)
linked_list.add_node(87)

print("Sebelum diurutkan:")
linked_list.print_list()

print("\nSetelah diurutkan secara ascending:")
linked_list.sort_ascending()
linked_list.print_list()

print("\nSetelah diurutkan secara descending:")
linked_list.sort_descending()
linked_list.print_list()
