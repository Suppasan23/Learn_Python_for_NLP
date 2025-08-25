import sympy as sp

# กำหนดตัวแปร
t, x, h = sp.symbols('t x h')

# นิยามฟังก์ชัน g(t)
g = t / (2*t + 6)

# (a) g(0)
a = g.subs(t, 0)

# (b) g(-3)
b = g.subs(t, -3)

# (c) g(10)
c = g.subs(t, 10)

# (d) g(x^2)
d = g.subs(t, x**2)

# (e) g(t + h)
e = g.subs(t, t + h)

# (f) g(t^2 - 3t + 1)
f = g.subs(t, t**2 - 3*t + 1)

print("(a) g(0) =", a)
print("(b) g(-3) =", b)
print("(c) g(10) =", c)
print("(d) g(x^2) =", d)
print("(e) g(t+h) =", e)
print("(f) g(t^2 - 3t + 1) =", f)
