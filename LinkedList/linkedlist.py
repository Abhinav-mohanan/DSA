class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        if not self.head:
            print("Linked list is empty!.")
            return
        current = self.head
        while current:
            end_char = "->" if current.next else "\n"
            print(current.value, end=end_char)
            current = current.next

    def delete(self, data):
        if not self.head:
            return
        current = self.head
        prev = None

        # If the head node is the one to delete
        if current.value == data:
            self.head = current.next
            current = None
            return
        
        while current:
            if current.value == data:
                break
            prev = current
            current = current.next

        # if data not found
        if current is None:
            print(f'value {data} not found in the list')
            return

        # Unlink the node from linkedlist
        prev.next = current.next
        current = None


array = [1, 2, 3, 4, 5]
LL = LinkedList()
for num in array:
    LL.insert(num)

LL.display()
LL.delete(59)
LL.display()
