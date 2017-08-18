class Skittle:
    """A Skittle object has a color to describe it."""
    def __init__(self, color):
        self.color = color


class Bag:
    """A Bag is a collection of Skittles. All bags share the
    number of Bags ever made (sold) and each bag keeps track of
    its Skittles in a list.
    """
    number_sold = 0
    def __init__(self):
        self.skittles = []
        Bag.number_sold += 1
    def tag_line(self):
        """Print the Skittles tag line."""
        print("Taste the rainbow!")
    def print_bag(self):
        print([s.color for s in self.skittles])
    def take_skittle(self):
        """Take the first skittle in the bag (from the front of
        the skittles list).
        """
        return self.skittles.pop(0)
    def add_skittle(self, s):
        """Add a skittle to the bag."""
        self.skittles.append(s)
    def take_color(self, color):
        for s in self.skittles:
            if s.color == color:
                self.skittles.remove(s)
                return s
        return None
    def take_all(self):
        for s in self.skittles:
            print(s.color)
            
    
"""
2.1 Questions

1. What does Python print for each of the following:
>>> johns_bag = Bag()
>>> johns_bag.print_bag()
[]

>>> for color in ['blue', 'red', 'green', 'red']:
... johns_bag.add_skittle(Skittle(color))
>>> johns_bag.print_bag()
['blue', 'red', 'green', 'red']

>>> s = johns_bag.take_skittle()
>>> print(s.color)
blue

>>> johns_bag.number_sold
1

>>> Bag.number_sold
1

>>> soumyas_bag = Bag()
>>> soumyas_bag.print_bag()
[]

>>> johns_bag.print_bag()
['red', 'green', 'red']

>>> Bag.number_sold
2

>>> soumyas_bag.number_sold
2

"""
"""
2. Write a new method for the Bag class called take color, which takes a color and
removes (and returns) a Skittle of that color from the bag. If there is no Skittle
of that color, then it returns None
"""

"""
3. Write a new method for the Bag class called take all, which takes all the Skittles
in the current bag and prints the color of the each Skittle taken from the bag.
"""
class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print('...')

class Dog(Pet):
    def __init__(self, name, owner, color):
        Pet.__init__(self, name, owner)
        self.color = color
    def talk(self):
        print('woof !')

class Cat(Pet):
    def __init__(self, name, owner, lives = 9):
        Pet.__init__(self, name, owner)
        self.lives = lives
    def talk(self):
        print('meow')
    def lose_life(self):
        """A cat can only lose a life if they have at least
        one life. When lives reach zero, the ’is_alive’
        variable becomes False.
        """
        if self.is_alive:
            self.lives -= 1
        if self.is_alive <= 0:
            self.is_alive = False
            print(self.name + 'is dead!')
"""
1. Implement the Cat class by inheriting from the Pet class. Make sure to use superclass
methods wherever possible. In addition, add a lose life method to the Cat class.
""""

"""

2. Assume these commands are entered in order. What would Python output?
>>> class Foo(object):
...     def __init__(self, a):
...         self.a = a
...     def garply(self):
...         return self.baz(self.a)
>>> class Bar(Foo):
...     a = 1
...     def baz(self, val):
...         return val
>>> f = Foo(4)
>>> b = Bar(3)
>>> f.a
4

>>> b.a
3

>>> f.garply()
No attribute 

>>> b.garply()
3

>>> b.a = 9
>>> b.garply()
9

>>> f.baz = lambda val: val * val
>>> f.garply()
16

"""
"""
1. More cats! Fill in the methods for NoisyCat, which is just like a normal Cat. However,
NoisyCat talks a lot, printing twice whatever a Cat says.
"""
class NoisyCat(Cat):
    """A Cat that repeats things twice."""
    def talk(self):
        """Repeat what a Cat says twice."""
        Cat.talk(self)
        Cat.talk(self)

class Vector:
    def __init__(self, vector):
        self.vector = vector
    def __neg__ (self) : 
        "*** YOUR CODE HERE ***"
        return Vector([-i for i in self.vector])
    def __add__ (self, other): 
        "*** YOUR CODE HERE ***"
        assert type(other) == Vector, "Invalid operation!"
        assert len(self) == len(other), "Invalid dimensions!"
        return Vector([self.vector[i] + other.vector[i] for i in range(len(self.vector))])
    def __sub__ (self, other): 
        return self.__add__(-other)
    def __mul__ (self, other): 
        if type(other) == int or type(other) == float:
            "*** YOUR CODE HERE ***"
            return Vector([self.vector[i]*other for i in range(len(self.vector))])
        elif type(other) == Vector:
            return sum([self.vector[i] * other.vector[i] for i in range(len(self.vector))])    
    def __rmul__(self, other): 
        return self.__mul__(other)
    def __len__(self) : 
        return len(self.vector)
    def __getitem__(self, n) : 
        return self.vector[n]