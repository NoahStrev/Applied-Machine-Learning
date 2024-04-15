# RANDOM FOREST EXAMPLE
# Using it to get an idea as to what Random Forest is all about
# So working with some bank data and using it to predict when we should pursue
# a new potential customer with effort

import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

bank_data = pd.read_csv('bank.csv', delimiter=';')

bank_data.drop(columns=['job','marital', 'education','housing','loan','contact',
                        'month', 'poutcome', 'age','pdays'], inplace=True)

print(bank_data)
print(bank_data.info())

# map the default column which contains no and yes to 0's and 1's respectively
# let's treat some unkown data as no for this example
defau_dic = {'no':0,'yes':1,'unknown':0}
bank_data.default = [defau_dic[item] for item in bank_data.default]

y_dict = {'no':0,'yes':1}
bank_data['y'] = [y_dict[item] for item in bank_data.y]

# Split the data into X and Y
X = bank_data.drop('y', axis=1)
y = bank_data['y']

print(X)
print(X.info())

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2)

# RANDOM FOREST
rf = RandomForestClassifier()
rf.fit(X_train,y_train)

# Evaluate the model
y_pred = rf.predict(X_test)
acc = accuracy_score(y_test,y_pred)
print('\n\nAccuracy:', acc)

print('\n\nConfusion matrix:')
print(confusion_matrix(y_test,y_pred))

import matplotlib.pyplot as plt
# Export the first three trees from the forest
# there are 100 by default

from sklearn import tree
for i in range(3):
    # graph the tree(s)
    fig = plt.figure(figsize=(10,20))
    tree.plot_tree(rf.estimators_[i],feature_names=X.columns.tolist())
    plt.show()

feature_scores = pd.Series(rf.feature_importances_,
                            index=X_train.columns.sort_values(ascending=False))
print(feature_scores)
