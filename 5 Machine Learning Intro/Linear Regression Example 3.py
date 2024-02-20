import matplotlib.pyplot as plt

ads_millions = [2.3, 2.8, 3.2, 3.5, 4.2]
sales = [5034221, 5036453, 5038242, 5040231, 5043873]

from sklearn.linear_model import LinearRegression

# NOTE: sklearn NEEDS a 2D array
import numpy as np
Xnp = np.array(ads_millions)

# reshape the array so that it is n rows and 1 column
XLR = Xnp.reshape(-1,1)
LRModel = LinearRegression()
LRModel.fit(XLR, sales)

# LRModel is now our machine learning model for our dataset
y_int = LRModel.intercept_
slope = LRModel.coef_[0]

print('slope', slope, 'y intercept', y_int)
print(LRModel.coef_)


try_these = [3.8, 3.0, 2.5, 4.1]

y_predicts = []

def predict(x):
    y = slope * x + y_int
    return y

for x in try_these:
    y_predicts.append(predict(x))

print('debugging:', y_predicts)

# Use sklearn to make the predictions
# because soon we will have training data AND test data to assess the model
# Because we can use our LR models to make the predictions as opposed to
# defining our function (i.e.predict)

# Need to get the try_these into a 2D array

try_these_np = np.array(try_these)
try_these_LR = try_these_np.reshape(-1,1)
model_predicts = LRModel.predict(try_these_LR)

print('\n\nModel predictions:')
print(model_predicts)
