import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix

data = pd.read_csv('customerdata.csv')
pd.options.display.max_columns = None
print(data)
print(data.info())

data.drop(columns = ['User ID'], inplace=True)

# RECODE GENDER -- male 0 and female 1
gender_dict = {'Male':0,'Female':1}
data.Gender =[gender_dict[item] for item in data.Gender]

X = data.drop(columns=['Purchased'])
y = data.Purchased

# split 70-30
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.3)

# CREATE THE MODEL
dectree = tree.DecisionTreeClassifier()
#dectree = tree.DecisionTreeClassifier(criterion= 'entropy')
dectree.fit(X_train, y_train)

# HOW GOOD IS OUR MODEL ??
predictions = dectree.predict(X_test)
print('\n\nAccuracy score:')
print(accuracy_score(y_test,predictions))

print('\n\nConfusion matrix:')
print(confusion_matrix(y_test,predictions))

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(20,20))
tree.plot_tree(dectree,feature_names=X.columns.tolist())
plt.show()
