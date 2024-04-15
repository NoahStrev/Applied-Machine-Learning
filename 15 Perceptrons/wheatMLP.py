# Redo of Homework 8 where we achieved .8888 accuracy
# when we created a kNN model

# Let's see how mLP does:

import sklearn
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

dataseeds = pd.read_csv('wheat.csv')
print(dataseeds.info())

X = dataseeds.drop(columns=['Variety'])
y = dataseeds.Variety

scaler = StandardScaler()
X = scaler.fit_transform(X)
print(X.shape, y.shape) # X.shape shows the number of features (x, THIS NUMBER)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2, random_state=1)

mlp_model = MLPClassifier(solver ='sgd', alpha=.0000001,max_iter=2000,
                          verbose=True, hidden_layer_sizes=(7,4,3),
                          random_state=1)
    # (Number of input features, number inbetween the other two, number of possible outputs)
    
mlp_model.fit(X_train,y_train)
# NOW WE HAVE A MODEL

print('Accuracy score:', mlp_model.score(X_test, y_test))

print(mlp_model.predict_proba(X_test))
print(y_test)
