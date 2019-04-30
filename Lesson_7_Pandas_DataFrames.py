# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 23:39:49 2019

@author: cho01
"""

"""
Note about Pandas DataFrames/Series
A DataFrame is a collection of Series; The DataFrame is the way Pandas represents a table, and Series is the data-structure Pandas use to represent a column.

Pandas is built on top of the Numpy library, which in practice means that most of the methods defined for Numpy Arrays apply to Pandas Series/DataFrames.

What makes Pandas so attractive is the powerful interface to access individual records of the table, proper handling of missing values, and relational-databases operations between DataFrames.
"""

#Use DataFrame.iloc[..., ...] to select values by their (entry) position
#To access a value at the position [i,j] of a DataFrame, we have two options, depending on what is the meaning of i in use. Remember that a DataFrame provides a index as a way to identify the rows of the table; a row, then, has a position inside the table as well as a label, which uniquely identifies its entry in the DataFrame.


#Use DataFrame.iloc[..., ...] to select values by their (entry) position
#Can specify location by numerical index analogously to 2D version of character selection in strings.
import pandas as pd
import os
os.chdir (r"C:\\Users\\cho01\\Documents\\carpentries\\data")
data = pd.read_csv('gapminder_gdp_europe.csv', index_col='country')
print(data.iloc[0, 0])
print(data.iloc[1, 0])
print(data.iloc[4, 1]) #row then columm


#Use DataFrame.loc[..., ...] to select values by their (entry) label.
#Can specify location by row name analogously to 2D version of dictionary keys.
data = pd.read_csv('gapminder_gdp_europe.csv', index_col='country')
print(data.loc["Albania", "gdpPercap_1952"])

#Use : on its own to mean all columns or all rows.
#Just like Python’s usual slicing notation.
print(data.loc["Albania", :])

#Would get the same result printing data.loc["Albania"]

print(data.loc[:, "gdpPercap_1952"]) #print all the rows of that column

'''
Take note
Would get the same result printing data["gdpPercap_1952"]
Also get the same result printing data.gdpPercap_1952 (since it’s a column name)
'''

#Select multiple columns or rows using DataFrame.loc and a named slice
print(data.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972'])

'''
In the above code, we discover that slicing using loc is inclusive at both ends, which differs from slicing using iloc, where slicing indicates everything up to but not including the final index.
'''

#Result of slicing can be used in further operations.
#Usually don’t just print a slice.
#All the statistical operators that work on entire dataframes work the same way on slices.
#E.g., calculate max of a slice.

print(data.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972'].max())
print(data.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972'].min())

'''
Use comparisons to select data based on value.
Comparison is applied element by element.
Returns a similarly-shaped dataframe of True and False.
'''

# Use a subset of data to keep output readable.
subset = data.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972']
print('Subset of data:\n', subset)

# Which values were greater than 10000 ?
print('\nWhere are values large?\n', subset > 10000)

#Select values or NaN using a Boolean mask. 
#A frame full of Booleans is sometimes called a mask because of how it can be used.
mask = subset > 10000
print(subset[mask]) #Get the value where the mask is true, and NaN (Not a Number) where it is false.
                    #Useful because NaNs are ignored by operations like max, min, average, etc.

print(subset[subset > 10000].describe())

'''
Select-Apply-Combine operations
Pandas vectorizing methods and grouping operations are features that provide users much flexibility to analyse their data.

For instance, let’s say we want to have a clearer view on how the European countries split themselves according to their GDP.

We may have a glance by splitting the countries in two groups during the years surveyed, those who presented a GDP higher than the European average and those with a lower GDP.
We then estimate a wealthy score based on the historical (from 1962 to 2007) values, where we account how many times a country has participated in the groups of lower or higher GDP
'''

mask_higher = data.apply(lambda x:x>x.mean())
wealth_score = mask_higher.aggregate('sum',axis=1)/len(data.columns)
wealth_score

data.groupby(wealth_score).sum()

"""
Use DataFrame.iloc[..., ...] to select values by integer location.

Use : on its own to mean all columns or all rows.

Select multiple columns or rows using DataFrame.loc and a named slice.

Result of slicing can be used in further operations.

Use comparisons to select data based on value.

Select values or NaN using a Boolean mask.
"""