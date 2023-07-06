print("============= NO 1 Ganjil =============")
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
    
    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
    
    def max(self):
        max_value = self.head.value
        current = self.head
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
    
if __name__ == "__main__":
    ll = LinkedList(3)
    ll.append(10)
    ll.append(7)
    ll.append(8)
    print(f'Maximal : {ll.max()}')

print("")
print("========== NO 3 Ganjil&Genap ==========")
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def append_list(self, new_list):
        for item in new_list:
            new_node = LinkedList(item)
            current_node = self
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
    
    def print_list(self):
        current_node = self
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next
            
if __name__ == "__main__":
    ll = LinkedList(3)
    ll.append_list([2,4,8,4,6])
    ll.print_list()