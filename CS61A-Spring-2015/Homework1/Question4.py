# -*- coding: utf-8 -*-
'''
Question 4

Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.

1.Pick a positive integer n as the start.
2.If n is even, divide it by 2.
3.If n is odd, multiply it by 3 and add 1.
4.Continue this process until n is 1.
The number n will travel up and down but eventually end at 1 (at least for all numbers that have ever been tried — nobody has ever proved that the sequence will terminate). 
Analogously, a hailstone travels up and down in the atmosphere before eventually landing on earth.

The sequence of values of n is often called a Hailstone sequence, because hailstones also travel up and down in the atmosphere before falling to earth. 
Write a function that takes a single argument with formal parameter name n, prints out the hailstone sequence starting at n, and returns the number of steps in the sequence:

'''
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    count = 1
    while(n != 1):
        if(n % 2 == 0):
           n = n / 2
        else:
            n = n*3 + 1
        print(n)
        count = count + 1
    return count

            