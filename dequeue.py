from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue from right side
q.append(1)
q.append(2)
q.append(3)

print(f"Initial queue----{q}")

# Adding elements to a queue from left
q.appendleft(0)
q.appendleft(-1)
q.appendleft(-2)

print(f"append_left  queue----{q}")

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.pop())
print(q.popleft())


print("\nQueue after removing elements")
print(q)