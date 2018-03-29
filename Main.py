from Variable import *


class Main:
    """This program is supposed to get the uncertainty."""
    def __init__(self):
        self.constants = []
        self.variables = []
        print("Welcome to the Uncertainty finding Program")
        self.get_constants_variables()
        self.get_variables()

    def get_constants_variables(self):
        while True:
            try:
                number_of_constants = int(input("How many constants: "))
            except ValueError:
                continue
            break
        for const in range(number_of_constants):
            self.constants.append(Variable())

    def get_variables(self):
        while True:
            try:
                number_of_variables = int(input("How many variables: "))
            except ValueError:
                print("Invalid Input!")
                continue
            break
        for variable in range(number_of_variables):
            self.variables.append(DerivedVariable(self.constants))
