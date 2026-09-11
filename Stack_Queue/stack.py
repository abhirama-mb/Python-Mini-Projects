# LIFO
class Stack:

    def __init__(self):
        self.values = []

    def push(self, x):
        self.values.append(x)

    def pop(self):
        if not self.values:
            return None

        return self.values.pop()

    def peek(self):
        if not self.values:
            return None

        return self.values[-1]


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.peek())   # 30
print(s.pop())    # 30
print(s.pop())    # 20
print(s.pop())    # 10
print(s.pop())    # None