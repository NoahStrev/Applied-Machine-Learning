import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix

data = pd.read_csv('tips.csv')
pd.options.display.max_columns = None
print(data)
print(data.info())

# Recode Tip Percent

def categorizeTip(tip):
    if tip < .162:
        return 0
    else:
        return 1

data['Tip Level'] = data['Tip percent'].apply(categorizeTip)

# Recode Day

day_dict = {'Thur':0,'Fri':1,'Sat':2,'Sun':0}
data.day =[day_dict[item] for item in data.day]

# Recode Time

time_dict = {'Lunch':0,'Dinner':1}
data.time =[time_dict[item] for item in data.time]

data.drop(columns = ['total_bill'], inplace=True)
data.drop(columns = ['Tip percent'], inplace=True)

print(data.info())

# SEPARATE X and y

X = data.drop(columns=['Tip Level'])
y = data['Tip Level']

# split 60-40
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.4)

# CREATE THE MODEL
dectree = tree.DecisionTreeClassifier()
#dectree = tree.DecisionTreeClassifier(criterion= 'entropy')
dectree.fit(X_train, y_train)
##
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
