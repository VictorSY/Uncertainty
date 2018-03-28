from decimal import Decimal

from numpy import sqrt, std
from sympy import sympify, Eq, Symbol, solve

"""This a a variable and derived variable classes that contain one 
    of the constants and manipulated variables of the equation"""


class Variable:

    @staticmethod
    def _multiple_uncertainty():
        while True:
            try:
                number_of_values = int(input("Number of values? "))
            except ValueError:
                print("Invalid Input!")
                continue
            break
        value_sum = []
        for one_value in range(number_of_values):
            while True:
                try:
                    value = float(input("Value: "))
                except ValueError:
                    print("Invalid Input!")
                    continue
                break
            value_sum.append(value)
        return std(value_sum)/sqrt(len(value_sum))

    @staticmethod
    def _single_uncertainty(uncertainty_type):
        while True:
            try:
                value = float(input("Value: "))
            except ValueError:
                print("Invalid Input!")
                continue
            break
        if uncertainty_type is "a":
            return value / (2 * sqrt(6))
        else:
            value = Decimal(str(value))
            exponent = value.as_tuple().exponent()
            return (10**exponent) / (2 * sqrt(3))

    def _calculate_uncertainty(self):
        uncertainty_type = input("What kind of Uncertainty? (m for multiple, d for digital, a for analog): ")
        while uncertainty_type not in ["m", "d", "a"]:
            uncertainty_type = input("Unrecognized value, enter m for multiple, d for digital or a for analog: ")
        if uncertainty_type is "m":
            return self._multiple_uncertainty()
        else:
            return self._single_uncertainty(uncertainty_type)

    def __init__(self):
        self.name = Symbol(input("Name of Variable: ").strip())
        self.value = input("Value of Variable: ").strip()
        self.uncertainty = self.__calculate_uncertainty()


class DerivedVariable:

    def __init__(self):
        self.name = Symbol(input("Name of Variable: ").strip())
        self._get_equation()
        self.values = solve_for_value(self.equation, )

    def _get_equation(self):
        while True:
            try:
                input_equation = input("Input equation: ")
                equation_list = input_equation.split("=")
                self.rhs = sympify(equation_list[1].strip())
                self.lhs = sympify(equation_list[0].strip())
            except IndexError:
                print("Missing equals sign and or one side of the equation!")
                continue
            except (SyntaxError, NotImplementedError):
                print("Equation in incorrect format!")
                continue
            break

        self.equation = solve(Eq(self.lhs, self.rhs), Symbol(self.name))
        self.required_symbols = self.equation.free_symbols.discard(self.name)
        if len(self.required_symbols) < 1:
            print("Inconsistent variable name or invalid equation!")
            self._get_equation()

    def solve_for_value(self, equations, known_variables, required_symbols):
        # equations = self.equation
        for element in required_symbols:
            for variable in known_variables:
                if element is variable.name:
                    for equation in equations:
                        equation.subs(variable.name, variable.value)
                    break
                if element is not variable.name and variable is known_variables[-1]:
                    return False
        values = []
        for equation in equations:
            values.append(solve(equation))
            try:
                float(values[-1])
            except ValueError:
                print("Invalid Equation or Variables please restart the program.")
                return False
        return values
