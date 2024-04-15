import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix

data = pd.read_csv('dropoutdata.csv')
pd.options.display.max_columns = None
print(data)
print(data.info())

# RECODE THE NONUMERIC DATA
# LOOK AT TWO DIFFERENT WAYS -- (a) REPLACE (b) DICTIONARY
# RECODE Family_Income using REPLACE
data.replace('LOW',0, inplace=True)
data.replace('MEDIUM',1, inplace=True)
data.replace('HIGH',2, inplace=True)
# USE dictionary to recode the GPA
GPA_dict = {'A':4,'AB':4,'B':3,'BC':3,'C':2,'D':1}
data.GPA=[GPA_dict[item] for item in data.GPA]

X = data.drop(columns=['Dropout'])
y = data.Dropout

# split 70-30
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.3, random_state=0)

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
fig = plt.figure(figsize=(10,20))
tree.plot_tree(dectree,feature_names=X.columns.tolist())
plt.show()
