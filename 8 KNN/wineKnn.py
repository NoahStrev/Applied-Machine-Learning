# A spirits distributor is acuiring wines for sales
# Of course everyone claims that their wine of good quality
# Well there is a plethora of wine data available attesting to what
# constitutes a quality wine and one such data set: wine.csv

# Step 1 Input the data
import numpy as np
import pandas as pd
wine_df = pd.read_csv('wine.csv')
#print(wine_df)
#print(wind_df.info())

pd.options.display.max_columns=None
pd.options.display.max_rows=None

wine_df.drop(columns=['color', 'quality'],inplace=True)
##print(wine_df)
##print(wine_df.info())

# ??????? how might you determine if all 12 features are relevent??
# print(wine_df.corr())
             
# Scale it (NORMALLY IN KNN YOU DON'T HAVE TO SCALE)
# Make sure to also scale predictor points when using the resulting model

# 2. Normalize the data  (scale the data)  standardization
# Do you want to scale the y-values
# the y value is high_quality
# No, we do not want to scale the y values!

X = wine_df.drop(columns=['high_quality'])
y = wine_df['high_quality']

from sklearn.preprocessing import StandardScaler

#You have to make the scaler object next
scaler = StandardScaler()
X = scaler.fit_transform(X)

# What is the mean of X?
# What is the standard deviation for X?

# 3. Split the data into train and test datasets
# Try to begin with:  70-30 (%s)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

# THAT WAS ALL THE SAME AS ALWAYS
# HERE IS WHERE NEW KNN SHIT STARTS

# 4. Create a kNN Classifier model with k=3 neibhors
from sklearn.neighbors import KNeighborsClassifier
kNN_model = KNeighborsClassifier(n_neighbors = 42)
kNN_model.fit(X_train,y_train)

# 5. Test the accuracy of the model
y_predicts = kNN_model.predict(X_test)
num_correct = np.where(y_predicts == y_test, 1, 0).sum()
print('\n\nNumber correct is ', num_correct, ' out of ', len(y_predicts))
rate = num_correct / len(y_predicts) * 100
print('which is around ', str(round(rate)) + '%')

# 5.5 Find the optimal value for k
# The goal is to find the smallest optimal value
# this is generally referred to as "Occam's Razor"
# also called the "principle of parsimony"
##from sklearn.model_selection import cross_val_score
##k_values = [i for i in range(1,50)]
##scores = []
##
##for k in k_values:
##    knn = KNeighborsClassifier(n_neighbors = k)
##    score = cross_val_score(knn,X,y,cv=4) # 4 train and 1 test from original data
##    scores.append(np.mean(score))
##    
### plot the scores
##import seaborn as sns
##import matplotlib.pyplot as plt
##sns.lineplot(x=k_values, y = scores,marker='o')
##plt.xlabel("K values")
##plt.ylabel("Accuracy score")
##plt.show()

### 6. Compare to sklearn accuracy info
##print('\n\n *** SKLEARN ACCURACY INFORMATION *** ')
##from sklearn.metrics import accuracy_score
##print(accuracy_score(y_test, y_predicts))
##
##
##print('\n\nClassification report')
##from sklearn.metrics import classification_report
##print(classification_report(y_test,y_predicts))
##
##print('\n\nConfusion matrix')
##from sklearn.metrics import confusion_matrix
##print(confusion_matrix(y_test,y_predicts))
