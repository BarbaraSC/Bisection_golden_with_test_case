from sympy import *

def bisection(expr, l, u, max_iterations, epsilon):
    x = symbols('x')
    z = expr.subs(x, l).evalf() * expr.subs(x, u).evalf()
    if z > 0:
        return [], []
    if expr.subs(x, l).evalf() < 0:
        l_sign = 0
    else:
        l_sign = 1

    approximations_roots = []
    precision = []

    for i in range(max_iterations):
        mid = (l + u) / 2  # Correct midpoint formula
        approximations_roots.append(mid)

        if i > 0:
            precision.append(abs((approximations_roots[-1] - approximations_roots[-2]) / approximations_roots[-1]))
            if precision[-1] < epsilon:
                break
        else:
            precision.append(0)

        if expr.subs(x, mid).evalf() < 0:
            if l_sign == 0:
                l = mid
            else:
                u = mid
        else:
            if l_sign == 1:
                l = mid
            else:
                u = mid

    return approximations_roots, precision


# Test case
def test_bisection():
    x = symbols('x')
    expr = x**2 - 4
    l = 1
    u = 3
    max_iterations = 100
    epislon = 1e-6
    
    roots, precision = bisection(expr, l, u, max_iterations, epislon)
    print(roots[-1], precision[-1])
    

if __name__ == "__main__":
    test_bisection()