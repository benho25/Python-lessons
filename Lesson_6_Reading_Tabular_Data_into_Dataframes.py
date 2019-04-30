# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:59:57 2019

@author: cho01
"""

'''
Use the Pandas library to do statistics on tabular data.
Pandas is a widely-used Python library for statistics, particularly on tabular data.
Borrows many features from R’s dataframes.
A 2-dimenstional table whose columns have names and potentially have different data types.
Load it with import pandas as pd. The alias pd is commonly used for Pandas.
Read a Comma Separate Values (CSV) data file with pd.read_csv.
Argument is the name of the file to be read.
Assign result to a variable to store the data that was read.
'''

import pandas as pd
import os
os.chdir (r"C:\\Users\\cho01\\Documents\\carpentries\\data")
data = pd.read_csv('gapminder_gdp_oceania.csv')
print(data)

#Use index_col to specify that a column’s values should be used as row headings.
data = pd.read_csv('gapminder_gdp_oceania.csv', index_col='country')
print(data)

#Use DataFrame.info to find out more about a dataframe.
data.info()

#The DataFrame.columns variable stores information about the dataframe’s columns.
#Note that this is data, not a method.
#Like math.pi.
#So do not use () to try to call it.
#Called a member variable, or just member.

print(data.columns)
#Use DataFrame.T to transpose a dataframe.
print(data.T)

#Use DataFrame.describe to get summary statistics about data.
print(data.describe())


data_america=pd.read_csv('gapminder_gdp_americas.csv', index_col = 'country')
americas = data_america
print (americas)

print (americas.head(3))

#Note: we could have done the above in a single line of code by ‘chaining’ the commands:
print (americas.T.tail(3))

'''
Use the Pandas library to get basic statistics out of tabular data.

Use index_col to specify that a column’s values should be used as row headings.

Use DataFrame.info to find out more about a dataframe.

The DataFrame.columns variable stores information about the dataframe’s columns.

Use DataFrame.T to transpose a dataframe.

Use DataFrame.describe to get summary statistics about data.

As well as the read_csv function for reading data from a file, Pandas provides a to_csv function to write dataframes to files. Applying what you’ve learned about reading from files, write one of your dataframes to a file called processed.csv. You can use help to get information on how to use to_csv.

'''