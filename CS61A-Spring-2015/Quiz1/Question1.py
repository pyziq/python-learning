'''
Question 1

Implement harmonic, which returns the harmonic mean of two positive numbers x and y. 
The harmonic mean of 2 numbers is 2 divided by the sum of the reciprocals of the numbers. 
(The reciprocal of x is 1/x.)

'''
def harmonic(x, y):
    """Return the harmonic mean of x and y.

    >>> harmonic(2, 6)
    3.0
    >>> harmonic(1, 1)
    1.0
    >>> harmonic(2.5, 7.5)
    3.75


    """
    "*** YOUR CODE HERE ***"
    return 2/(1/x+1/y)
