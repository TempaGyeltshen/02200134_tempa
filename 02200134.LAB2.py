class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def append(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size +=1

    def prepend(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.head = self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.headself.head = new_node
        self.size +=1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range!")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.element
    
    def set(self, index, element):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range!")
        current = self.head
        for _ in range(index):
            current = current.next
        current.element = element

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(None)


if __name__ == " __main__":
    ll = LinkedList
    print(f"Element at 0: {ll.append(5)}")
    print(f"Element at 1: {ll.get(1)}")
    print(f"Element at 0: {ll.set(0,10)}")
    print(f"Element at 0: {ll.size}")
    ll.prepend(10)
    print(ll)