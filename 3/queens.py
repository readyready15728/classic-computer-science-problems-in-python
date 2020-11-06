from csp import Constraint, CSP

class QueensConstraint(Constraint):
    def __init__(self, columns):
        super().__init__(columns)
        self.columns = columns

    def satisfied(self, assignment):
        # q_0_c = queen 0 column, q_0_r = queen 0 row
        for q_0_c, q_0_r in assignment.items():
            # q_1_c = queen 1 column
            for q_1_c in range(q_0_c + 1, len(self.columns) + 1):
                if q_1_c in assignment:
                    q_1_r = assignment[q_1_c] # q_1_r =  queen 1 row

                    if q_0_r == q_1_r: # Same row?
                        return False

                    if abs(q_0_r - q_1_r) == abs(q_0_c - q_1_c): # Same diagonal?
                        return False

        return True

if __name__ == '__main__':
    columns = list(range(1, 9))
    rows = {}

    for column in columns:
        rows[column] = list(range(1, 9))

    csp = CSP(columns, rows)
    csp.add_constraint(QueensConstraint(columns))
    solution = csp.backtracking_search()

    if solution is None:
        print('No solution found!')
    else:
        print(solution)
