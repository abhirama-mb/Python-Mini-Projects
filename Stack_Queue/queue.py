class Queue:

    def __init__(self):
        self.values = []
        self.front = 0

    def enqueue(self, x):
        self.values.append(x)

    def dequeue(self):
        if self.front == len(self.values):
            return None

        value = self.values[self.front]
        self.front += 1
        return value

    
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

print(q1.dequeue())  # 10
print(q1.dequeue())  # 20
print(q1.dequeue())  # 30
print(q1.dequeue())  # None

