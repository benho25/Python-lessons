# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:21:38 2019

@author: cho01
"""

'''
Break programs down into functions to make them easier to understand.
Human beings can only keep a few items in working memory at a time.
Understand larger/more complicated ideas by understanding and combining pieces.
Components in a machine.
Lemmas when proving theorems.
Functions serve the same purpose in programs.
Encapsulate complexity so that we can treat it as a single “thing”.
Also enables re-use.
Write one time, use many times.
Define a function using def with a name, parameters, and a block of code.
Begin the definition of a new function with def.
Followed by the name of the function.
Must obey the same rules as variable names.
Then parameters in parentheses.
Empty parentheses if the function doesn’t take any inputs.
We will discuss this in detail in a moment.
Then a colon.
Then an indented block of code.
'''

def print_greeting():
    print('Hello!')

def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(1871, 3, 19)
print_date(month=3, day=19, year=1871)

'''
Functions may return a result to their caller using return.
Use return ... to give a value back to the caller.
May occur anywhere in the function.
But functions are easier to understand if return occurs:
At the start to handle special cases.
At the very end, with a final result.
Remember: every function returns something.
A function that doesn’t explicitly return a value automatically returns None.
'''
def average(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)
a = average([1, 3, 4])
print('average of actual values:', a)
print('average of empty list:', average([]))

result = print_date(1871, 3, 19)
print('result of call is:', result)

'''
Break programs down into functions to make them easier to understand.

Define a function using def with a name, parameters, and a block of code.

Defining a function does not run it.

Arguments in call are matched to parameters in definition.

Functions may return a result to their caller using return.
'''