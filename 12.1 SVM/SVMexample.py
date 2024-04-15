

import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt


from sklearn.feature_extraction.text import CountVectorizer

from sklearn import svm

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

##import nltk
###nltk.download('all')

smstxt_data = pd.read_csv('spamORham.csv')

print(smstxt_data.info())
print(smstxt_data['Category'].value_counts())


import AIN210b
smstxt_data['Cleanedup_Message'] = smstxt_data.Message.apply(AIN210b.clean_data1)
smstxt_data['Cleanedup_Message'] = smstxt_data.Cleanedup_Message.apply(AIN210b.clean_data2)

print(smstxt_data.head())

X = smstxt_data['Cleanedup_Message'].values
y = smstxt_data['Category'].values


X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.3)


cv = CountVectorizer() 

from sklearn.pipeline import Pipeline
svc_pipeline = Pipeline([('vect', cv), ('clf', SVC())])
svc_pipeline.fit(X_train, y_train)
y_pred = svc_pipeline.predict(X_test)
print('Model Accuracy for the Train set:', svc_pipeline.score(X_train, y_train))
print('Model Accuracy for the Test set:', svc_pipeline.score(X_test, y_test))
from sklearn.metrics import confusion_matrix, classification_report
print(pd.DataFrame(confusion_matrix(y_test, y_pred), columns=['ham', 'spam'], index=['ham', 'spam']))
print(classification_report(y_test, y_pred))
evaluation_df = pd.DataFrame({'Message': X_test, 'Actual Label': y_test, 'Predicted Label': y_pred})
print(evaluation_df.head(10))
