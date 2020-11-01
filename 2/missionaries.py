from generic_search import bfs, node_to_path, Node
from inspect import cleandoc

MAX_NUM = 3

class MCState:
    def __init__(self, missionaries, cannibals, boat_on_west_bank):
        self.west_bank_missionaries = missionaries
        self.west_bank_cannibals = cannibals
        self.east_bank_missionaries = MAX_NUM - self.west_bank_missionaries
        self.east_bank_cannibals = MAX_NUM - self.west_bank_cannibals
        self.boat_on_west_bank = boat_on_west_bank

    def __str__(self):
        return cleandoc(f'''On the west bank there are {self.west_bank_missionaries} missionaries and {self.west_bank_cannibals} cannibals.
            On the east bank there are {self.east_bank_missionaries} missionaries and {self.east_bank_cannibals} cannibals.
            The boat is on the {'west' if self.boat_on_west_bank else 'east'} bank.
            ''')

    @property
    def is_legal(self):
        if self.west_bank_missionaries < self.west_bank_cannibals and self.west_bank_missionaries > 0:
            return False
        if self.east_bank_missionaries < self.east_bank_cannibals and self.east_bank_missionaries > 0:
            return False

        return True

    def goal_test(self):
        return self.is_legal and self.east_bank_missionaries == MAX_NUM and self.east_bank_cannibals == MAX_NUM

    def successors(self):
        successors = []

        if self.boat_on_west_bank:
            if self.west_bank_missionaries > 1:
                successors.append(MCState(self.west_bank_missionaries - 2, self.west_bank_cannibals, not self.boat_on_west_bank))
            if self.west_bank_missionaries > 0:
                successors.append(MCState(self.west_bank_missionaries - 1, self.west_bank_cannibals, not self.boat_on_west_bank))
            if self.west_bank_cannibals > 1:
                successors.append(MCState(self.west_bank_missionaries, self.west_bank_cannibals - 2, not self.boat_on_west_bank))
            if self.west_bank_cannibals > 0:
                successors.append(MCState(self.west_bank_missionaries, self.west_bank_cannibals - 1, not self.boat_on_west_bank))
            if self.west_bank_cannibals > 0 and self.west_bank_missionaries > 0:
                successors.append(MCState(self.west_bank_missionaries - 1, self.west_bank_cannibals - 1, not self.boat_on_west_bank))
        else: # Boat on east bank
            if self.east_bank_missionaries > 1:
                successors.append(MCState(self.west_bank_missionaries + 2, self.west_bank_cannibals, not self.boat_on_west_bank))
            if self.east_bank_missionaries > 0:
                successors.append(MCState(self.west_bank_missionaries + 1, self.west_bank_cannibals, not self.boat_on_west_bank))
            if self.east_bank_cannibals > 1:
                successors.append(MCState(self.west_bank_missionaries, self.west_bank_cannibals + 2, not self.boat_on_west_bank))
            if self.east_bank_cannibals > 0:
                successors.append(MCState(self.west_bank_missionaries, self.west_bank_cannibals + 1, not self.boat_on_west_bank))
            if self.east_bank_cannibals > 0 and self.east_bank_missionaries > 0:
                successors.append(MCState(self.west_bank_missionaries + 1, self.west_bank_cannibals + 1, not self.boat_on_west_bank))

        return [successor for successor in successors if successor.is_legal]

def display_solution(path):
    if len(path) == 0:
        return

    old_state = path[0]
    print(old_state)
    print()

    for i, current_state in enumerate(path[1:]):
        if current_state.boat_on_west_bank:
            print(f'{old_state.east_bank_missionaries - current_state.east_bank_missionaries} missionaries and {old_state.east_bank_cannibals - current_state.east_bank_cannibals} cannibals moved from the east bank to the west bank.')
        else:
            print(f'{old_state.west_bank_missionaries - current_state.west_bank_missionaries} missionaries and {old_state.west_bank_cannibals - current_state.west_bank_cannibals} cannibals moved from the west bank to the east bank.')

        print(current_state)

        if i != len(path[1:]) - 1: # Puts a blank line after each paragraph except for the last
            print()

        old_state = current_state

if __name__ == '__main__':
    start = MCState(MAX_NUM, MAX_NUM, True)
    solution = bfs(start, MCState.goal_test, MCState.successors)

    if solution is None:
        print("No solution found!")
    else:
        path = node_to_path(solution)
        display_solution(path)
