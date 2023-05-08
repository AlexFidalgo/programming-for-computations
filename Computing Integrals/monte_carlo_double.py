import numpy as np

def MonteCarlo_double(f, g, x0, x1, y0, y1, n):
    """
    Monte Carlo integration of f over a domains g>=0 embedded in a rectangle [x0,x1]X[y0,y1].
    n² is the number of random points
    """
    
    # Draw n² random points in the rectangle
    x = np.random.uniform(x0, x1, n)
    y = np.random.uniform(y0, y1, n)
    
    # Compute sum of f values inside the integration domain
    f_mean = 0
    num_inside = 0 # number of x,y points inside domain
    for i in range(len(x)):
        for j in range(len(y)):
            if g(x[i], y[j]) >=0:
                num_inside += 1
                f_mean += f(x[i], y[j])
    f_mean = f_mean/float(num_inside)
    area = num_inside/float(n**2)*(x1-x0)*(y1-y0)
    return area*f_mean


if __name__ == '__main__':
    
    def g(x, y):
        return (1 if (0 <= x <= 2 and 3 <= y <= 4.5) else -1)
    
    res = MonteCarlo_double (lambda x, y: 1, g, 0, 3, 2, 5, 1000)
    
    def g(x,y):
        xc, yc = 0,0
        R = 2
        return R**2 - ((x-xc)**2 + (y-yc)**2)
    
    res = MonteCarlo_double (lambda x, y: np.sqrt(x**2 + y**2), g, -2, 2, -2, 2, 1000)