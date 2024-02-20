import matplotlib.pyplot as plt

ads_millions = [2.3, 2.8, 3.2, 3.5, 4.2]

sales = [5034221, 5036453, 5038242, 5040231, 5043873]

# IS the Linear Regression ML model appropriate to consider?

plt.scatter(ads_millions, sales)
# plt.show()

import numpy as np
import pandas as pd
import statsmodels.api as sm
# pip install statsmodels

print('Correlation and Coefficient')
#print(np.corrcoef(ads_millions, sales))
print(np.corrcoef(ads_millions, sales)[0,1])

X = ads_millions
y = sales

# statsmodels ML algorithm for regression requires this:
X = sm.add_constant(X)

# Now ready to generate the Linear Regression model:
LRModel = sm.OLS(y, X).fit()
# print(LRModel.summary())
line = LRModel.params
y_int = line[0]
slope = line[1]
print(line, y_int, slope)

### x1 coef is the slope, const coef is the y intercept
##predA = 5127.2815534 * 2.5 + 5022196.69902912
##print('\n\nIf spend 2.5 on advertising:', predA)
##
##predB = 5127.2815534 * 4 + 5022196.69902912
##print('\n\nIf spend 4 on advertising:', predB)


try_these = [3.8, 3.0, 2.5, 4.1]

# Try these as predictors for corresponding sales
# and then plot the predictions and the regression line

y_predicts = []

def predict(x):
    y = slope * x + y_int
    return y

for x in try_these:
    y_predicts.append(predict(x))

print('debugging:', y_predicts)

# so now plot
# format the y values
txt = "{ycoord:.2f}"

plt.scatter(try_these, y_predicts)
# label points
for i in range(len(try_these)):
    y_p = y_predicts[i] / 1000000
    annotation = str(try_these[i]), ",", txt.format(ycoord = y_p)
    # annotation = str(try_these[i]), ",", str(y_predicts[i])
    plt.annotate(annotation, xy=(try_these[i], y_predicts[i]))
    
plt.xlabel('Advertisement')
plt.ylabel('Sales')
plt.plot(try_these, y_predicts, "red", alpha=0.9)
plt.show()
