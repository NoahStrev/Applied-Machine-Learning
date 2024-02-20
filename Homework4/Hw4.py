# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
mydf = pd.read_csv('NFL2023Season.csv')

# 1) Print the Dataframe
print('\n\n1) **********')
print(mydf)

# 2) Printing a single row
print('\n\n2) **********')
print(mydf.loc[13])

# 3) Printing the adjacent columns
print('\n\n3) **********')
print(mydf[['NFL Team', 'PCT']])

# 4) Descriptive Stats for Winning Percent
print('\n\n4) Winning Percent **********')
print('The Max is', mydf['PCT'].max())
print('The Min is', mydf['PCT'].min())
print('The Mean is', mydf['PCT'].mean())
print('The Median is', mydf['PCT'].median())
print('The Range is ', np.ptp(mydf['PCT']))
print('The Standard Deviation is ', mydf['PCT'].std())
print('The Variance is ', mydf['PCT'].var())

# 5) Descriptive Stats for Points For
print('\n\n5) Points For **********')
print('The Max is', mydf['PointsFor'].max())
print('The Min is', mydf['PointsFor'].min())
print('The Mean is', mydf['PointsFor'].mean())
print('The Median is', mydf['PointsFor'].median())
print('The Range is ', np.ptp(mydf['PointsFor']))
print('The Standard Deviation is ', mydf['PointsFor'].std())
print('The Variance is ', mydf['PointsFor'].var())

# 6) Net Points Histogram

hist = mydf.hist(column='Net Pts', figsize=[10,7], bins=11)
plt.title('Histogram of Net Points')

for ax in hist.flatten():
    ax.set_xlabel("Net Points")
    ax.set_ylabel("Count")
plt.show()
