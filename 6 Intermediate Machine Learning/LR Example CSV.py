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

# WHY DO WE BUILD A ML MODEL ???
# BECAUSE WE WISH TO PREDICT

# IN PREDICTING, WE CAN:
# a. Identify individual values
# b. use a dataset of values

# BUT IN "REAL" LIFE -- before we predict using our model, we assess it
# To assess it, we utilize TRAINING data and TEST data
# We build the model using TRAINING data and assess using TEST and then we are either
# confident about to use it for prediction

# to predict use:
# TRY_THESE = [
# need data in range of my X values (otherwise extrapolation)
xmax = mydf['income'].max()
xmin = mydf['income'].min()
print('\n\nmax is', xmax, 'min is ', xmin)

# wish to offer a job to a candidate and we have an idea of a salary range
# the range is $55,000.00 and 62,000
# how much happier will the candidate be with the high end vs the low end
# therefore predict job satisfaction for both salaries
# sincethe ML model is a linear regression model, use the egn of the line
predict_hi = slope * 6.2 + y_int
predict_lo = slope * 5.5 + y_int

print('\n\nhi is', predict_hi, 'lo is ', predict_lo)
