# imports
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

# 2) load the dataset
pd.options.display.max_columns = None
pd.options.display.max_rows = None

mydf = pd.read_csv('rideshare.csv')
##print("2) Print the dataframe and find any nulls **********")
##print(mydf)
##print("\nAny Nulls?:", mydf.info())

# 3) Best Predictor of Distance

##print(mydf.corr())

# After looking through the different correlation coefficents cloud cover
# has the highest absolute value, so it is the best predictor of distance, even
# though it's value is only .75, which isn't great.

# 4) Scatter Plot of Cloud Cover vs Distance

##plt.scatter(mydf.cloudCover, mydf.distance)
##plt.xlabel("Cloud Cover")
##plt.ylabel("Distance")
##plt.show()

# 5) statsmodel OLS predictor

X = mydf.cloudCover
y = mydf.distance
X = sm.add_constant(X)

LRModel = sm.OLS(y,X).fit()
print(LRModel.summary())

line = LRModel.params
y_int = line.iloc[0] #line.iloc[0] if later Python
slope = line.iloc[1]
print("\n\n5) Print the m and b **********")
print('y =', slope, ' * x +', y_int)

# 6) min and max for X (cloud cover)

xmax = mydf.cloudCover.max()
xmin = mydf.cloudCover.min()
print("\n\n6) Print the min and max for X **********")
print('xMax is', xmax, ' and xMin is', xmin)

# 7)Predicting distance with three values (0.0, 0.4, 1.0)

x_values = [0.0, 0.4, 1.0]
y_predicts = []

def predict(x):
    y = slope * x + y_int
    return y

for x in x_values:
    y_predicts.append(predict(x))
    
print("\n\n7) Predict distance for three valid values (0.0, 0.4, 1.0) **********")
print('Predicted values:', y_predicts)

# format the y values
txt = "{ycoord:.2f}"

# 8) Plotting the predicted points

plt.scatter(x_values, y_predicts)
# label points
for i in range(len(x_values)):
    y_p = y_predicts[i]
    annotation = str(x_values[i]), ",", txt.format(ycoord = y_p)
    plt.annotate(annotation, xy=(x_values[i], y_predicts[i]))
    
plt.xlabel('Cloud Cover')
plt.ylabel('Distance')
plt.plot(x_values, y_predicts, "red", alpha=0.9)
plt.show()
