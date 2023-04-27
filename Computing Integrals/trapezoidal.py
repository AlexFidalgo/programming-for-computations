from math import exp

def trapezoidal(f, a, b, n):
    h = float(b-a)/n
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1, n):
        result += f(a + i*h)
    result *= h
    return result

if __name__ == '__main__':

    v = lambda t: 3*(t**2)*exp(t**3)
    n = 4

    numerical = trapezoidal(v, 0, 1, n)

    V = lambda t: exp(t**3)
    exact = V(1) - V(0)

    error = exact - numerical

    print('n=%d: %.16f, error: %g' % (n, numerical, error))
