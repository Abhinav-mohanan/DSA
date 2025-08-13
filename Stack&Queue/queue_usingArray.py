# QUEUE [FIFO]
class Queue:
    def __init__(self):
        self.q = []
    
    # Add a element to Queue
    def enqueue(self,data):
        self.q.append(data)
    
    # Remove a element from Queue
    def dequeue(self):
        if not self.q:
            print("Queue is empty")
            return
        return self.q.pop(0)
    
    def peek(self):
        if not self.q:
            print("Queue is empty")
            return
        return self.q[0]
    
    def display(self):
        print(self.q)
    
Q = Queue()
Q.enqueue(100)
Q.enqueue(200)
Q.enqueue(300)
Q.enqueue(400)

Q.display()
Q.dequeue()
Q.dequeue()
print('top element:- ',Q.peek())
Q.display()