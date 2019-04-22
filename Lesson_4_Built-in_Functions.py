# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 00:10:54 2019

@author: cho01
"""

'''
A function may take zero or more arguments.
We have seen some functions already — now let’s take a closer look.
An argument is a value passed into a function.
len takes exactly one.
int, str, and float create a new value from an existing one.
print takes zero or more.
print with no arguments prints a blank line.
Must always use parentheses, even if they’re empty, so that Python knows a function is being called.
'''

print('before')
print()
print('after')

'''
Other commonly used functions max,min and round
Use max to find the largest value of one or more values.
Use min to find the smallest.
Both work on character strings as well as numbers.
“Larger” and “smaller” use (0-9, A-Z, a-z) to compare letters.
max and min must be given at least one argument.
“Largest of the empty set” is a meaningless question.
And they must be given things that can meaningfully be compared.

'''
print(max(1, 2, 3))
print(min('a', 'A', '0')) # Larger” and “smaller” use (0-9, A-Z, a-z) to compare letters.
print(max(1, 'a'))

# round will round off a floating point-number,By default, rounds to zero decimal places.
round(3.712)
round(3.712, 1) # to specify the number of decimal places we want.

# use help() for every built-in function 
help(round)

'''
Use comments to add documentation to programs.

A function may take zero or more arguments.

Commonly-used built-in functions include max, min, and round.

Functions may only work for certain (combinations of) arguments.

Functions may have default values for some arguments.

Use the built-in function help to get help for a function.

The Jupyter Notebook has two ways to get help.

Every function returns something.

Python reports a syntax error when it can’t understand the source of a program.

Python reports a runtime error when something goes wrong while a program is executing.

Fix syntax errors by reading the source code, and runtime errors by tracing the program’s execution.
'''
