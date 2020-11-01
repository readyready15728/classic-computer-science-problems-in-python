from collections import deque
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

def search(initial, goal_test, successors, structure):
    frontier = structure()
    frontier.push(Node(initial, None))
    explored = {initial}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state

        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            if child in explored:
                continue

            explored.add(child)
            frontier.push(Node(child, current_node))

    return None

def dfs(initial, goal_test, successors):
    return search(initial, goal_test, successors, Stack)

def node_to_path(node):
    path = [node.state]

    while node.parent is not None:
        node = node.parent
        path.append(node.state)

    path.reverse()
    return path

class Queue:
    def __init__(self):
        self._container = deque()

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.popleft()

    def __repr__(self):
        return repr(self._container)

def bfs(initial, goal_test, successors):
    return search(initial, goal_test, successors, Queue)

class PriorityQueue:
    def __init__(self):
        self._container = []

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        heappush(self._container, item)

    def pop(self):
        return heappop(self._container)

    def __repr__(self):
        return repr(self._container)

def a_star(initial, goal_test, successors, heuristic):
    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored = {initial: 0.0}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state

        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            new_cost = current_node.cost + 1

            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))

    return None
