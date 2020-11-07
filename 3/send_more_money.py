from csp import Constraint, CSP

class SendMoreMoneyConstraint(Constraint):
    def __init__(self, letters):
        super().__init__(letters)
        self.letters = letters

    def satisfied(self, assignment):
        if len(set(assignment.values())) < len(assignment):
            return False

        # If all variables have been assigned, check if it adds correctly
        if len(assignment) == len(self.letters):
            s = assignment['S']
            e = assignment['E']
            n = assignment['N']
            d = assignment['D']
            m = assignment['M']
            o = assignment['O']
            r = assignment['R']
            y = assignment['Y']
            send = s * 1000 + e * 100 + n * 10 + d
            more = m * 1000 + o * 100 + r * 10 + e
            money = m * 10000 + o * 1000 + n * 100 + e * 10 + y

            return send + more == money

        # No conflict, ensures partial solution can continue to be worked on
        return True

if __name__ == '__main__':
    letters = list('SENDMORY')
    possible_digits = {}

    for letter in letters:
        possible_digits[letter] = list(range(10))

    possible_digits['M'] = [1] # So we don't get answers starting with a 0
    csp = CSP(letters, possible_digits)
    csp.add_constraint(SendMoreMoneyConstraint(letters))
    solution = csp.backtracking_search()

    if solution is None:
        print('No solution found!')
    else:
        print(solution)
