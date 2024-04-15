import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model

data = pd.read_csv('HWG.csv')
print(data.info())

X = data.drop(columns = ['Gender'])
y = data.Gender

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2, random_state=15)

from sklearn.linear_model import LogisticRegression

# use the default parameters
logreg = LogisticRegression()
# fit the model with data
logreg.fit(X_train,y_train)

y_pred = logreg.predict(X_test)

# import metrics
from sklearn import metrics

conf_matrix = metrics.confusion_matrix(y_test,y_pred)
print(conf_matrix)

target_names = ['Female', 'Male']
print(metrics.classification_report(y_test,y_pred,target_names=target_names))

import matplotlib.pyplot as plt
y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr,tpr,_ = metrics.roc_curve(y_test,y_pred_proba)
auc = metrics.roc_auc_score(y_test,y_pred_proba)
plt.plot(fpr,tpr,label='data1,auc='+str(auc))
plt.legend(loc=4)
plt.show()

predict_for = pd.DataFrame({
    "Height": [70],
    "Weight": [180]
    })

prediction_result = logreg.predict(predict_for)
print(prediction_result)

predict_for2 = pd.DataFrame({
    "Height": [65],
    "Weight": [120]
    })

prediction_result = logreg.predict(predict_for2)
print(prediction_result)
