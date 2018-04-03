from Variable import *


class Main:
    """This program is supposed to get the uncertainty."""
    def __init__(self):
        self.known_variables = []
        self.unknown_variables = []
        print("Welcome to the Uncertainty finding Program")
        self.get_constants_variables()
        self.get_variables()
        for answering_round in range(25):
            self.solve_unknowns()

    def get_constants_variables(self):
        while True:
            try:
                number_of_constants = int(input("How many constants: "))
            except ValueError:
                continue
            break
        for const in range(number_of_constants):
            self.known_variables.append(Variable())

    def get_variables(self):
        while True:
            try:
                number_of_variables = int(input("How many variables: "))
            except ValueError:
                print("Invalid Input!")
                continue
            break
        for variable in range(number_of_variables):
            self.unknown_variables.append(DerivedVariable(self.known_variables))

    def solve_unknowns(self):
        for variable in self.unknown_variables:
            variable.value, variable.derivative_values = variable.solve_for_value(variable.equation,
                                                                                  self.known_variables,
                                                                                  variable.required_symbols)
            if variable.value is not None and variable.uncertainty is not None:
                self.known_variables.append(variable)
                self.unknown_variables.remove(variable)


Main()
