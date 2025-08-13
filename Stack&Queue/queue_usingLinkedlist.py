class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# QUEUE - [FIFO] 
class Queue:
    def __init__(self):
        self.head = None
    
    # Add element to Queue
    def enqueue(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    # Remove element from Queue
    def dequeue(self):
        if not self.head:
            print("Queue is empty")
            return
        dequeued_value = self.head.value
        self.head = self.head.next
        return dequeued_value
    
    def display(self):
        if not self.head:
            print("Queue is empty")
            return
        current = self.head
        while current:
            print(current.value,end=' ')
            current = current.next
    
    def peek(self):
        if not self.head:
            print('Queue is empty')
            return
        return self.head.value 
    

Q = Queue()
Q.enqueue(9)
Q.enqueue(8)
Q.enqueue(7)
Q.enqueue(6)
Q.display()

print()
print('Top value :- ',Q.peek())
Q.dequeue()
Q.dequeue()
Q.display()