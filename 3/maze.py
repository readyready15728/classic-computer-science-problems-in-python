import math
import random
from collections import namedtuple
from generic_search import dfs, bfs, node_to_path, a_star, Node

class Cell:
    EMPTY = ' '
    BLOCKED = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'

MazeLocation = namedtuple('MazeLocation', ['row', 'column'])

class Maze:
    def __init__(self, rows = 10, columns = 10, sparseness = 0.2, start = MazeLocation(0, 0), goal = MazeLocation(9, 9)):
        self._rows = rows
        self._columns = columns
        self.start = start
        self.goal = goal
        self._grid = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self._randomly_fill(rows, columns, sparseness)
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows, columns, sparseness):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self):
        output = []

        for row in self._grid:
            output.append(''.join([c for c in row]))

        return '\n'.join(output)

    def goal_test(self, ml):
        return ml == self.goal

    def successors(self, ml):
        locations = []

        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
                locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
                locations.append(MazeLocation(ml.row - 1, ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
                locations.append(MazeLocation(ml.row, ml.column + 1))
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
                locations.append(MazeLocation(ml.row, ml.column - 1))

        return locations
