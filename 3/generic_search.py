from heapq import heappush, heappop

def linear_contains(iterable, key):
    for item in iterable:
        if item == key:
            return True

    return False

def binary_contains(sequence, key):
    low = 0
    high = len(sequence) - 1

    while low <= high:
        mid = (low + high) // 2

        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True

    return False

class Stack:
    def __init__(self):
        self._container = []

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)

class Node:
    def __init__(self, state, parent=None, cost=0.0, heuristic=0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

if __name__ == '__main__':
    print(linear_contains([1, 5, 15, 15, 15, 15, 20], 5)) # True
    print(binary_contains(["a", "d", "e", "f", "z"], "f")) # True
    print(binary_contains(["john", "mark", "ronald", "sarah"], "sheila")) # False
