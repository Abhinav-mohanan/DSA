# Stack [LIFO]

class Stack:
    def __init__(self):
        self.items = []
    
    # Add element to the top of the stack
    def push(self,item):
        self.items.append(item)
    
    # Remove and return the top element of the stack
    def pop(self):
        if not self.items:
            print('Stack is empty')
            return
        return self.items.pop()
    
    def display(self):
        print(self.items)
    
    # Return  the top element without removing it
    def peek(self):
        if not self.items:
            print("stack is empty")
            return
        return self.items[-1]


ST = Stack()
ST.push(11)
ST.push(22)
ST.push(33)
ST.push(44)

ST.pop()
ST.pop()
print(ST.peek())
ST.display()
