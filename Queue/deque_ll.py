class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_c = 0

    def is_empty(self):
        return self.front == None

    def insert_front(self, data):
        n = Node(None, data, self.front)
        if self.is_empty():
            self.front = n
        else:
            self.front.prev = n
        self.front = n
        self.item_c += 1

    def insert_rear(self, data):
        n = Node(self.rear, data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_c += 1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("underflow")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
            self.item_c -= 1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("underflow")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
            self.item_c -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError("underflow")
        return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError("underflow")
        return self.rear.item

    def size(self):
        return self.item_c


t = Deque()

t.insert_front(36)
t.insert_front(6)
t.insert_front(3)
t.insert_front(99)
t.insert_rear(9)
print(t.get_front(), t.get_rear())
