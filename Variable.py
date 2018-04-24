from copy import deepcopy
from decimal import Decimal

from numpy import sqrt, std
from sympy import sympify, Eq, Symbol, solve, diff, Mul

"""This a a variable and derived variable classes that contain one 
    of the constants and manipulated variables of the equation"""


class Variable:

    def __init__(self):
        self.name = Symbol(input("Name of Variable: ").strip())
        self.value = None
        self.uncertainty = self._calculate_uncertainty()

    def _multiple_uncertainty(self):
        while True:
            try:
                number_of_values = int(input("Number of values? "))
            except ValueError as e:
                print(e)
                print("Invalid Input!")
                continue
            break
        value_sum = []
        for one_value in range(number_of_values):
            while True:
                try:
                    value = float(input("Value: "))
                except ValueError as e:
                    print(e)
                    print("Invalid Input!")
                    continue
                break
            value_sum.append(value)
            self.value = sum(value_sum) / len(value_sum)
        return std(value_sum) / sqrt(len(value_sum))

    def _single_uncertainty(self, uncertainty_type):
        while True:
            try:
                self.value = float(input("Value of Variable: ").strip())
            except ValueError as e:
                print(e)
                continue
            break
        if uncertainty_type is "a":
            while True:
                try:
                    value = float(input("a value: "))
                except ValueError as e:
                    print(e)
                    print("Invalid Input!")
                    continue
                break
            return value / (2 * sqrt(6))
        elif uncertainty_type is "u":
            try:
                self.uncertainty = float(input("Uncertainty: ").strip())
            except ValueError as e:
                print(e)
        else:
            exponent = Decimal(str(self.value)).as_tuple()[2]
            return (10 ** exponent) / (2 * sqrt(3))

    def _calculate_uncertainty(self):
        uncertainty_type = input("What kind of Uncertainty? (m for multiple, d for digital, a for analog,\n"
                                 "u for uncertainty you already know): ")
        while uncertainty_type not in ["m", "d", "a", "u"]:
            uncertainty_type = input("Unrecognized value, (m for multiple, d for digital, a for analog,\n"
                                     "u for uncertainty you already know): ")
        if uncertainty_type is "m":
            return self._multiple_uncertainty()
        else:
            return self._single_uncertainty(uncertainty_type)


class DerivedVariable:

    def __init__(self, known_variables):
        self.required_symbols = None
        self.equation = None
        self.name = Symbol(input("Name of Variable: ").strip())
        self._get_equation()
        try:
            self.value, self.uncertainty = self.solve_for_value(self.equation, known_variables,
                                                                self.required_symbols)
        except TypeError as e:
            print(e)
            pass

    def _get_equation(self):
        while True:
            try:
                input_equation = input("Input equation: ")
                equation_list = input_equation.split("=")
                self.rhs = sympify(equation_list[1].strip())
                self.lhs = sympify(equation_list[0].strip())
            except IndexError as e:
                print(e)
                print("Missing equals sign and or one side of the equation!")
                continue
            except (SyntaxError, NotImplementedError)as e:
                print(e)
                print("Equation in incorrect format!")
                continue
            break
        original_equation = Eq(self.lhs, self.rhs)
        self.equation = solve(original_equation, self.name)
        self.required_symbols = self.rhs.free_symbols.union(self.lhs.free_symbols)
        self.required_symbols.remove(self.name)
        if len(self.required_symbols) < 1 or len(self.equation) < 1:
            print("Inconsistent variable name or invalid equation!")
            self._get_equation()

    def solve_for_value(self, equations: list, known_variables: list, required_symbols: set, need_diff=True):
        if need_diff:
            diff_equations_og = deepcopy(equations)
        for element in required_symbols:
            for variable in known_variables:
                if element is variable.name:
                    for equation in equations:
                        equations.remove(equation)
                        equation = equation.subs(variable.name, variable.value)
                        equations.insert(0, equation)
                    break
                if element is not variable.name and variable is known_variables[-1]:
                    return None, None
        values = []
        for equation in equations:
            values.append(equation)
        if need_diff:
            diff_answers = []
            for equation in diff_equations_og:
                for variable in known_variables:
                    diff_equation = diff(equation, variable.name)

                    diff_answers.append(Mul(variable.uncertainty,
                                            self.solve_for_value([diff_equation],
                                                                 known_variables,
                                                                 required_symbols,
                                                                 False)[0]))
            sum_inside_sqrt = 0
            for answer in diff_answers:
                sum_inside_sqrt += answer ** 2
            return values[0], sum_inside_sqrt ** 0.5
        return values
