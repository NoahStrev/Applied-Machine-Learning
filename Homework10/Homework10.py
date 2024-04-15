import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import accuracy_score, confusion_matrix

data = pd.read_csv('quality.csv')
print(data.info())

label_dict = {'B':0,
               'G':1}
data.label =[label_dict[item] for item in data.label]

X = data.drop(columns = ['label'])
y = data.label

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.3, random_state=15)

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X_train,y_train)
y_pred = logreg.predict(X_test)

from sklearn import metrics

print('\n\nAccuracy score:')
print(accuracy_score(y_test,y_pred))

print('\n\nConfusion matrix:')
print(confusion_matrix(y_test,y_pred))

import matplotlib.pyplot as plt
y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr,tpr,_ = metrics.roc_curve(y_test,y_pred_proba)
auc = metrics.roc_auc_score(y_test,y_pred_proba)

print('\n\nauc score:')
print(auc)

plt.plot(fpr,tpr,label='data1,auc='+str(auc))
plt.legend(loc=4)
plt.show()

predict_for = pd.DataFrame({
    "num_words": [18],
    "num_characters": [95],
    "num_misspelled": [2],
    "bin_end_qmark": [0],
    "num_interrogative": [2],
    "bin_start_small": [0],
    "num_sentences": [2],
    "num_punctuations": [3]
    })

prediction_result = logreg.predict(predict_for)
print(prediction_result)

predict_for2 = pd.DataFrame({
    "num_words": [18],
    "num_characters": [95],
    "num_misspelled": [2],
    "bin_end_qmark": [0],
    "num_interrogative": [2],
    "bin_start_small": [0],
    "num_sentences": [2],
    "num_punctuations": [3]
    })

prediction_result = logreg.predict(predict_for2)
print(prediction_result)
