from sympy import *

x, y, z = symbols("x y z")

#ข้อ 4.1
print("━━━━━━━━━━ข้อ 4.1━━━━━━━━━")
expr11 = Eq(x + y , 2)
expr12 = Eq(2*x + y , 0)
expr1112_solve = solve((expr11, expr12),(x, y))

""" pretty_print(expr1112_solve) """
pretty_print(dotprint(x+2))





