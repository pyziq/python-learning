#coding = utf-8
'''
1. Fill in the is prime function, which returns True if n is a prime number and False
otherwise.
Hint: use the % operator: x % y returns the remainder of x when divided by y.
'''
def is_prime(n):
    i = 2
    while i < n:
        if n % 2 == 0:
            return False
        i = i+1
    return True

'''
2. Fill in the choose function, which returns the number of ways to choose k items from
n items. Mathematically, choose(n, k) is defined as:
n x (n-1) x (n-2) x ... x (n-k+1) /
k x (k-1) x (k-2) x ... x 2 x 1
'''
def choose(n, k):
    """
    Returns the number of ways to choose K items from
        N items.
        >>> choose(5, 2)
        10
        >>> choose(20, 6)
        38760
    """
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = numerator * (n-i)
        denominator = denominator * (k-i)
    devsion = numerator / denominator
    return devsion

'''
3.Suppose we want to square or double every integer from 1 to n and print the result as
we go. Fill in the functions square ints and double ints by using the square and
double functions we have defined.
'''
def square(x):
    return x * x
def square_ints(n):
    """
    Print out the square of every integer from 1 to n.
    >>> square_ints(3)
    1
    4
    9
    """
    for i in range(1, n+1):
        print (square(i))

def double(x):
    return 2 * x

def double_ints(n):
    """
    Print out the double of every integer from 1 to n.
    >>> double_ints(3)
    2
    4
    6
    """
    for i in range (1,n+1):
        print (double(i))

'''
4. Implement the function transform ints that takes in a function func and a number
n and prints the result of applying that function to each of the first n natural
numbers.
'''
def transform_ints(func, n):
    """
    Print out all integers from 1 to n with func applied
    on them.
    >>> def square(x):
    ...     return x * x
    >>> transform_ints(square, 3)
    1
    4
    9
    """
    for i in range(1, n+1):
        print(func(i))

'''
5.Write a function and add that takes a function f (such that f is a function of one
argument) and a number n as arguments. It should return a function that takes one
argument, and does the same thing as the function f, except also adds n to the result.
'''
def and_add(f, n):
    """
    Return a new function. This new function takes an
    argument x and returns f(x) + n.
    >>> def square(x):
    ...     return x * x
    >>> new_square = and_add(square, 3)
    >>> new_square(4) # 4 * 4 + 3
    19
    """
    def func(x):
        return f(x) + n
    return func
'''
6.Draw the environment diagram that results from running the following code:
'''
n = 7
def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return h

def f(f, x):
    return f(x + n)()

m = f(g, n)

'''
7. Implement a function keep ints, which takes in a function cond and a number n,
and only prints a number from 1 to n if calling cond on that number returns True:
'''
def is_even(x):
    return x % 2 == 0

def keep_ints(cond, n):
    """
    Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    for i in range(1, n+1):
        if cond(i):
            print(i)

'''
8. The following code has been loaded into the Python interpreter:
'''
def skipped(f):
    def g():
        return f
    return g

def composed(f, g):
    def h(x):
        return f(g(x))
    return h

def added(f, g):
    def h(x):
        return f(x) + g(x)
    return h

def square(x):
    return x*x

def two(x):
    return 2
'''
What will Python output when the following lines are evaluated?
>>> composed(square, two)(7)
4
>>> skipped(added(square, two))()(3)
11
>>> composed(two, square)(2)
2
'''

'''
9. Draw the environment diagram for the following code:
'''
from operator import add
def curry2(h):
    def f(x):
        def g(y):
            return h(x, y)
        return g
    return f

make_adder = curry2(add)
add_three = make_adder(3)
five = add_three(2)

'''
10.Draw the environment diagram that results from running the following code.
'''
a = 1
def b(b):
    return a + b
a = b(a)
a = b(a)

'''
11. Draw the environment diagram that results from executing the code below.
'''
def this(x):
    return 2*that(x)
def that(x):
    x = y + 1
    this = that
    return x
x, y = 1, 2
this(that(y))

'''
12.Draw the environment diagram that results from executing the code below
'''
from operator import add, mul
six = 2
def ty(one, a):
    spring = one(a, six)
    return spring
def fif(teen):
    return teen ** 2
six = ty(add, mul(six, six))
spring = fif(six)
