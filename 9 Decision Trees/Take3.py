import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix

data = pd.read_csv('customerdataGens.csv')
pd.options.display.max_columns = None
print(data)
print(data.info())

data.drop(columns = ['User ID'], inplace=True)

# RECODE GENDER -- male 0 and female 1
gender_dict = {'Male':0,'Female':1}
data.Gender =[gender_dict[item] for item in data.Gender]

# RECODE GENERATION

generation_dict = {'Baby Boomer':0,
               'Gen X':1,
               'Millenial':2,
               'Gen Z':3}
data.Generation =[generation_dict[item] for item in data.Generation]

# *************************************************
# * CATEGORIZE THE SALARY VALUES
# *************************************************

def categorizeSalary(sal):
    cat = sal/10000
    if cat < 4:
        return 0
    elif cat > 8:
        return 2
    else:
        return 1

data['EstimatedSalary'] = data['EstimatedSalary'].apply(categorizeSalary)
    

# SEPARATE X and y

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

# Predict yes will purchase or no probably not
# for a female millenial 75k salary
sal = categorizeSalary(75000)
xpredict = [[1,2,sal]]
X_predicts = pd.DataFrame(xpredict,columns=X.columns)
print('\n\nPredicting data: ', X_predicts)
yForX_predicts = dectree.predict(X_predicts)
print(yForX_predicts)
