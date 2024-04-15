import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 1) Download the dataset and confirm theres no missing data

mydf = pd.read_csv('Environs.csv')
print("1) Download the dataset and confirm theres no missing data **********")
print(mydf.info())


# 2) Find the best predictor for Design

print("\n\n2) Find the best predictor for Design **********")
y = mydf.Design
##X = mydf.Pressure
##X = mydf.Time
##X = mydf['Heat Factor']
##X = mydf[ ['Time', 'Pressure'] ]
##X = mydf[ ['Time', 'Heat Factor'] ]
##X = mydf[ ['Pressure', 'Heat Factor'] ]
X = mydf[ ['Pressure', 'Heat Factor', 'Time'] ]

X = sm.add_constant(X)

LRModel_Radio = sm.OLS(y,X).fit()
print(LRModel_Radio.summary())
print(LRModel_Radio.params)
# 3) Finding the equation

y_int = 389.1659
pressure_slope = 5.3185
heat_slope = -3.0165
time_slope = 2.1247
print("\n\n3) Find the equation to calculate the design value **********")
print('y =', pressure_slope, '* pressure +', time_slope, '* time +', heat_slope, '* heat factor +', y_int)

# 4) Predicting the Design value for the three features

a_values = [34.85, 31.84, 38.0]
b_values = [34.6, 35.56, 33.99]
c_values = [128.48, 132.08, 133.0]
y_predicts = []

def predict(a,b,c):
    y = pressure_slope * a + heat_slope * b + time_slope * c + y_int
    return y

for i in range(len(a_values)):
    a = a_values[i]
    b = b_values[i]
    c = c_values[i]
    y_predicts.append(predict(a,b,c))
    
print("\n\n4) Use the equation to predict the design value **********")
print('Predicted values:', y_predicts)
