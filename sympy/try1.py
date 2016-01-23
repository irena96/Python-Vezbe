import sympy

x = sympy.symbols("x")

str_expr = "x**2 + 3*x - 1/2"
expr = sympy.sympify(str_expr)
expr
print expr.subs(x, 2)

