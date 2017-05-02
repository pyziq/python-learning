'''
Question 2

Complete the implementation of pi_fraction, which takes a positive number gap and prints the fraction that is no more than gap away from pi and has the smallest possible positive integer denominator. 
See the doctests for the format of the printed output.

Hint: If you want to find the nearest integer to a number, use the built-in round function. 
It's possible to solve this problem without using round.

You may change the starter implementation if you wish.
'''

from math import pi

def pi_fraction(gap):
    """Print the fraction within gap of pi that has the smallest denominator.

    >>> pi_fraction(0.01)
    22 / 7 = 3.142857142857143
    >>> pi_fraction(1)
    3 / 1 = 3.0
    >>> pi_fraction(1/8)
    13 / 4 = 3.25
    >>> pi_fraction(1e-6)
    355 / 113 = 3.1415929203539825


    """
    numerator, denominator = 3, 1
    "*** YOUR CODE HERE ***"
    while True:
        g1,g2 = abs(numerator/denominator - pi), abs((numerator+1)/denominator-pi)
        if abs(g1) < gap:
            break
        if g2 < g1:
            g1,g2 = g2,(numerator+1)/denominator
            numerator += 1
            continue
        else:
            denominator += 1
            numerator =3
            continue
    print(numerator, '/', denominator, '=', numerator/denominator)
    return
pi_fraction(1e-6)