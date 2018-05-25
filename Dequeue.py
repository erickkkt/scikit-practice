class Dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return  self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def palChecker(word):
    deque = Dequeue()

    for l in word:
        deque.addFront(l)

    equal = True
    while deque.size()>1 and equal:
        first = deque.removeFront()
        last = deque.removeRear()
        if first != last:
            equal = False

    return equal


print (palChecker('abcdef'))
print(palChecker('abcba'))