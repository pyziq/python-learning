"""
1. What would Python print?
>>> [i + 1 for i in [1, 2, 3, 4, 5] if i % 2 == 0]
>>> [3,5]
>>> [i * i for i in [5, -1, 3, -1, 3] if i > 2]
>>> [25,9,9]
>>> [[y * 2 for y in [x, x + 1]] for x in [1, 2, 3, 4]]
>>> [[2,4],[4,6],[6,8],[8,10]]
"""
"""
2. Define a function foo that takes in a list lst and returns a new list that keeps only
the even-indexed elements of lst and multiples each of those elements by the corresponding
index.
"""
def foo(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> foo(x)
    [0, 6, 20]
    """
    return [lst[i]*i for i in range(len(lst)) if i % 2 == 0]
"""
A tree has both a root value and a sequence of branches. In our implementation, we
represent the branches as lists of subtrees.
The arguments to the constructor, tree, as a value for the root and a list of branches
The selectors are root and branches.
"""
# Constructor
def tree(value, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [value] + list(branches)
# Selectors
def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

#We have also provided two convenience functions, is leaf and is tree:

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
"""
1. Define a function square tree(t) that squares every item in the tree t. It should
return a new tree. You can assume that every item is a number.
"""
def square_tree(t):
    """Return a tree with the square of every element in t"""
    sq_branch = [square_tree(branch) for branch in branches(t)]
    return tree(root(t)**2,sq_branch)

t = tree(8,[tree(3,[tree(9,[tree(4)]),tree(5),tree(6)]),tree(2,[tree(10)])])

"""
2. Define a function height(t) that returns the height of a tree. Recall that the height
of a tree is the length of the longest path from the root to a leaf.
"""
def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 0
    return 1 + max([height(branch) for branch in branches(t)])

"""
3. Define a function tree size(t) that returns the number of nodes in a tree.
"""
def tree_size(t):
    """Return the size of a tree."""
    if is_leaf(t):
       return 0
    return 1 + sum([tree_size(branch) for branch in branches(t)])        
        


"""
4. Define a function tree max(t) that returns the largest number in a tree.
"""
def tree_max(t):
    """Return the max of a tree."""
    if is_leaf(t):
        return root(t)
    return max([tree_max(branch) for branch in branches(t)]+[root(t)])
"""
1. An expression tree is a tree that contains a function for each non-leaf root, which
can be either add or mul. All leaves are numbers. Implement eval tree, which
evaluates an expression tree to its value. You may find the functions reduce and
apply to all, introduced during lecture, useful.
"""
def reduce(fn, s, init):
    reduced = init
    for x in s:
        reduced = fn(reduced, x)
    return reduced

def apply_to_all(fn, s):
    return [fn(x) for x in s]

from operator import add, mul
def eval_tree(tree):
    """Evaluates an expression tree with functions as root
    >>> eval_tree(tree(1))
    1
    >>> expr = tree(mul, [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree(add, [expr, tree(4)]))
    10
    """
    if is_leaf(tree):
        return root(tree)
    func,subtrees = root(tree),branches(tree)
    init = 0 if func == add else 1
    return reduce(func,apply_to_all(eval_tree,subtrees),init)
"""
2. We can represent the hailstone sequence as a tree in the figure below, showing the
route different numbers take to reach 1. Remember that a hailstone sequence starts
with a number n, continuing to n/2 if n is even or 3n + 1 if n is odd, ending with
1. Write a function hailstone tree(n, h) which generates a tree of height h,
containing hailstone numbers that will reach n.
"""
def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will reach N
    , with height H.
    >>> hailstone_tree(1, 0)
    [1]
    >>> hailstone_tree(1, 4)
    [1, [2, [4, [8, [16]]]]]
    >>> hailstone_tree(8, 3)
    [8, [16, [32, [64]], [5, [10]]]]
    """
    if  h == 0:
        return  tree(n)
    branches = [hailstone_tree(2*n,h-1)]
    if (n-1) %3 == 0 and (n-1) //3 >1:
        branches += [hailstone_tree((n-1)//3,h-1)]
    return tree(n,branches)

"""
3. Define the procedure find path(tree, x) that, given a rooted tree tree and a
value x, returns a list containing the nodes along the path required to get from the
root of tree to a node x. If x is not present in tree, return None. Assume that the
elements in tree are unique.
For the following tree, find path(t, 5) should return [2, 7, 6, 5]
"""
def find_path(tree, x):
    """ Return a path in a tree to a leaf with value X,
    None if such a leaf is not present.
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree
    (11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 6)
    [2, 7, 6]
    >>> find_path(t, 10)
    """
    if root(tree) == x:
        return [x]
    for path in [find_path(branch,x) for branch in branches(tree)]:
        print(path)
        if path:
            return [root(tree)]+path
  