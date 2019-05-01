# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:04:31 2019

@author: cho01
"""
'''
A for loop executes commands once for each value in a collection.
Doing calculations on the values in a list one by one is as painful as working with pressure_001, pressure_002, etc.
A for loop tells Python to execute some statements once for each value in a list, a character string, or some other collection.
“for each thing in this group, do these operations”
'''

for number in [2, 3, 5]:
    print(number)
    
    '''
    The collection, [2, 3, 5], is what the loop is being run on.
The body, print(number), specifies what to do for each value in the collection.
The loop variable, number, is what changes for each iteration of the loop.
The “current thing”.
'''
#Loop variables can be called anything.

for kitten in [2, 3, 5]:
    print(kitten)
    
#The body of a loop can contain many statements.
primes = [2, 3, 5]
for p in primes:
    squared = p ** 2
    cubed = p ** 3
    print(p, squared, cubed)

#Use range to iterate over a sequence of numbers.
#The built-in function range produces a sequence of numbers.
#Not a list: the numbers are produced on demand to make looping over large ranges more efficient.
#range(N) is the numbers 0..N-1
#Exactly the legal indices of a list or character string of length N
print('a range is not a list: range(0, 3)')
for number in range(0,3):
    print(number)

#The Accumulator pattern turns many values into one.
# Sum the first 10 integers.
total = 0
for number in range(10):
   total = total + (number + 1)
print(total)
'''
A for loop executes commands once for each value in a collection.

A for loop is made up of a collection, a loop variable, and a body.

The first line of the for loop must end with a colon, and the body must be indented.

Indentation is always meaningful in Python.

Loop variables can be called anything (but it is strongly advised to have a meaningful name to the looping variable).

The body of a loop can contain many statements.

Use range to iterate over a sequence of numbers.

The Accumulator pattern turns many values into one.
''
