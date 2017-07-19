'''
Question 2

Write a function has_seven that takes a positive integer n and returns whether n contains the digit 7. Do not use any assignment statements - use recursion instead:
'''

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k % 10 == 7:
        return True
    elif k // 10 > 0:
        return has_seven(k // 10)
    else:
        return False

