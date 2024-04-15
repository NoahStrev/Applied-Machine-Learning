import numpy
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

mydf = pd.read_csv('FiveFeaturesOneDependent.csv')

print(mydf)

print(mydf.info())

# predict X6
# use all of the other features
y = mydf['X6']
X = mydf[['X1','X2','X3','X4','X5']]

# alternatively we could X = mydf.drop(columns = ['X6'])
X = sm.add_constant(X)

LRModel = sm.OLS(y,X).fit()
print('Model summary:')
print(LRModel.summary())

# Pretty good model for predicting X6
# can we get a sense as to which variables might be more influential?
X = mydf.drop(columns = ['X6'])
# pip install seabon
import seaborn as sns
fig,ax = plt.subplots(5,1,figsize=(8,12))
for i, col in enumerate(X.columns):
    xfeature = col
    sns.scatterplot(data = mydf, x = xfeature, y = 'X6', ax = ax[i])
plt.tight_layout()
plt.show()
