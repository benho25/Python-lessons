# -*- coding: utf-8 -*-
"""
Created on Wed May  1 07:21:37 2019

@author: cho01
"""

"""
matplotlib is the most widely used scientific plotting library in Python.
Commonly use a sub-library called matplotlib.pyplot.
The Jupyter Notebook will render plots inline if we ask it to using a “magic” command.
"""
"""
#matplotlib inline
import matplotlib.pyplot as plt
time = [0, 1, 2, 3]
position = [0, 100, 200, 300]

plt.plot(time, position)
plt.xlabel('Time (hr)')
plt.ylabel('Position (km)')
"""
"""
Plot data directly from a Pandas dataframe.
We can also plot Pandas dataframes.
This implicitly uses matplotlib.pyplot.
Before plotting, we convert the column headings from a string to integer data type, since they represent numerical values
"""


import pandas as pd
import os

os.chdir (r"C:\Users\cho01\Documents\carpentries\data")
data = pd.read_csv('gapminder_gdp_oceania.csv', index_col='country')

# Extract year from last 4 characters of each column name
years = data.columns.str.strip('gdpPercap_')
# Convert year values to integers, saving results back to dataframe
data.columns = years.astype(int)
'''
data.loc['Australia'].plot()
data.T.plot() #transposing data
plt.ylabel('GDP per capita')

plt.style.use('ggplot')
data.T.plot(kind='bar')
plt.ylabel('GDP per capita')
'''

"""
Data can also be plotted by calling the matplotlib plot function directly.
The command is plt.plot(x, y)
The color / format of markers can also be specified as an optical argument: e.g. ‘b-‘ is a blue line, ‘g–’ is a green dashed line.
"""
'''
years = data.columns
gdp_australia = data.loc['Australia']

#plt.plot(years, gdp_australia, 'g--')

# Select two countries' worth of data.
gdp_australia = data.loc['Australia']
gdp_nz = data.loc['New Zealand']

# Plot with differently-colored markers.
#plt.plot(years, gdp_australia, 'b-', label='Australia')
#plt.plot(years, gdp_nz, 'g-', label='New Zealand')

# Create legend.
plt.legend(loc='upper left')
plt.xlabel('Year')
plt.ylabel('GDP per capita ($)')

plt.scatter(gdp_australia, gdp_nz)

data.T.plot.scatter(x = 'Australia', y = 'New Zealand')

'''
#test question
data_europe = pd.read_csv('gapminder_gdp_europe.csv', index_col='country')
data_europe.min().plot(label='min')
data_europe.max().plot(label='max')
plt.legend(loc='best')
plt.xticks(rotation=90) #rotate the x labeling

'''
Key Points
matplotlib is the most widely used scientific plotting library in Python.

Plot data directly from a Pandas dataframe.

Select and transform data, then plot it.

Many styles of plot are available: see the Python Graph Gallery for more options.

Can plot many sets of data together.
plt.savefig('my_figure.png') for saving files

for example
fig = plt.gcf() # get current figure
data.plot(kind='bar')
fig.savefig('my_figure.png')
'''