# LR model from a CSV dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

pd.options.display.max_columns = None
pd.options.display.max_rows = None

mydf = pd.read_csv('incomedata.csv')
print(mydf)
print(mydf.info())

# There is some missing data in the Job satisfaction column of the data
# If these are not dealt with the model wil lcome back with Nan results

# Method 1:
# Fill the NaN values with the median value
# by using an inline function

mydf2 = mydf.apply(lambda x: x.fillna(x.median()), axis=0) # axis 0 is row
print(mydf2)
print(mydf2.info())

# Method 2:
# Remove the rows with the NaN values



mydf = mydf2

# get names of cols in two ways:
# (a) .info
# (b)
for col in mydf:
    print(col)

# ignore the Sample column -- drop it from the dataframe
mydf = mydf.drop(columns = ['Sample'])
print(mydf.info())

# is LR appropriate??
##plt.scatter(mydf.income, mydf['job satisfaction'])
##plt.show()

# correlation between income and job satisfaction?
print('\n\nCORRELATION:')
# using numpy:
print(np.corrcoef(mydf.income,  mydf['job satisfaction'])[0][1])
# using pandas:
print(mydf['income'].corr(mydf['job satisfaction']))

# ********** LEARNING MODEL --- LR **********
# identify the independent and dependent variables
X = mydf.income
y = mydf['job satisfaction']

# using statsmodels means we add a constant to x
X = sm.add_constant(X)

LRModel = sm.OLS(y,X).fit()
print(LRModel.summary())

line = LRModel.params
y_int = line[0] #line.iloc[0] if later Python
slope = line[1]
print('slope', slope, 'y intercept', y_int)
