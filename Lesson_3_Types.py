# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:40:40 2019

@author: cho01
"""

"""
Every value in a program has a specific type.
Integer (int): represents positive or negative whole numbers like 3 or -512.
Floating point number (float): represents real numbers like 3.14159 or -2.5.
Character string (usually called “string”, str): text.
Written in either single quotes or double quotes (as long as they match).
The quote marks aren’t printed when the string is displayed.
"""
print(type(52))
fitness = 'average'
print (type(fitness))

# a value type determines what the program can do it for strings + and *
print (5-3)
print('hello' - 'h') # not supported

full_name = 'Ahmed' + ' ' + 'Walsh'
print(full_name)

separator = '=' * 10
print(separator) #Multiplying a character string by an integer N creates a new string that consists of that character string repeated N times.Since multiplication is repeated addition.

# for length 
print(len(full_name))
print(len(52)) #no length

print(1 + '2') #cannot add numbers and string
# look at the difference 
print(1 + int('2')) 
print(str(1) + '2')

'''
Can mix integers and floats freely in operations.
Integers and floating-point numbers can be mixed in arithmetic.
Python 3 automatically converts integers to floats as needed. (Integer division in Python 2 will return an integer, the floor of the division.)
'''
print('half is', 1 / 2.0)
print('three squared is', 3.0 ** 2)

first = 1
second = 5 * first
first = 2
print('first is', first, 'and second is', second)

#In Python 3, the // operator performs integer (whole-number) floor division, 
#the / operator performs floating-point division, and the ‘%’ (or modulo) operator calculates and returns the remainder from integer division:

print('5 // 3:', 5//3)
print('5 / 3:', 5/3)
print('5 % 3:', 5%3)

num_subjects = 600
num_per_survey = 42
num_surveys = num_subjects // num_per_survey + 1

print(num_subjects, 'subjects,', num_per_survey, 'per survey:', num_surveys)

#Stings to Numbers
print("string to float:", float("3.4"))
print("float to int:", int(3.4))

print("fractional string to int:", int("3.4")) #print("fractional string to int:", int("3.4"))


'''
SUMARY
Every value has a type.

Use the built-in function type to find the type of a value.

Types control what operations can be done on values.

Strings can be added and multiplied.

Strings have a length (but numbers don’t).

Must convert numbers to strings or vice versa when operating on them.

Can mix integers and floats freely in operations.

Variables only change value when something is assigned to them.
'''