# Loading a CSV file into a pandas dataframe
# Then do some basic stats with the df

import pandas as pd
mydf = pd.read_csv('csemploydata.csv')

print(mydf)

pd.options.display.max_rows = 1000
# or None

print(mydf.head())
print(mydf.head(10))

print(mydf.tail())
print(mydf.tail(10))

print(mydf['Average Salary'])

# list the salaries and titles next to each other (adjacent columns)
print(mydf['Average Salary'], mydf['Title']) # no
# print(mydf['Average Salary'], 'Title') # no --> error
print(mydf[['Average Salary', 'Title']]) # YES

saltitle = mydf[['Average Salary', 'Title']]
print(saltitle)
print(type(saltitle)) # it is type: pandas dataframe

print('\n\nUsing info method: ')
print(mydf.info())

print('********** DESCRIPTIVE STATISTICS **********')
print('\n\n')
print('Max Salary is', mydf['Average Salary'].max())
print('Min Salary is', mydf['Average Salary'].min())
print('Mean Salary is', mydf['Average Salary'].mean())
print('Median Salary is', mydf['Average Salary'].median())

d = mydf['Average Salary'].describe()
print('\n\nd is ')
# print(d.mean())
print('\n\ntype', type(d))
print(d['mean'])

print('\n\nRange is ', d['max'] - d['min'])

import numpy as np # want to use ptp
import matplotlib.pyplot as plt

print('\n\nRange of salaries is ', np.ptp(mydf['Average Salary']))

print('\n\Standard Deviation is ', mydf['Average Salary'].std())
print('\n\Variance is ', mydf['Average Salary'].var())

# Plot a histogram for average salary
mydf.hist(column = 'Average Salary', figsize[10, 7], bins = 4)

# set the title and axis labels
plt.title('Histogram of Average Salary')
plt.title('Salary Values')
plt.title('Frequency')
plt.show()

# ******* HISTOGRAM OPTION 2 ******
mydf.hist(figsize = [10, 7])
