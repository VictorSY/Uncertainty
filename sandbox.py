from sympy import sympify, solve, Symbol, Eq


def equation_input():
    input_equation = input("input equation:")
    equation_list = input_equation.split("=")
    global rhs, lhs
    rhs = sympify(equation_list[1].strip())
    lhs = sympify(equation_list[0].strip())


equation_input()
equation = Eq(lhs, rhs)
print(equation)
print((equation.free_symbols()))
# eq_x = solve(rhs-lhs, Symbol("x"))
eq_x = solve(equation, Symbol("mx"))
print(type(eq_x))
print(eq_x)
