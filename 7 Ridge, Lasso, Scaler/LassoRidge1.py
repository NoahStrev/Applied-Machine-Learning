import numpy as np
import pandas as pd
from sklearn import linear_model

traindata = pd.read_csv('train.csv')
# SCALE IT
from sklearn.preprocessing import StandardScaler
std_scaler = StandardScaler()
dfcols = traindata.columns
print(dfcols)
df_scaled = std_scaler.fit_transform(traindata)
df_scaled = pd.DataFrame(df_scaled, columns = dfcols)

print(df_scaled)

X_train = df_scaled.drop(columns=['SalePrice', 'Id'])
y_train = df_scaled.SalePrice

# Linear Regression model, Lasso model and a Ridge model
regr_linear = linear_model.LinearRegression()
regr_Lasso = linear_model.Lasso(alpha=0.1) # try others later
regr_Ridge = linear_model.Ridge(alpha=0.1) # do not have to be the same

# train the models
regr_linear.fit(X_train, y_train)
regr_Lasso.fit(X_train, y_train)
regr_Ridge.fit(X_train, y_train)

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

# Load the test data
testdata = pd.read_csv('test.csv')
# SCALE THE TEST DATA BECAUSE WE SCALED THE TRAINING DATA
std_scaler = StandardScaler()
df_scaledt = std_scaler.fit_transform(testdata)
df_scaledt = pd.DataFrame(df_scaledt, columns = dfcols)

X_test = df_scaledt.drop(columns=['SalePrice', 'Id'])
y_test = df_scaledt.SalePrice

# print accuracy score for each model -- how well it was trained for the test data
# if accuracy score is poor then model is NOT a good predictor probably due to overfitting

print('\n\nLinear model accuracy:')
print(regr_linear.score(X_train,y_train))
print(regr_linear.score(X_test,y_test))
print()

print('\n\nLasso model accuracy:')
print(regr_Lasso.score(X_train,y_train))
print(regr_Lasso.score(X_test,y_test))
print()

print('\n\nRidge model accuracy:')
print(regr_Ridge.score(X_train,y_train))
print(regr_Ridge.score(X_test,y_test))
print()
