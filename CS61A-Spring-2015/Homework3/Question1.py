'''
Question 1

A mathematical function G on positive integers is defined by two cases:
G(n) = n,                                       if n <= 3
G(n) = G(n - 1) + 2 * G(n - 2) + 3 * G(n - 3),  if n > 3
Write a recursive function g that computes G(n). Then, write an iterative function g_iter that also computes G(n):
'''
def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    return g(n-1) + 2 * g(n-2) + 3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    a, b, c = 1, 2, 3
    while n > 3:
        a, b, c = b, c, c+2*b+3*a
        n = n - 1
    return c

