'''

Question 3

Implement the function nearest_two, which takes as input a positive number x 
and returns the power of two (..., 1/8, 1/4, 1/2, 1, 2, 4, 8, ...) 
that is nearest to x. 
If x is exactly between two powers of two, return the larger.

You may change the starter implementation if you wish.
'''
def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0


    """
    power_of_two = 1.0
    "*** YOUR CODE HERE ***"
    i = 0
    if x >= 1:
        while True:
            power_of_two = pow(2,i)
            d = abs(x-power_of_two)
            d1 = abs(x-pow(2,i+1))
            if d1 < d:
                i = i+1
                continue
            elif d1 == d:
                power_of_two = pow(2,i+1)
                break
            else:
                break
    if x < 1:
        while True:
            power_of_two = pow(2,i)
            d = abs(x-power_of_two)
            d1 = abs(x-pow(2,i-1))
            if d1 < d:
                i = i-1
                continue
            else:
                break
    return power_of_two

print(nearest_two(0.01))