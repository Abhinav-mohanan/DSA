class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
    
    def display(self):
        if not self.head:
            print("Circular linked list is empty")
            return
        current = self.head
        while True:
            print(current.value,end='<->')
            current = current.next
            if current == self.head:
                break
    
    def delete(self,data):
        if not self.head:
            print("circular linked list is empty")
            return
        
        current = self.head
        prev = None

        # Only one node
        if current.next == self.head and current.value == data:
            self.head = None
            return
        
        # Deleting head node
        if current.value == data:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = current.next
            self.head = current.next
            return
        
        # Deleting non-head node
        while current.next != self.head:
            prev = current
            current = current.next
            if current.value == data:
                prev.next = current.next
                return
        print(f'value {data} not found in circular linked list')
    
    
nums = [12,23,34,45,56]
CL = CircularLinkedList()
for num in nums:
    CL.insert(num)
CL.display()
print()
CL.delete(56)
CL.display()
