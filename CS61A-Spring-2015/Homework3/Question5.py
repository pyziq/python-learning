'''
A classic puzzle called the Towers of Hanoi is a game that consists of three rods, 
and a number of disks of different sizes which can slide onto any rod. 
The puzzle starts with n disks in a neat stack in ascending order of size on a start rod, 
the smallest at the top, forming a conical shape.
The objective of the puzzle is to move the entire stack to an end rod, obeying the following rules:

Only one disk may be moved at a time.
Each move consists of taking the top (smallest) disk from one of the rods and sliding it onto another rod, 
on top of the other disks that may already be present on that rod.
No disk may be placed on top of a smaller disk.
Complete the definition of towers_of_hanoi which prints out the steps to solve this puzzle for 
any number of n disks starting from the start rod and moving them to the end rod:
'''

def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n == 1:
        print("Move the top disk from rod", start, "to rod", end)
    else:
        other = 6 - start - end
        towers_of_hanoi(n-1, start, other)
        towers_of_hanoi(1, start, end)
        towers_of_hanoi(n-1, other, end)
