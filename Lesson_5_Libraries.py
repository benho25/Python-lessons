# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 18:26:16 2019

@author: cho01
"""
'''
A library is a collection of modules, but the terms are often used interchangeably, 
especially since many libraries only consist of a single module, so don’t worry if you mix them.
'''
'''
Use import to load a library module into a program’s memory.
Then refer to things from the module as module_name.thing_name.
Python uses . to mean “part of”.
Using math, one of the modules in the standard library
'''

import math

print('pi is', math.pi)
print('cos(pi) is', math.cos(math.pi))

# Use help to learn about the contents of a library module

help(math)

#Import specific items from a library module to shorten programs.
#Use from ... import ... to load only specific items from a library module.
#Then refer to them directly without library name as prefix.

from math import cos, pi

print('cos(pi) is', cos(pi)) # no need for math.cos notice the difference between the first one


# Use import ... as ... to give a library a short alias while importing it
import math as m

print('cos(pi) is', m.cos(m.pi))
cos(pi) is -1.0

# Question and more information
'''
You want to select a random character from a string:

bases = 'ACTTGCTTGAC'
Which standard library module could help you?
Which function would you select from that module? Are there alternatives?
Try to write a program that uses the function.
'''

from random import randrange
bases = 'ACTTGCTTGAC'
random_index = randrange(len(bases))
print(bases[random_index])
# more compactly:

from random import randrange

print(bases[randrange(len(bases))])
Perhaps you found the random.sample function? It allows for slightly less typing:

from random import sample

print(sample(bases, 1)[0])


''''
Key points
Most of the power of a programming language is in its libraries.

A program must import a library module in order to use it.

Use help to learn about the contents of a library module.

Import specific items from a library to shorten programs.

Create an alias for a library when importing it to shorten programs.
''''