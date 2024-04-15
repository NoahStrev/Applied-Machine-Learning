import numpy as np
import pandas as pd
import statsmodels.api as sm

mydf = pd.read_csv('USCensusHousingBoston.csv')
print(mydf)
print(mydf.info())

# To ignore the records with missing data (not needed here but in the future)
mydf2 = mydf.dropna() # axis = 0 by default

mydf = mydf2
# numpy corrcoef looks like: np.corrcoef(mydf.crim,mydf.nox)
pd.options.display.max_columns = None
print(mydf.corr()) # showing the corrcoef for the entire dataframe

# scatterplot for nox and dis
import matplotlib.pyplot as plt
plt.scatter(mydf.dis, mydf.nox)
plt.show()

## LR MODEL using statsmodel
#X = mydf.dis
#y = mydf.nox

#LRModel = sm.OLS(y,X).fit()
#print(LRModel.summary)
#line = LRModel.params

#LR MODEL using statsmodel
X = mydf.indus
y = mydf.nox

LRModel = sm.OLS(y,X).fit()
print(LRModel.summary())
line = LRModel.params
