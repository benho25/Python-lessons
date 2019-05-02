# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:18:20 2019

@author: cho01
"""

'''
Use if statements to control whether or not a block of code is executed.
An if statement (more properly called a conditional statement) controls whether some block of code is executed or not.
Structure is similar to a for statement:
First line opens with if and ends with a colon
Body containing one or more statements is indented (usually by 4 spaces)
'''

mass = 3.54
if mass > 3.0:
    print(mass, 'is large') # not printed

mass = 2.07
if mass > 3.0:
    print (mass, 'is large')
    
'''
Conditionals are often used inside loops.
Not much point using a conditional when we know the value (as above).
But useful when we have a collection to process.
'''
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is large')
        
'''
Use else to execute a block of code when an if condition is not true.
else can be used following an if.
Allows us to specify an alternative to execute when the if branch isn’t taken.
'''
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is large')
    else:
        print(m, 'is small')
        
'''
Use elif to specify additional tests.
May want to provide several alternative choices, each with its own test.
Use elif (short for “else if”) and a condition to specify these.
Always associated with an if.
Must come before the else (which is the “catch all”).
'''
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 9.0:
        print(m, 'is HUGE')
    elif m > 3.0:
        print(m, 'is large')
    else:
        print(m, 'is small')
        
#Conditions are tested once, in order.
grade = 85
if grade >= 70:
    print('grade is C')
elif grade >= 80:
    print('grade is B')
elif grade >= 90:
    print('grade is A') #only the first is chosen

#Often use conditionals in a loop to “evolve” the values of variables.
velocity = 10.0
for i in range(5): # execute the loop 5 times
    print(i, ':', velocity)
    if velocity > 20.0:
        print('moving too fast')
        velocity = velocity - 5.0
    else:
        print('moving too slow')
        velocity = velocity + 10.0
print('final velocity:', velocity)

#ompound Relations Using and, or, and Parentheses
mass     = [ 3.54,  2.07,  9.22,  1.86,  1.71]
velocity = [10.00, 20.00, 30.00, 25.00, 20.00]

i = 0
for i in range(5):
    if mass[i] > 5 and velocity[i] > 20:
        print("Fast heavy object.  Duck!")
    elif mass[i] > 2 and mass[i] <= 5 and velocity[i] <= 20:
        print("Normal traffic")
    elif mass[i] <= 2 and velocity[i] <= 20:
        print("Slow light object.  Ignore it")
    else:
        print("Whoa!  Something is up with the data.  Check it")
        
'''
Use if statements to control whether or not a block of code is executed.

Conditionals are often used inside loops.

Use else to execute a block of code when an if condition is not true.

Use elif to specify additional tests.

Conditions are tested once, in order.

Create a table showing variables’ values to trace a program’s execution.
'''