# Predict a student's major program
# purpose for academic advisiing
import numpy as np
import pandas as pd

# Read and analyze data characteristics
hs_df = pd.read_csv('hsdata.csv')

# drop id and gender
hs_df.drop(columns=['id', 'gender'],inplace=True)

# NEED TO CONVERT CATEGORICAL DATA
# reason: Knn still calculates distances from data points
# recode ses to numeric (0, 1, 2)
hs_df['ses'].replace(['low', 'middle', 'high'], [0,1,2], inplace=True)
print(hs_df)
print(hs_df.info())

# if all features are important to use
# so normally hs_df.corr()

# Seperate X and y
X = hs_df.drop(columns = ['prog'])
y = hs_df.prog

# Standard Scalar (Normalize) the X values
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the dataset into train and test
# The popular splits are 70-30 and 80-20 and 60-40
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

# create an initial kNN model (later we will modify with "optimal" k)
from sklearn.neighbors import KNeighborsClassifier
kNN_Classifier = KNeighborsClassifier(n_neighbors = 3)
kNN_Classifier.fit(X_train,y_train)

# test the accuracy of the model
y_predicts = kNN_Classifier.predict(X_test)
num_correct = np.where(y_predicts == y_test, 1, 0).sum()
print('\n\nNumber correct is ', num_correct)
rate = num_correct / len(y_predicts) * 100
print('which is around ', str(round(rate)) + '%')

### Compare to sklearn accuracy info
##print('\n\n *** SKLEARN ACCURACY INFORMATION *** ')
##from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
##print(accuracy_score(y_test, y_predicts))
##
##print('\n\nClassification report')
##print(classification_report(y_test,y_predicts))
##
##print('\n\nConfusion matrix')
##print(confusion_matrix(y_test,y_predicts))

### Optimal k search???
##from sklearn.model_selection import cross_val_score
##k_values = [i for i in range(1,100)]
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

# Predict for a student who scored 53 on math and 68 on science and is of ses middle
# feed the X predict data to kNN_Classifier.predict(X_predict)

xpredict = [[1,53,68]]
X_predicts = pd.DataFrame(xpredict,columns=['ses','math','science'])
X_predicts = scaler.transform(X_predicts)
y_p = kNN_Classifier.predict(X_predicts)
print('Recommendation is', y_p)
