from collections import namedtuple
from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint

GridLocation = namedtuple('GridLocation', ['row', 'column'])

def generate_grid(rows, columns):
    return [[choice(ascii_uppercase) for c in range(columns)] for _ in range(rows)]

def display_grid(grid):
    for row in grid:
        print(''.join(row))

def generate_domain(word, grid):
    domain = []
    height = len(grid)
    width = len(grid[0])
    length = len(word)

    for row in range(height):
        for column in range(width):
            columns = range(column, column + length + 1)
            rows = range(row, row + length + 1)

            if column + length <= width:
                # Left to right
                domain.append([GridLocation(row, c) for c in columns])
                # Diagonal towards bottom right
                if row + length <= height:
                    domain.append([GridLocation(r, column + (r - row)) for r in rows])

            if row + length <= height:
                # Top to bottom
                domain.append([GridLocation(r, column) for r in rows])
                # Diagonal towards bottom left
                if column - length >= 0:
                    domain.append([GridLocation(r, column - (r - row)) for r in rows])

    return domain

class WordSearchConstraint(Constraint):
    def __init__(self, words):
        super().__init__(words)
        self.words = words

    def satisfied(self, assignment):
        # If there are any duplicated grid locations, then there is an overlap
        all_locations = [locations for values in assignment.values() for locations in values]
        return len(set(all_locations)) == len(all_locations)

if __name__ == '__main__':
    grid = generate_grid(9, 9)
    words = [name.upper() for name in ['matthew', 'joe', 'mary', 'sarah', 'sally']]
    locations = {}

    for word in words:
        locations[word] = generate_domain(word, grid)

    csp = CSP(words, locations)
    csp.add_constraint(WordSearchConstraint(words))
    solution = csp.backtracking_search()

    if solution is None:
        print('No solution found!')
    else:
        for word, grid_locations in solution.items():
            # Random reverse half the time
            if choice([True, False]):
                grid_locations.reverse()

            for index, letter in enumerate(word):
                row, column = grid_locations[index].row, grid_locations[index].column
                grid[row][column] = letter

        display_grid(grid)
