class queue:
    def __init__(self):
        self.i = []

    def is_empty(self):
        return len(self.i) == 0

    def enqueue(self, data):
        self.i.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.i.pop(0)
        else:
            raise IndentationError("Queue Underflow")

    def get_front(self):
        if not self.is_empty():
            return self.i[0]
        else:
            raise IndexError("Queue Underflow")

    def get_rear(self):
        if not self.is_empty():
            return self.i[-1]
        else:
            raise IndexError("Queue Underflow")

    def size(self):
        return len(self.i)


q1 = queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])

q1.enqueue(30)
q1.enqueue(10)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(90)
q1.enqueue(36)
q1.enqueue(3)
print("Front=", q1.get_front(), "Rear=", q1.get_rear())
try:
    q1.dequeue()
    print("Queue has now", q1.size(), "elements")
except IndexError as e:
    print(e.args[0])
