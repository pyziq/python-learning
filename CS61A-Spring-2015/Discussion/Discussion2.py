'''
1. Print out a countdown using recursion.
'''

def countdown(n):
    """
    >>> countdown(3)
    3
    2
    1
    """
    print(n)
    if n == 1:
        return
    return countdown(n-1)

'''
2. Is there an easy way to change countdown to count up instead?
'''
def countup(n):
    if n <= 0:
        return
    countup(n-1)
    print(n)

'''
3. Write a procedure expt(base, power), which implements the exponent function.
For example, expt(3, 2) returns 9, and expt(2, 3) returns 8. Assume power is
always an integer. Use recursion, not pow!
'''
def expt(base, power):
    if power == 1:
        return base
    return base*expt(base, power-1)

'''
4. Fill in the is prime function, which returns True if n is a prime number and False otherwise.
Hint: We wrote this iteratively last week, but this time use recursion!
'''
def is_prime(n):
    def prime_test(k):
        if k >= n:
            return True
        elif n % k == 0:
            return False
        return prime_test(k+1)
    return prime_test(2)

'''
5. Write sum primes up to(n), which sums up every prime up to and including n.
Assume you have an is prime() predicate.
'''
def sum_primes_up_to(n):
    if n == 1:
        return n
    elif is_prime(n):
        return n + sum_primes_up_to(n-1)
    return sum_primes_up_to(n-1)

'''
6. Draw an environment diagram for the following code:
Bonus question: what does this function do?
calculate the pow
'''
def rec(x, y):
    if y > 0:
        return x*rec(x, y-1)
    return 1

'''
7. I want to go up a flight of stairs that has n steps. I can either take 1 or 2 steps each
time. How many different ways can I go up this flight of stairs? Write a function
count stair ways that solves this problem for me.
'''
def count_stair_ways(n):
    if n == 1 or n == 0:
        return 1
    return count_stair_ways(n-1) + count_stair_ways(n-2)

'''
8. Pascal's triangle is a useful recursive definition that tells us the coefficients in the
expansion of the polynomial(x + a)n.
Each element in the triangle has a coordinate,
given by the row it is on and its position in the row (which you could call its column).
Every number in Pascal's triangle is defined as the sum of the item above it and the
item that is directly to the upper left of it. If there is a position that does not have an
entry, we treat it as if we had a 0 there. Below are the first few rows of the triangle:
Item:  0 1 2 3 4 5
Row 0: 1
Row 1: 1 1
Row 2: 1 2 1
Row 3: 1 3 3 1
Row 4: 1 4 6 4 1
Row 5: 1 5 10 10 5 1
...
Define the procedure pascal(row, column) which takes a row and a column, and
finds the value at that position in the triangle. Don't use the closed-form solution, if
you know it.
'''
def pascal(row, column):
    if column == 0:
        return 1
    elif row == column:
        return 1
    return pascal(row-1, column-1) + pascal(row-1, column)
'''
9. The TAs want to print handouts for their students. However, for some unfathomable
reason, both the printers are broken; the first printer only prints multiples of n1, and
the second printer only prints multiples of n2. Help the TAs figure out whether or
not it is possible to print an exact number of handouts!
First try to solve without a helper function. Also try to solve using a helper function
and adding up to the sum.
'''
def has_sum(sum, n1, n2):
    """
    >>> has_sum(1, 3, 5)
    False
    >>> has_sum(5, 3, 5) # 1(5) + 0(3) = 5
    True
    >>> has_sum(11, 3, 5) # 2(3) + 1(5) = 11
    True
    """
    if sum < 0:
        return False
    elif sum % n2 == 0:
        return True
    return has_sum(sum-n1, n1, n2)

'''
10. The next day, the printers break down even more! Each time they are used, Printer
A prints a random x copies 50 <= x <= 60, and Printer B prints a random y copies
130 <= y <= 140. The TAs also relax their expectations: they are satisfied as long as they
get at least lower, but no more than upper, copies printed. (More than upper copies
is unacceptable because it wastes too much paper.)
Hint: Try using a helper function.
'''
def sum_range(lower, upper):
    """
>>> sum_range(45, 60) # Printer A prints within this range;
    ... # the TAs would be satisfied with any number it prints
    ...True
>>> sum_range(40, 55) # Printer A can print some number
    56-60
    ... # copies, which is not within the TA acceptable range
    ...False
>>> sum_range(170, 201) # Printer A + Printer B will print
    ... # somewhere between 180 and 200 copies total
    ...True
"""
    def printed(printed_lower, printed_upper):
        if upper < printed_upper:
            return False
        elif lower <= printed_lower:
            return True
        else:
            return printed(printed_lower+50, printed_upper+60) \
                   or printed(printed_lower+130, printed_upper+140)
    return printed(0, 0)
    