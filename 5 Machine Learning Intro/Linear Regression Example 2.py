import matplotlib.pyplot as plt

ads_millions = [2.3, 2.8, 3.2, 3.5, 4.2]

sales = [5034221, 5036453, 5038242, 5040231, 5043873]

# IS the Linear Regression ML model appropriate to consider?

# plt.scatter(ads_millions, sales)
# plt.show()

# pip install scipy
from scipy import stats

X = ads_millions
y = sales

# Create the LR ML model
slope, intercept, r, p, std_err = stats.linregress(X, y)

print(slope, intercept)

try_these = [3.8, 3.0, 2.5, 4.1]

# Try these as predictors for corresponding sales
# and then plot the predictions and the regression line

y_predicts = []

def predict(x):
    y = slope * x + intercept
    return y

for x in try_these:
    y_predicts.append(predict(x))

print('debugging:', y_predicts)
