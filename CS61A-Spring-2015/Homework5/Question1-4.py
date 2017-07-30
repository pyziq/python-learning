"""
Question 1

Write a version of the make_withdraw function that returns password-protected withdraw functions. That is, make_withdraw should take a password argument (a string) in addition to an initial balance. The returned function should take two arguments: an amount to withdraw and a password.

A password-protected withdraw function should only process withdrawals that include a password that matches the original. Upon receiving an incorrect password, the function should:

1.Store that incorrect password in a list, and
2.Return the string 'Incorrect password'.
"""
def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    "*** YOUR CODE HERE ***"
    wrong_password = []
    def withdraw(amount,attempts):
        nonlocal balance
        nonlocal password
        nonlocal wrong_password
        if len(wrong_password) >= 3:
                return "Your account is locked. Attempts: ",wrong_password[0:3]
        if attempts in password:
            if amount > balance:
                return 'Insufficient funds'
            balance = balance -amount
            return balance
        else:
            wrong_password.append(attempts)
            return 'Incorrect password'
    return withdraw
"""
Question 2
Suppose that our banking system requires the ability to make joint accounts. Define a function make_joint that takes three arguments.

A password-protected withdraw function,
The password with which that withdraw function was defined, and
A new password that can also access the original account.
The make_joint function returns a withdraw function that provides additional access to the original account using either the new or old password. Both functions draw down the same balance. 
Incorrect passwords provided to either function will be stored and cause the functions to be locked after three wrong attempts.

Hint: The solution is short (less than 10 lines) and contains no string literals! 
The key is to call withdraw with the right password and interpret the result. 
You may assume that all failed attempts to withdraw will return some string (for incorrect passwords, locked accounts, or insufficient funds), while successful withdrawals will return a number.
Use type(value) == str to test if some value is a string:
"""
def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    if type(withdraw(0,old_password)) == str:
        return withdraw(0,old_password)
    def joint(amount,attempt):
        if attempt == old_password or attempt == new_password:
            return withdraw(amount,old_password)
        return withdraw(amout,attempt)
    return joint

"""
Question 3

Create a class called VendingMachine that represents a vending machine for some product. 
A VendingMachine object returns strings describing its interactions. See the doctest below for examples:
"""
class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"
    def __init__ (self,product,price):
        self.product = product
        self.price = price
        self.balance = 0
        self.stock = 0
    def restock(self,n):
        self.stock = self.stock+n
        return "Current " + self.product +" stock: "+str(self.stock)
    def vend(self):   
        if self.stock < 1:
            return "Machine is out of stock"
        else:
            if self.balance == self.price:
                self.stock -= 1
                self.balance = 0
                return "Here is your " + self.product
            elif self.balance > self.price:
                self.stock -= 1
                change = self.balance-self.price
                self.balance = 0
                return "Here is your " + self.product +" and $" +str(change)+" change"
            elif self.balance < self.price:
                return "You must balance $"+str(self.price-self.balance)+" more" 
    def deposit(self,n):
        self.balance += n
        if self.stock < 1:
            if self.balance > 0:
                change = self.balance
                self.balance = 0
                return "Machine is out of stock. Here is your $"+str(change)
        return "Current balance: $"+str(self.balance)
        
"""
Question 4

Create a class called MissManners that promotes politeness among our objects. A MissManners object takes another object on construction. 
It has one method, called ask. It responds by calling methods on the object it contains, but only if the caller said please first.

Hint: Your implementation will need to use the *args notation that allows functions to take a flexible number of arguments:
"""
class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    >>> fussy_three = MissManners(3)
    >>> fussy_three.ask('add', 4)
    'You must learn to say please first.'
    >>> fussy_three.ask('please add', 4)
    'Thanks for asking, but I know not how to add'
    >>> fussy_three.ask('please __add__', 4)
    7
    """
    "*** YOUR CODE HERE ***"
    def __init__ (self,object):
        self.object = object
    def ask(self,message,*args):
        if not message.startswith('please'):
            return 'You must learn to say please first.'
        attr = message[len('please '):]
        if not hasattr(self.object,attr):
            return "Thanks for asking, but I know not how to "+attr
        return getattr(self.object,attr)(*args)