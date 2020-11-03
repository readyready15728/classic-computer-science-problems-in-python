from abc import ABC, abstractmethod

class Constraint(ABC):
    def __init__(self, variables):
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment):
        ...

class CSP:
    def __init__(self, variables, domains):
        self.variables = variables
        self.domains = domains
        self.constraints = {}

        for variable in self.variables:
            self.constraints[variable] = []

            if variable not in self.domains:
                raise LookupError('Every variable must have a domain assigned to it')

    def add_constraint(self, constraint):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError('Variable in constraint not in CSP')
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable, assignment):
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False

        return True

    def backtracking_search(self, assignment={}):
        # Assignment is complete if every variable is assigned
        if len(assignment) == len(self.variables):
            return assignment

        # Get all variables in the CSP but not in the assignment
        unassigned = [v for v in self.variables if v not in assignment]

        # Get the every possible domain value of the first unassigned variable
        first = unassigned[0]

        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value

            # If the solution is still consistent, recurse
            if self.consistent(first, local_assignment):
                result = self.backtracking_search(local_assignment)

                if result is not None:
                    return result

        return None
