from collections import deque

q = deque()

# Add from right
q.append(10)
q.append(20)
q.append(30)

print(q)   # deque([10, 20, 30])

# Add from left
q.appendleft(5)

print(q)   # deque([5, 10, 20, 30])

# Remove from left
print(q.popleft())   # 5

# Remove from right
print(q.pop())       # 30

print(q)   # deque([10, 20])



'''
    append(x)       → add to RIGHT
    appendleft(x)   → add to LEFT
    pop()           → remove from RIGHT
    popleft()       → remove from LEFT

'''