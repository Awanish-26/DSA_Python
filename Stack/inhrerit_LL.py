from .linked_list import sll


class Stack(sll):
    def __init__(self):
        super().__init__()
        self.count = 0

    def is_empty(self):
        return super().is_empty()

    def push(self, data):
        self.insert_at_start(data)
        self.count += 1

    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.count -= 1
        else:
            raise IndexError("Stack underflow")

    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise ImportError("Empty Stack")

    def size(self):
        return self.count


s1 = Stack()
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.push(60)
print()
print("top value", s1.peek())
print()
