import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix

data = pd.read_csv('lensesdata.csv')
pd.options.display.max_columns = None
print(data)
print(data.info())

# RECOMMEND = 1 patient should be prescribed hard contact lenses
#             2                              soft
#             3                NOT be prescribed contact lenses

X = data.drop(columns=['RECOMMEND'])
y = data.RECOMMEND

# split 70-30
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.3, random_state=0)

# CREATE THE MODEL
#dectree = tree.DecisionTreeClassifier()
dectree = tree.DecisionTreeClassifier(criterion= 'entropy')
dectree.fit(X_train, y_train)

# HOW GOOD IS OUR MODEL ??
predictions = dectree.predict(X_test)
print('\n\nAccuracy score:')
print(accuracy_score(y_test,predictions))

print('\n\nConfusion matrix:')
print(confusion_matrix(y_test,predictions))

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,20))
tree.plot_tree(dectree,feature_names=X.columns.tolist())
plt.show()
