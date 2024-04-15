# Create a simple Single Layer Perceptron (SLP) NN for classification
# An SLP is simply put, a weighted linear sum of input signals

# Use the famous MNIST dataset consisting of a large number of
# handwritten digits
# Very popular dataset for testing NN and Deep Learning NN models

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from sklearn.datasets import fetch_openml
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings # with NN especially later the learning takes place
warnings.filterwarnings('ignore') # within a threshold

# LOAD THE DATASET
mnist_data = fetch_openml("mnist_784", version=1)
X = mnist_data['data']
y = mnist_data['target']
##print('Shape of X:', X.shape, ' shape of y:', y.shape)
##print(y)

# plot the first few images
import matplotlib.pyplot as plt
import numpy as np
for i in range(9):
    j = i%3
    plt.subplot(130+1+j)
    digit = X.iloc[i]
    digit_pixels = np.array(digit).reshape(28,28)
    plt.imshow(digit_pixels)
    plt.axis('off')
    plt.show()

X_train, X_test, y_train, y_test = train_test_split(X/255,y,test_size=.2, random_state=1)

# Create a perceptron and set certain parameters
# max_iter because otherwise we can end up waiting hours or days or ...
# tol which is tolerance which is the learning threshold
# can think of it as an error loss factor

perceptron = Perceptron(random_state=1, max_iter=50, tol=.005)
perceptron.fit(X_train,y_train)

yhat_train_perceptron = perceptron.predict(X_train)
yhat_test_perceptron = perceptron.predict(X_test)

acc_train = accuracy_score(y_train, yhat_train_perceptron)
acc_test = accuracy_score(y_test, yhat_test_perceptron)

print('\n\nAccuracy score for training is:', acc_train)
print('\n\nAccuracy score for test data is:', acc_test)

# PREDICT FOR SOME HANDWRITTEN PNG IMAGES

# pip install opencv-python
import cv2

def load_image(filename):
    image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    plt.imshow(image)
    plt.show()
    # return the encoding of the image for the ML model
    arr = cv2.resize(image, (28,28)).astype(np.float32)
    arr = arr/255
    arr = arr.reshape(1,784)
    return arr

# make a prediction for a new image
img = load_image('47.png')
predict_value = perceptron.predict(img)
print(predict_value)

