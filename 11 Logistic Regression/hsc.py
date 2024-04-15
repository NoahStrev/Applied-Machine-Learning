# Horshoe crabs - Multinomial Regression
# Classification

from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings('ignore')

hscrabs = pd.read_csv('horseshoecrabs.csv')
print(hscrabs.info())
print(hscrabs.head())

X = hscrabs.drop(columns = ['spine'])
y = hscrabs.spine

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2, random_state=5)

logmodel = LogisticRegression(multi_class="multinomial")
logmodel.fit(X_train,y_train)

acc = accuracy_score(logmodel.predict(X_test),y_test)
print('Accuracy score is:', acc)

predict_for = pd.DataFrame({
    "crab": [30],
    "sat": [0],
    "y": [0],
    "weight": [2.1],
    "width": [24.3],
    "color": [2]
    })

prediction_result = logmodel.predict(predict_for) # 3 - not great reproduction forecast
print(prediction_result)

predict_for2 = pd.DataFrame({
    "crab": [15],
    "sat": [14],
    "y": [1],
    "weight": [2.3],
    "width": [26],
    "color": [2]
    })

prediction_result2 = logmodel.predict(predict_for2) # 3 - not great reproduction forecast
print(prediction_result2)
