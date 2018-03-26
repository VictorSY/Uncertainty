import Variable


class Main:
    """This program is supposed to get the uncertainty."""
    def __init__(self):
        print("Welcome to the Uncertainty finding Program")
        self.get_constants_variables()
        self.get_variables()



    @staticmethod
    def get_constants_variables(self):
        while True:
            try:
                number_of_constants = int(input("How many constants: "))
            except ValueError:
                continue
            break
        for const in range(number_of_constants):
            name = input("Variable name: ")
            while True:
                try:
                    value = float(input("Variable value: "))
                except ValueError:
                    print("Invalid Input!")
                    continue
                break
            self.constants.append(Variable.Variable(name, value))

    @staticmethod
    def get_variables(self):
        while True:
            try:
                number_of_variables = int(input("How many variables: "))
            except ValueError:
                continue
            break
        for const in range(number_of_variables):
            name = input("Variable name: ")
            while True:
                try:
                    value = float(input("Variable value: "))
                except ValueError:
                    print("Invalid Input!")
                    continue
                break
            self.constants.append(Variable.DerivedVariable(name, value))

