"""from sympy import sympify, solve, Symbol, Eq


def equation_input():
    while True:
        try:
            input_equation = input("input equation: ")
            equation_list = input_equation.split("=")
            global rhs, lhs
            rhs = sympify(equation_list[1].strip())
            lhs = sympify(equation_list[0].strip())
        except IndexError:
            print("Missing equals sign and or one side of the equation!")
            continue
        except (SyntaxError, NotImplementedError):
            print("Equation in incorrect format!")
            continue
        break


equation_input()
equation = Eq(lhs, rhs)
print(equation)
print("Variables: %s" % equation.free_symbols)
print(type(next(iter(equation.free_symbols))))
eq_x = solve(equation, Symbol("x"))
print(type(eq_x))
print(eq_x)"""

from Main import Main

main = Main()
