from numpy import exp
from numpy import linspace

def trapezoidal(f, a, b, n):
    h = float(b-a)/n
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1, n):
        result += f(a + i*h)
    result *= h
    return result

def trapezoidal_vectorized(f, a, b, n):
    h = float(b-a)/n
    x = linspace(a, b, n+1)
    s = sum(f(x)) - 0.5*f(a) - 0.5*f(b)
    return h*s

if __name__ == '__main__':

    v = lambda t: 3*(t**2)*exp(t**3)
    n = 4

    numerical = trapezoidal(v, 0, 1, n)
    
    numerical_vectorized = trapezoidal_vectorized(v, 0, 1, n)

    V = lambda t: exp(t**3)
    exact = V(1) - V(0)

    error = exact - numerical

    print('n=%d: numerical=%.16f, numerical_vectorized=%.16f, error: %g' % (n, numerical, numerical_vectorized, error))
