class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.item_c = 0

    def is_empty(self):
        return self.front == None

    def enqueue(self, data):
        n = Node(data)
        if self.front == None:
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_c += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        elif self.front==self.rear:
            

