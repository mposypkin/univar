from expr.lipexpr import *

def f(x):
    return Sin(Ident(x))

print(Sin(Ident([0,1])))


xrange = [0, 6]
P = []
P.append(xrange)
fr = 100000000
eps = 0.01
maxlen = 8
while len(P) > 0 and len(P) <= 80:
    x = P.pop(0)
    e = f(x)
    fr = min(e.value, fr)
    print(e)
    if fr - e.range[0] > eps:
        m = 0.5 * (x[0] + x[1])
        x1 = [x[0], m]
        x2 = [m, x[1]]
        P.append(x1)
        P.append(x2)

print(fr)
