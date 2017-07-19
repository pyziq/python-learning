'''
Question 4

Once the machines take over, the denomination of every coin will be a power of two: 
1-cent, 2-cent, 4-cent, 8-cent, 16-cent, etc. There will be no limit to how much a coin can be worth.

A set of coins makes change for n if the sum of the values of the coins is n.
For example, the following sets make change for 7:

7 1-cent coins
5 1-cent, 1 2-cent coins
3 1-cent, 2 2-cent coins
3 1-cent, 1 4-cent coins
1 1-cent, 3 2-cent coins
1 1-cent, 1 2-cent, 1 4-cent coins
Thus, there are 6 ways to make change for 7. 
Write a function count_change that takes a positive integer n and returns the number of ways to make change 
for n using these coins of the future:

'''
def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def f(amount,min_coin = 1):
        if amount < min_coin:
            return 0
        if amount == min_coin:
            return 1
        with_min_coin = f(amount-min_coin,min_coin)
        without_min_coin = f(amount,2*min_coin)
        return with_min_coin + without_min_coin
    
    return f(amount)