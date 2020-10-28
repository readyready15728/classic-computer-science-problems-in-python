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

    return True

print(linear_contains([1, 5, 15, 15, 15, 15, 20], 5)) # True
print(binary_contains(["a", "d", "e", "f", "z"], "f")) # True
print(binary_contains(["john", "mark", "ronald", "sarah"], "sheila")) #False
