from numpy import exp
from numpy import linspace, sum

def midpoint(f, a, b, n):
    """
    Returns the one-dimensional integral of f from a to b considering n intervals using the midpoint method

    f : function
    a : lower bound
    b : upper bound
    n : number of intervals
    """
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

def midpoint_double(f, a, b, c, d, nx, ny):
    """
    Returns the two-dimensional integral of f from a to b considering n intervals using the midpoint method

    f : function
    a : x lower bound
    b : x upper bound
    c: y lower bound
    d: y upper bound
    nx : number of intervals on x-axis
    ny: number of intervals on y-axis
    """
    def g(x):
        return midpoint(lambda y: f(x, y), c, d, ny)
    return midpoint(g, a, b, nx)

if __name__ == '__main__':

    # Note the necessity to use exp from numpy: our v function will be called with x as an array, and the exp function must be capable of 
    # working with an array.
    v = lambda t: 3*t**2*exp(t**3) 
    n = 4

    numerical = midpoint(v, 0, 1, n)
    
    numerical_vectorized = midpoint_vectorized(v, 0, 1, n)

    V = lambda t: exp(t**3)
    exact = V(1) - V(0)

    error = exact - numerical

    print('n=%d: numerical=%.16f, numerical_vectorized=%.16f, error: %g' % (n, numerical, numerical_vectorized, error))
    
"""
v = lambda t: 3*t**2*exp(t**3)

%timeit midpoint_vectorized(v, 0, 1, 1000000)
29.5 ms ± 3.3 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

%timeit midpoint(v, 0, 1, 1000000)
688 ms ± 18 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
"""
