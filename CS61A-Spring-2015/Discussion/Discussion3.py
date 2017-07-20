'''
1. The Hadley Cycle describes the process of atmospheric circulation caused by rising
air at the equator and falling air at about 30 degrees North or South. The air loses
water vapor to rain as it rises from the equator. Consequently, the falling cold air is
dry, so that many regions around 30 degrees from the equator comprise of desert.
Write a function near thirty(city, diff) that checks whether an input city is
within diff degrees of 30 degrees N or 30 degrees S.
'''
def near_thirty(city, diff):
   city_lat = get_lat(city)
   return abs(city_lat - 30) <= 30 or abs(city_lat+30) <= 30

'''
2. Implement closer city, a function that takes a latitude, longitude, and two cities,
and returns the name of the city that is relatively closer to the provided latitude and
longitude.
You may only use selectors and constructors (introduced above) for this question. You
may also use the distance function defined above.
'''
def closer_city(lat, lon, city1, city2):
    city = make_city('city',lat,lon)
    return get_name(city1) if distance(city,city1) < distance(city,city2) else get_name(city2)
'''
1. Write a function that returns the given rational number x raised to positive power e.
'''
from math import pow
def rational_pow(x, e):
    return 1 if e == 0 else mul_rational(x,rational_pow(x,e-1))

'''
2. The irrational number e ≈ 2.718 can be generated from an infinite series. Let’s try
calculating it using our rational number data type! The mathematical formula is as
follows:
e =1/0! + 1/1! + 1/2! + 1/3! + 1/4! ...
Write a function approx e that returns a rational number approximation of e to iter
amount of iterations. We’ve provided a factorial function.
'''
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
def approx_e(iter=100):
    s = rational(1,factorial(0))
    for i in range(1,iter):
        tmp = rational(1,factorial(i))
        s = add_rationals(s,tmp)
    return s
'''
3. Implement the following rational number methods.
'''
def inverse_rational(x):
    """Returns the inverse of the given non-zero rational
    number"""
    n = number(x)
    d = denom(x)
    return rational(d,n)

def div_rationals(x, y):
    """Returns x / y for given rational x and non-zero
    rational y"""
    return mul_rational(x,inverse_rational(y))

'''
1. Implement the constructors and selectors for the unit data abstraction using lists. Each
unit will have a string catchphrase and an integer amount of damage.
'''
def make_unit(catchphrase, damage):
    return [catchphrase,damage]

def get_catchphrase(unit):
    return unit[0]

def get_damage(unit):
    return unit[1]
'''
1. Let’s simulate a battle between units! In a battle, each unit yells its respective catchphrase,
then the unit with more damage wins. Implement battle, which displays
the catchphrases of the first and second unit in that order, then returns the unit that
does more damage. The first unit wins ties. Don’t violate any data abstractions!
'''
def battle(first, second):
    """Simulates a battle between the first and second unit
    >>> zealot = make_unit(’My life for Aiur!’, 16)
    >>> zergling = make_unit(’GRAAHHH!’, 5)
    >>> winner = battle(zergling, zealot)
    GRAAHHH!
    My life for Aiur!
    >>> winner is zealot
    True
    """
    print(get_catchphrase(first))
    print(get_catchphrase(second))
    return first if get_damage(first) > get_damage(second) else second

'''
1. Write constructors and selectors for a data abstraction that combines an integer amount
of minerals and gas together into a bundle. Use functional pairs.
'''
def pair(x, y):
    """Return a function that represents a pair."""
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get

def select(p, i):
    """Return the element at index i of pair p"""
    return p(i)

def make_resource_bundle(minerals, gas):
    return pair(minerals,gas)

def get_minerals(bundle):
    return select(bundle,0)

def get_gas(bundle):
    return select(bundle,1)

def make_pair(a, b):
    return [a, b]
def get_pair(pair, i):
    return pair[i]
def make_pair_of_pairs(pair1, pair2):
    return make_pair(pair1, pair2)

'''
Let’s make a building pair that is constructed with a unit data type and a resource
bundle data type. This time take your choice of lists or functional pairs in representing
a building. Make sure not to violate any data abstractions.
'''
def make_building(unit, bundle):
    return pair(unit, bundle)

def get_unit(building):
    return select(building, 0)

def get_bundle(building):
    return select(building, 1)

'''
2. Implement build unit. This function takes in a building and resource bundle. First,
it checks whether the amount of each resources provided in the bundle is greater than
or equal to the amount the building was constructed with. If it is not, it prints out ”We
require more minerals!” if more minerals are needed, or ”We require more vespene
gas!” if more gas is needed, or both. Otherwise, it creates a new copy of the building’s
unit and returns it.
'''
def build_unit(building, bundle):
    """Constructs a unit if given the minimum amount of
    resources. Otherwise, prints an error message.
    >>> barracks = make_building(make_unit(’Go go go!’, 6),
                             make_resource_bundle(50, 0))
    >>> marine = build_unit(barracks, make_resource_bundle(20,
        20))
    We require more minerals!
    >>> marine = build_unit(barracks, make_resource_bundle(50,
        0))
    >>> print(get_catchphrase(marine))
    Go go go!
    """
    have_minerals = get_minerals(bundle)
    have_gas = get_gas(bundle)
    required_minerals = get_minerals(get_bundle(building))
    required_gas = get_gas(get_bundle(building))
    if have_minerals < required_minerals:
        return print('We required more minerals')
    if have_gas < required_gas
        return print('We required more gas')
    return get_unit(building)
'''
3. Data abstractions are extremely useful when the underlying implementation of the
abstraction changes. For example, after writing a program using lists as a way of
storing pairs, suddenly someone switches the implementation to functional pairs. If
we correctly use constructors and selectors, our program should still work perfectly.
Reimplement the resource abstraction to use lists instead of functional pairs. Then
verify that all the code that use the resource still works
'''
def make_resource_bundle(minerals, gas):
    return [minerals, gas]

def get_minerals(bundle):
    return bundle[0]

def get_gas(bundle):
    return bundle[1]
        