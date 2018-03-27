from sympy import sympify, solve, Symbol, Eq

rhs = sympify(input("RHS: "))
lhs = sympify(input("LHS: "))
equation = Eq(lhs, rhs)
print(equation)
# eq_x = solve(rhs-lhs, Symbol("x"))
eq_x = solve(equation, Symbol("x"))
print(type(eq_x))
print(eq_x)
