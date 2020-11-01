import math
import random
from collections import namedtuple
from generic_search import a_star, bfs, dfs, node_to_path, Node

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

    def mark(self, path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH

        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY

        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

def euclidean_distance(goal):
    def distance(maze_location):
        x_dist = maze_location.column - goal.column
        y_dist = maze_location.row - goal.row
        return (x_dist**2 + y_dist**2)**0.5
    return distance

def manhattan_distance(goal):
    def distance(maze_location):
        x_dist = abs(maze_location.column - goal.column)
        y_dist = abs(maze_location.row - goal.row)
        return x_dist + y_dist
    return distance

if __name__ == '__main__':
    m = Maze()
    print(m)
    print()

    solution_dfs = dfs(m.start, m.goal_test, m.successors)

    if solution_dfs is None:
        print('No solution found using depth-first search!')
    else:
        path_dfs = node_to_path(solution_dfs)
        m.mark(path_dfs)
        print(m)
        print()
        m.clear(path_dfs)

    solution_bfs = bfs(m.start, m.goal_test, m.successors)

    if solution_bfs is None:
        print('No solution found using breadth-first search!')
    else:
        path_bfs = node_to_path(solution_bfs)
        m.mark(path_bfs)
        print(m)
        print()
        m.clear(path_bfs)

    distance = manhattan_distance(m.goal)
    solution_a_star = a_star(m.start, m.goal_test, m.successors, distance)

    if solution_a_star is None:
        print('No solution found using A* search!')
    else:
        path_a_star = node_to_path(solution_a_star)
        m.mark(path_a_star)
        print(m)
