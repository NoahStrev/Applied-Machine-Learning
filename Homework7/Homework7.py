import numpy as np
import pandas as pd
from sklearn import linear_model
df = pd.read_csv('Concrete_samples.csv')

pd.options.display.max_columns = None
# pd.options.display.max_rows = None
dfcols = df.columns
print(df)
print(df.info())

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(df_scaled, columns = dfcols)
print(df_scaled)

# SEPARATE X and y, and drop MPA
X = df.drop('MPA', axis=1)
y = df.MPA

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.4, random_state=0)

regr_linear = linear_model.LinearRegression()
regr_Lasso = linear_model.Lasso(alpha=0.001) # set ridge lasso
regr_Ridge = linear_model.Ridge(alpha=0.001) # set ridge alpha

# train the models
regr_linear.fit(X_train, y_train)
regr_Lasso.fit(X_train, y_train)
regr_Ridge.fit(X_train, y_train)

# RUN TYPE
print('Run 20%-80%, alpha = 0.1')

# print the coefficients LINEAR
print('\n\nLinear model coefficients:')
for idx, col_name in enumerate(X_train.columns):
    print('The coefficient for {} is {}'.format(col_name, regr_linear.coef_[idx]))
print('The intercept is {}'.format(regr_linear.intercept_))

# print the coefficients LASSO
print('\n\nLasso model coefficients:')
for idx, col_name in enumerate(X_train.columns):
    print('The coefficient for {} is {}'.format(col_name, regr_Lasso.coef_[idx]))
print('The intercept is {}'.format(regr_linear.intercept_))

# print the coefficients RIDGE
print('\n\nRidge model coefficients:')
for idx, col_name in enumerate(X_train.columns):
    print('The coefficient for {} is {}'.format(col_name, regr_Ridge.coef_[idx]))
print('The intercept is {}'.format(regr_linear.intercept_))

# accuracy LINEAR
print('\n\nLinear model accuracy:')
print(regr_linear.score(X_train,y_train))
print(regr_linear.score(X_test,y_test))

# accuracy Lasso
print('\n\nLasso model accuracy:')
print(regr_Lasso.score(X_train,y_train))
print(regr_Lasso.score(X_test,y_test))

# accuracy Ridge
print('\n\nRidge model accuracy:')
print(regr_Ridge.score(X_train,y_train))
print(regr_Ridge.score(X_test,y_test))
