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
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_c -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        else:
            return self.front.item

    def get_front(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        else:
            return self.rear.item

    def size(self):
        return self.item_c


t1 = queue()

t1.enqueue(23)
t1.enqueue(43)
t1.enqueue(9)
t1.enqueue(3)
t1.enqueue(99)
print(t1.size())
