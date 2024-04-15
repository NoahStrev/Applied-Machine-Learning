import numpy as np
import pandas as pd

# 1 ******************************

pd.options.display.max_columns=None
pd.options.display.max_rows=None

wheat_df = pd.read_csv('wheat.csv')
print(wheat_df)
print(wheat_df.info())

# 2 There is no categorical data ******************************
# 3 ******************************

X = wheat_df.drop(columns=['Variety'])
y = wheat_df['Variety']

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X = scaler.fit_transform(X)

# 4 ******************************

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

# 5 ******************************

print("\n\nMean", np.mean(X_train))
print("Standard Deviation", np.std(X_train))

# 6 ******************************

from sklearn.neighbors import KNeighborsClassifier
kNN_model = KNeighborsClassifier(n_neighbors = 8)
# 8, 10, 15
kNN_model.fit(X_train,y_train)

# 7 ******************************

y_predicts = kNN_model.predict(X_test)
num_correct = np.where(y_predicts == y_test, 1, 0).sum()
print('\n\nNumber correct is ', num_correct, ' out of ', len(y_predicts))
rate = num_correct / len(y_predicts) * 100
print('which is around ', str(round(rate)) + '%')

print('\n\n *** SKLEARN ACCURACY INFORMATION *** ')
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_predicts))

print('\n\nClassification report')
from sklearn.metrics import classification_report
print(classification_report(y_test,y_predicts))

print('\n\nConfusion matrix')
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_predicts))

# 8 ******************************

from sklearn.model_selection import cross_val_score
k_values = [i for i in range(1,50)]
scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors = k)
    score = cross_val_score(knn,X,y,cv=4) # 4 train and 1 test from original data
    scores.append(np.mean(score))

import seaborn as sns
import matplotlib.pyplot as plt
sns.lineplot(x=k_values, y = scores,marker='o')
plt.xlabel("K values")
plt.ylabel("Accuracy score")
plt.show()

# 11 ******************************

xpredict = [[19.09, 16.61, .8722, 6.3, 3.737, 6.682, 6.053]]
X_predicts = pd.DataFrame(xpredict,columns=['Area','Perim','Compactness', 'Length', 'Width', 'AsymmCoeff', 'GrooveLength'])
X_predicts = scaler.transform(X_predicts)
y_p = kNN_model.predict(X_predicts)
print('Recommendation is', y_p)

xpredict = [[11.34, 12.82, .8596, 5.053, 2.9, 3.347, 4.999]]
X_predicts = pd.DataFrame(xpredict,columns=['Area','Perim','Compactness', 'Length', 'Width', 'AsymmCoeff', 'GrooveLength'])
X_predicts = scaler.transform(X_predicts)
y_p = kNN_model.predict(X_predicts)
print('Recommendation is', y_p)
