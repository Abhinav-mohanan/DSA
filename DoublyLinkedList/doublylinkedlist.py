class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def display(self):
        if not self.head:
            print("Linked list is empty")
            return
        current  = self.head
        while current:
            end_char = '<->' if current.next else '\n'
            print(current.value,end=end_char)
            current = current.next
    
    def delete(self,data):
        if not self.head:
            print("Linked list is empty")
            return
        current = self.head
        if current.value == data:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return
        while current and current.value != data:
            current = current.next
        if current is None:
            print(f"Value {data} not present in Doubly linked list")
            return
        
        # If the node to be deleted is not the last
        if current.next:
            current.next.prev = current.prev
            
        # Update previous node's next pointer
        if current.prev:
            current.prev.next = current.next
        current = None
        

nums = [10,20,30,40,50]
DL = DoublyLinkedList()
for num in nums:
    DL.insert(num)
DL.display()
DL.delete(50)
DL.display()