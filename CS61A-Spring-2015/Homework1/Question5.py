'''
Question 5: Challenge Problem (optional)

Write a one-line program that prints itself, using only the following features of the Python language:

Number literals
Assignment statements
String literals that can be expressed using single or double quotes
The arithmetic operators +, -, *, and /
The built-in print function
The built-in eval function, which evaluates a string as a Python expression
The built-in repr function, which returns an expression that evaluates to its argument
You can concatenate two strings by adding them together with + and repeat a string by multipying it by an integer. 
Semicolons can be used to separate multiple statements on the same line. E.g.,
>>> c='c';print('a');print('b' + c * 2)
a
bcc

'''
from __future__ import print_function

s = 'print("s = " + repr(s)+"; eval(s)")'; eval(s)
