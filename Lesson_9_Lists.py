# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:13:40 2019

@author: cho01
"""

'''
A list stores many values in a single structure.
Doing calculations with a hundred variables called pressure_001, pressure_002, etc., would be at least as slow as doing them by hand.
Use a list to store many values together.
Contained within square brackets [...].
Values separated by commas ,.
Use len to find out how many values are in a list.
'''
pressures = [0.273, 0.275, 0.277, 0.275, 0.276]
print('pressures:', pressures)
print('length:', len(pressures))
print('zeroth item of pressures:', pressures[0])
print('fourth item of pressures:', pressures[4])

#Lists’ values can be replaced by assigning to them
pressures[0] = 0.265
print('pressures is now:', pressures)
print(pressures)

#Appending items to a list lengthens it.
#Use list_name.append to add items to the end of a list.
primes = [2, 3, 5]
print('primes is initially:', primes)
primes.append(7)
primes.append(9)
print('primes has become:', primes)
'''
#append is a method of lists.
Like a function, but tied to a particular object.
Use object_name.method_name to call methods.
Deliberately resembles the way we refer to things in a library.
We will meet other methods of lists as we go along.
Use help(list) for a preview.
extend is similar to append, but it allows you to combine two lists. For example:
 '''
teen_primes = [11, 13, 17, 19]
middle_aged_primes = [37, 41, 43, 47]
print('primes is currently:', primes)
primes.extend(teen_primes)
print('primes has now become:', primes) #joins the list together
primes.append(middle_aged_primes)
print('primes has finally become:', primes)

#Note that while extend maintains the “flat” structure of the list, appending a list to a list makes the result two-dimensional.
print('primes before removing last item:', primes)
del primes[4] #no. 9 is remove
print('primes after removing last item:', primes)

# The empty list contains no values []
#A single list may contain numbers, strings, and anything else.

goals = [1, 'Create lists.', 2, 'Extract items from lists.', 3, 'Modify lists.']

#Get single characters from a character string using indexes in square brackets.
element = 'carbon'
print('zeroth character:', element[0])
print('third character:', element[3])

'''
Things to note:
    Cannot change the characters in a string after it has been created.
Immutable: can’t be changed after creation.
In contrast, lists are mutable: they can be modified in place.
Python considers the string to be a single value with parts, not a collection of values.
'''

#Stepping through a list
element = 'fluorine'
print(element[::2])
print(element[::-1])

element = 'lithium'
print(element[0:20])
print(element[-1:3]) #nth

#Take note
# Program A
letters = list('gold')
result = sorted(letters)
print('letters is', letters, 'and result is', result)
# Program B
letters = list('gold')
result = letters.sort()
print('letters is', letters, 'and result is', result)

#sorted(letters) returns a sorted copy of the list letters (the original list letters remains unchanged), while letters.sort() 
#sorts the list letters in-place and does not return anything.

#new = old makes new a reference to the list old; new and old point towards the same object.

#new = old[:] however creates a new list object new containing all elements from the list old; new and old are different objects.
# Program A
old = list('gold')
new = old      # simple assignment
new[0] = 'D'
print('new is', new, 'and old is', old)
# Program B
old = list('gold')
new = old[:]   # assigning a slice
new[0] = 'D'
print('new is', new, 'and old is', old)

'''
A list stores many values in a single structure.

Use an item’s index to fetch it from a list.

Lists’ values can be replaced by assigning to them.

Appending items to a list lengthens it.

Use del to remove items from a list entirely.

The empty list contains no values.

Lists may contain values of different types.

Character strings can be indexed like lists.

Character strings are immutable.

Indexing beyond the end of the collection is an error.
'''