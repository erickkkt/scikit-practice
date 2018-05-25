class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def parChecker(symbolString):
    s=Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

#abcba
def parSChecker(symbolString):
    s=Stack()
    index = 0
    balanced = True
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not marches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def marches(open, close):
    opens="([{"
    closes=")]}"
    return opens.index(open) == closes.index(close)

def divideBy2(decNumber):
    remStack = Stack()
    while decNumber>0:
        rem = decNumber % 2
        remStack.push(rem)
        decNumber = decNumber // 2

    binString=""
    while not remStack.isEmpty():
        binString = binString + str(remStack.pop())
    return binString

stack = Stack()
stack.push(3)
stack.push(5)
stack.push(7)
stack.push(12)

print(stack.items)
print(stack.size())
print(parChecker('(((())))'))
print(parChecker('(((())'))
print(parSChecker('{{([][])}()}'))
print(parSChecker('((([[{}]])))'))
print(divideBy2(63))