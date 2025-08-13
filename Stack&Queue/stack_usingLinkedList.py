class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# STACK [LIFO]
class Stack:
    def __init__(self):
        self.head = None
    
    # push an element onto stack
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # pop the top element
    def pop(self):
        if not self.head:
            print('Stack is empty')
            return 
        popped_value = self.head.value
        self.head = self.head.next
        return popped_value
    
    def display(self):
        if not self.head:
            print("Stack is empty")
            return
        current = self.head
        while current:
            print(current.value,end=' ')
            current = current.next
            
    # Return the top element
    def peek(self):
        if not self.head:
            print("Stack is empty")
            return
        return self.head.value

ST = Stack()
ST.push(99)
ST.push(89)
ST.push(79)
ST.push(69)

ST.display()
print()
print('popped value :- ',ST.pop())
print('popped value :- ',ST.pop())
print('Top value :- ',ST.peek())
ST.display()