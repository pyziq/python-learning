'''
Question 2

If f is a numerical function and n is a positive integer, 
then we can form the nth repeated application of f, 
which is defined to be the function whose value at x is f(f(...(f(x))...)). 
For example, if f adds 1 to its argument, then the nth repeated application of f adds n. 
Write a function that takes as inputs a function f and a positive integer n 
and returns the function that computes the nth repeated application of f:

'''

def repeated(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    """
    "*** YOUR CODE HERE ***"
    def h(x):
        k = 1
        while k<= n: 
            x = f(x)
            k = k+1
        return x
    return h

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def square(x):
    return x * x

print(repeated(square,2)(3))