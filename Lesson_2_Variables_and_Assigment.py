# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:09:49 2019

@author: cho01
"""

"""
Taken from : http://swcarpentry.github.io/python-novice-gapminder/02-variables/index.html"
Use VARIABLES to store values.
VARIABLES are names for values.
In Python the = symbol assigns the value on the right to the name on the left.
The variable is created when a value is assigned to it.
Here, Python assigns an age to a variable age and a name in quotes to a variable first_name.
Variable names
can only contain letters, digits, and underscore _ (typically used to separate words in long variable names)
cannot start with a digit
Variable names that start with underscores like __alistairs_real_age have a special meaning 
so we won’t do that until we understand the convention.

"""

age = 42
first_name = 'Ahmed'

"""
Use print() to display values.
Python has a built-in function called print that prints things as text.
Call the function (i.e., tell Python to run it) by using its name.
Provide values to the function (i.e., the things to print) in parentheses.
To add a string to the printout, wrap the string in single or double quotes.
The values passed to the function are called arguments

"""
print(first_name, 'is', age, 'years old')

"""
kernel -> restart & run all

"""
# VARiables can be used in calculations

age = age + 3
print ('Age in three years:', age)

# INDEXING pythons counts from 0
atom_name = 'helium'
print (atom_name[0])

"""
A part of a string is called a substring. A substring can be as short as a single character.
An item in a list is called an element. Whenever we treat a string as if it were a list, the string’s elements are its individual characters.
A slice is a part of a string (or, more generally, any list-like thing).
We take a slice by using [start:stop], where start is replaced with the index of the first element we want and stop is replaced with the index of the element just after the last element we want.
Mathematically, you might say that a slice selects [start:stop).
The difference between stop and start is the slice’s length.
Taking a slice does not change the contents of the original string. Instead, the slice is a copy of part of the original string.
"""

atom_name = 'sodium'
print (atom_name[0:3])
print (atom_name[:7])
# count the number of elements
print(len('sodium'))


#It is important to help other people understand what the program does
flabadab = 42
ewr_422_yY = 'Ahmed'
print(ewr_422_yY, 'is', flabadab, 'years old')

'''
Summary
Use variables to store values.

Use print to display values.

Variables persist between cells.

Variables must be created before they are used.

Variables can be used in calculations.

Use an index to get a single character from a string.

Use a slice to get a substring.

Use the built-in function len to find the length of a string.

Python is case-sensitive.

Use meaningful variable names.
'''