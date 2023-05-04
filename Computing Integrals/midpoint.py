from numpy import exp
from numpy import linspace, sum

def midpoint_without_vectorization(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result

def midpoint_vectorized(f, a, b, n):
    h = float(b-a)/n
    x = linspace(a + h/2, b - h/2, n)
    return h*sum(f(x))

if __name__ == '__main__':

    #Note the necessity to use exp from numpy: our v function will be called with x as an array, and the exp function must be capable of 
    # working with an array.
    v = lambda t: 3*t**2*exp(t**3) 
    n = 4

    numerical = midpoint_without_vectorization(v, 0, 1, n)
    
    numerical_vectorized = midpoint_vectorized(v, 0, 1, n)

    V = lambda t: exp(t**3)
    exact = V(1) - V(0)

    error = exact - numerical

    print('n=%d: numerical=%.16f, numerical_vectorized=%.16f, error: %g' % (n, numerical, numerical_vectorized, error))
