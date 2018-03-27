from decimal import Decimal as decimal

from numpy import sqrt, std
from sympy import sympify


class Variable:
    """This a a variable class that contains one of the manipulated variables in the equation"""

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
    def _single_uncertainty(self, uncertainty_type):
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
            value = decimal(str(value))
            exponent = value.as_tuple().exponent()
            return (10**exponent) / (2 * sqrt(3))

    @staticmethod
    def _calculate_uncertainty(self):
        uncertainty_type = input("What kind of Uncertainty? (m for multiple, d for digital, a for analog): ")
        while uncertainty_type not in ["m", "d", "a"]:
            uncertainty_type = input("Unrecognized value, enter m for multiple, d for digital or a for analog: ")
        if uncertainty_type is "m":
            return self.__multiple_uncertainty()
        else:
            return self.__single_uncertainty(uncertainty_type)

    def __init__(self, variable_name, variable_value):
        self.variable_name = variable_name
        self.variable_value = variable_value
        self.uncertainty = self.__calculate_uncertainty()


class DerivedVariable(Variable):

    def __init__(self, name, value):
        super().__init__(name, value)
        self.equation = self.__get_equation()

    @staticmethod
    def _get_equation(self):
        while True:
            try:
                equation = sympify(input("Enter the equation equal to your variable (ex. sqrt(arctan(x**5)):\n"))
            except:
                print("Invalid equation.")
                continue
            break
        return equation

    def solve_for_variable(self, origianl_equation):
        print("Solving for %s" % self.name)
        # new_equation = solvers.
