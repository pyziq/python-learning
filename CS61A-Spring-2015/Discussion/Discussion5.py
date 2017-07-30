"""
1.1 What Would Python Output?
Consider the following definitions and assignments and determine what Python would
output for each of the calls below if they were evaluated in order. Draw the box and pointers
diagrams to the right in order to keep track of the state.

1.  >>> lst1 = [1, 2, 3]
    >>> lst2 = lst1
    >>> lst2 is lst1
    True
2.  >>> lst1.append(4)
    >>> lst1
    [1,2,3,4]
3.  >>> lst2
    [1,2,3,4]
4.  >>> lst2[1] = 42
    >>> lst2
    [1,42,3,4]
5.  >>> lst1
    [1,42,3,4]
6.  >>> lst1 = lst1 + [5]
    >>> lst1
    [1,42,3,4,5]
7.  >>> lst2
    [1,42,3,4]
8.  >>> lst2 is lst1
    False             
"""
"""
1. Write a function square elements which takes a lst and replaces each element
with the square of that element. Mutate lst rather than returning a new list.
"""
def square_elements(lst):
    """Squares every element in lst.
    >>> lst = [1, 2, 3]
    >>> square_elements(lst)
    >>> lst
    [1, 4, 9]
    """
    for i in range(len(lst)):
        lst[i] = lst[i]**2
    return

"""
2. Write a function which reverses a list using mutation. Don't use the reverse list
method.
"""
def reverse_list(lst):
    """Reverses lst in-place (mutating the original list).
    >>> lst = [1, 2, 3, 4]
    >>> reverse_list(lst)
    >>> lst
    [4, 3, 2, 1]
    >>> pi = [3, 1, 4, 1, 5]
    >>> reverse_list(pi)
    >>> pi
    [5, 1, 4, 1, 3]
    """
    l = len(lst)
    for i in range(int(l/2)):
        lst[i],lst[l-i-1] = lst[l-i-1],lst[i]
    return

"""
1. Write a function which takes in a list lst, and two values x and y, and adds as many
ys to the end of lst as there are xs. Do not use the count list method.
"""
def add_this_many(x, y, lst):
    """Adds y to the end of lst the number of times x occurs.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    """
    times = sum([1 for element in lst if element == x])
    for _ in range(times):
        lst.append(y)
    return


"""
2. Write a function that removes all instances of el from lst.
"""
def remove_all(el, lst):
    """Removes all instances of el from lst.
    >>> x = [3, 1, 2, 1, 5, 1, 1, 7]
    >>> remove_all(1, x)
    >>> x
    [3, 2, 5, 7]
    """
    while el in lst:
        lst.remove(el)
"""
3.1 What Would Python Output?
Assume these commands are entered in order after the above code has been executed in
the interpreter.
1.  >>> 'mewtwo'in pokemon
    False
2.  >>> len(pokemon)
    5
3.  >>> pokemon['ditto'] = pokemon['jolteon']
    >>> pokemon[('diglett', 'diglett', 'diglett')] = 51
    >>> pokemon[25] = 'pikachu'
    >>> pokemon
    {'jolteon':135,'ditto':135,('diglett', 'diglett', 'diglett'):51,25:'pikachu',
        'pikachu':25,'dragonair':148,'mew':151}
4.  >>> pokemon['mewtwo'] = pokemon['mew'] * 2
    >>> pokemon
    {'jolteon':135,'ditto':135,('diglett', 'diglett', 'diglett'):51,25:'pikachu',
        'pikachu':25,'dragonair':148,'mew':151,'mewtwo':302}
5.  >>> pokemon[['firetype', 'flying']] = 146
    TypeError
"""
"""
3.3 Dictionary Questions

1. Given a dictionary d, replace all occurences of x as a value (not a key) with y.
"""
def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d
    {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    """
    for key,value in d.items():
        if value == x:
            d[key] = y
    return

"""
1. Given an arbitrarily deep dictionary d, replace all occurences of x as a value (not a key)
with y. Hint: You will need to combine iteration and recursion.
"""
def replace_all_deep(d, x, y):
    """
    >>> d = {1: {2: 3, 3: 4}, 2: {4: 4, 5: 3}}
    >>> replace_all_deep(d, 3, 1)
    >>> d
    {1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}}
    """
    for key in d.keys():
        if type(d[key]) == dict:
            replace_all_deep(d[key],x,y)
        if d[key] == x:
            d[key] = y
    

"""
2. Given a (non-nested) dictionary d, write a function which deletes all occurrences of x
as a value. You cannot delete items in a dictionary as you are iterating through it.
"""
def remove_all(d, x):
    """
    >>> d = {1:2, 2:3, 3:2, 4:3}
    >>> remove_all(d, 2)
    >>> d
    {2: 3, 4: 3}
    """
    remove_key = [key for key in d.keys() if d[key]==x]
    for key in remove_key:
        del d[key]

"""
1. Draw the environment diagram for the following series of calls after make step has
been defined:
>>> s = make_step(3)
>>> s()
>>> s()
"""
def make_step(num):
    def step():
        nonlocal num
        num = num + 1
        return num
    return step
"""
For each of the following pieces of code, explain what's wrong with the use of nonlocal.
1.  a = 5
    def add_one(x):
        nonlocal x
        x += 1
    >>> add_one(a)
    nonlocal can not be used if its parent frame does not define variable x
2. a = 5
    def another_add_one():
        nonlocal a
        a += 1
    >>> another_add_one(a)
    nonlocal is not appliable for variables in the global frame.
"""
"""
1. Given the definition of make shopkeeper below, draw the environment diagram.
"""
def make_shopkeeper(total_gold):
    def buy(cost):
        nonlocal total_gold
        if total_gold < cost:
            return 'Go farm some more champions'
        total_gold = total_gold - cost
        return total_gold
    return buy
infinity_edge, zeal, gold = 3800, 1100, 3800
shopkeeper = make_shopkeeper(gold - 1000)
shopkeeper(zeal)
shopkeeper(infinity_edge)
