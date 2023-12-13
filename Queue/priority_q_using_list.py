"""     Priority queue using list      """


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data, priorty):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priorty:
            index += 1
        self.items.insert(index, (data, priorty))

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue is Empty")
        else:
            return self.items.pop(0)[0]

    def size(self):
        return len(self.items)


# driver code

p = PriorityQueue()

p.push("Amit", 4)
p.push("Ambika", 2)
p.push("Amitesh", 9)
p.push("Alok", 1)
p.push("BSDK", 12)

while not p.is_empty():
    print(p.pop())
