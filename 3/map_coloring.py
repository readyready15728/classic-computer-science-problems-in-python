from csp import Constraint, CSP

class MapColoringConstraint(Constraint):
    def __init__(self, place_0, place_1):
        super().__init__([place_0, place_1])
        self.place_0 = place_0
        self.place_1 = place_1

    def satisfied(self, assignment):
        # If either place is not in the assignment, then it is not yet
        if self.place_0 not in assignment or self.place_1 not in assignment:
            return True

        # Check the color assigned to place_0 is not the same as the color assigned to place_1
        return assignment[self.place_0] != assignment[self.place_1]

if __name__ == '__main__':
    variables = [
        'Western Australia',
        'Northern Territory',
        'South Australia',
        'Queensland',
        'New South Wales',
        'Victoria',
        'Tasmania'
    ]
    domains = {}

    for variable in variables:
        domains[variable] = ['red', 'green', 'blue']

    csp = CSP(variables, domains)
    csp.add_constraint(MapColoringConstraint('Western Australia', 'Northern Territory'))
    csp.add_constraint(MapColoringConstraint('Western Australia', 'South Australia'))
    csp.add_constraint(MapColoringConstraint('South Australia', 'Northern Territory'))
    csp.add_constraint(MapColoringConstraint('Queensland', 'Northern Territory'))
    csp.add_constraint(MapColoringConstraint('Queensland', 'South Australia'))
    csp.add_constraint(MapColoringConstraint('Queensland', 'New South Wales'))
    csp.add_constraint(MapColoringConstraint('New South Wales', 'South Australia'))
    csp.add_constraint(MapColoringConstraint('Victoria', 'South Australia'))
    csp.add_constraint(MapColoringConstraint('Victoria', 'New South Wales'))
    csp.add_constraint(MapColoringConstraint('Victoria', 'Tasmania'))

    solution = csp.backtracking_search()

    if solution is None:
        print("No solution found!")
    else:
        print(solution)
