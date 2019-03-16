from expr.lipexpr import *

e1 = Const(1)
e2 = Const(2)
e3 = Ident(0, 1)
e4 = e3 + (e1 + e2)
print(e4)
print("Hello test")