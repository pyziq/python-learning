'''
Question 3

The ping-pong sequence counts up starting from 1 and is always either counting up or counting down. 
At element k, the direction switches if k is a multiple of 7 or contains the digit 7. 
The first 30 elements of the ping-pong sequence are listed below, with direction swaps marked using 
brackets at the 7th, 14th, 17th, 21st, 27th, and 28th elements:
1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6
Implement a function pingpong that returns the nth element of the ping-pong sequence. 
Do not use any assignment statements; however, you may use def statements.
Hint: If you're stuck, try implementing pingpong first using assignment and a while statement, 
then try a recursive implementation without assignment:
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

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
    def next(k,p,is_up):
        if k == n:
            return p
        if is_up:
            return switch(k+1,p+1,is_up)
        else:
            return switch(k+1,p-1,is_up)
    def switch(k,p,is_up):
        if k % 7 == 0 or has_seven(k):
            return next(k,p,not is_up)
        else:
            return next(k,p,is_up)
    return next(1,1,True)
