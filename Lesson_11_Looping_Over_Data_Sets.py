# -*- coding: utf-8 -*-
"""
Created on Wed May  1 23:48:15 2019

@author: cho01
"""

''''

Use a for loop to process files given a list of their names.
A filename is just a character string.
And lists can contain character strings.
'''

import os
os.chdir (r"C:\Users\cho01\Documents\carpentries\data")
import pandas as pd
for filename in ['gapminder_gdp_africa.csv', 'gapminder_gdp_asia.csv']:
    data = pd.read_csv(filename, index_col='country')
    print(filename, data.min())

#Use glob.glob to find sets of files whose names match a pattern.
    '''
  In Unix, the term “globbing” means “matching a set of files with a pattern”.
The most common patterns are:
* meaning “match zero or more characters”
? meaning “match exactly one character”
Python contains the glob library to provide pattern matching functionality
The glob library contains a function also called glob to match file patterns
E.g., glob.glob('*.txt') matches all files in the current directory whose names end with .txt.
Result is a (possibly empty) list of character strings.
'''
import glob
print('all csv files in data directory:', glob.glob('*.csv'))

#Use glob and for to process batches of files.
for filename in glob.glob('gapminder_*.csv'):
    data = pd.read_csv(filename)
    print(filename, data['gdpPercap_1952'].min())
'''
This includes all data, as well as per-region data.
Use a more specific pattern in the exercises to exclude the whole data set.
But note that the minimum of the entire data set is also the minimum of one of the data sets, which is a nice check on correctness.
'''

'''
Write a program that reads in the regional data sets and plots the average GDP per capita for each region over time in a single chart.
'''
import glob
import pandas as pd
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)
for filename in glob.glob('data/gapminder_gdp*.csv'):
    dataframe = pd.read_csv(filename)
    # extract region from the filename, expected to be in the format 'data/gapminder_gdp_<region>.csv'
    region = filename.rpartition('_')[2][:-4] 
    dataframe.mean().plot(ax=ax, label=region)
plt.legend()
plt.show()

'''
Use a for loop to process files given a list of their names.

Use glob.glob to find sets of files whose names match a pattern.

Use glob and for to process batches of files.
'''