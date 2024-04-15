# MLP MultiLayer Perceptron because we now have one hidden layer

from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier # there is a MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings('ignore')

# LOAD THE DATASET
dataset = fetch_openml("mnist_784", version=1)
X = dataset['data']
y = dataset['target']

# Partition into training and test
X_train, X_test, y_train, y_test = train_test_split(X/255,y,test_size=.2, random_state=1)

mlp = MLPClassifier(solver='sgd', # Stochastic Gradient Descent to min unnecessary backprop
                    max_iter=50,
                    verbose=True, # tell us about it
                    random_state=1,
                    learning_rate_init=.1, # alpha
                    hidden_layer_sizes = (784,100,10)) # input layer, hidden layer, output layer

mlp.fit(X_train,y_train)

y_train_predict = mlp.predict(X_train)
y_test_predict = mlp.predict(X_test)

print('\n\nMultiLayer Perceptron Results:')
print('Training:', accuracy_score(y_train, y_train_predict))
print('Testing:', accuracy_score(y_test, y_test_predict))
