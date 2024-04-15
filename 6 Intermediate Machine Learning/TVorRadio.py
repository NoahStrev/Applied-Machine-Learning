import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

mydf = pd.read_csv('AdsMedia.csv')
print(mydf)
print(mydf.info())

mydf = mydf.drop(columns = ['Sample'])

# look at TVAds first
plt.scatter(mydf['TVAds'], mydf.Sales)
plt.show()

X = mydf.TVAds
y = mydf.Sales

X = sm.add_constant(X)

LRModel_TV = sm.OLS(y,X).fit()
print(LRModel_TV.summary())

# look at RadioAds first
plt.scatter(mydf['RadioAds'], mydf.Sales)
plt.show()

X = mydf.RadioAds
y = mydf.Sales

X = sm.add_constant(X)

LRModel_Radio = sm.OLS(y,X).fit()
print(LRModel_Radio.summary())

# * * * * * *  NOW USE BOTH TV AND RADIO  * * * * * *
y = mydf.Sales
X = mydf[ ['TVAds', 'RadioAds'] ]

X = sm.add_constant(X)
LR_Model = sm.OLS(y,X).fit()
print(LR_Model.summary())

# DATA VISUALIZATION -- 3 variables so plot
import matplotlib.pyplot as plt
max = plt.axes(projection="3d")
max.scatter3D(mydf['TVAds'], mydf['RadioAds'], mydf['Sales'], color="green")
plt.title("simple 3D scatter plot")
plt.show()
