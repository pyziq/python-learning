'''
Question 1

Implement piecewise, which takes two one-argument functions, f and g, along with a number b. 
It returns a new function that takes a number x and returns either f(x) if x is less than b, 
or g(x) if x is greater than or equal to b.

'''
def piecewise(f, g, b):
    """Returns the piecewise function h where:

    h(x) = f(x) if x < b,
           g(x) otherwise

    >>> def negate(x):
    ...     return -x
    >>> abs_value = piecewise(negate, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    "*** YOUR CODE HERE ***"
    def h(x):
        if x < b:
            return f(x)
        else:
            return g(x)
    return h
