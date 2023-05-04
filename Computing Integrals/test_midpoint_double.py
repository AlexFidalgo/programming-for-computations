from midpoint import midpoint_double

def test_midpoint_double():
    """Test that a linear function is integrated exactly"""
    
    def f(x, y):
        return 2*x + y
    
    a = 0; b = 2; c = 2; d = 3
    
    import sympy
    x, y = sympy.symbols('x y')
    I_expected = sympy.integrate(f(x, y), (x, a, b), (y, c, d))
    # Test three cases: nx < ny, nx = ny, nx > ny
    for nx, ny in (3, 5), (4, 4), (5, 3):
        I_computed = midpoint_double(f, a, b, c, d, nx, ny)
        tol = 1E-14
        #print I_expected, I_computed1, I_computed2
        assert abs(I_computed - I_expected) < tol
        
if __name__ == '__main__':
    test_midpoint_double()