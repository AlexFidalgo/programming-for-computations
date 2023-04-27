from math import exp

def midpoint(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result

if __name__ == '__main__':

    v = lambda t: 3*(t**2)*exp(t**3)
    n = 4

    numerical = midpoint(v, 0, 1, n)

    V = lambda t: exp(t**3)
    exact = V(1) - V(0)

    error = exact - numerical

    print('n=%d: %.16f, error: %g' % (n, numerical, error))
