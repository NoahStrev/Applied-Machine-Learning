# NAIVE BAYES CLASSIFICATION
# CLASSIFY A MOVIE REVIEW -- positive or negative
# pip install beautifulsoup4
# cleaning texts
import pandas as pd
import ain210wedid as ain210
##import re
##import nltk
##from nltk.tokenize.toktok import ToktokTokenizer
##from nltk.corpus import stopwords
##from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

import warnings
warnings.filterwarnings('ignore')

dataset = pd.read_csv('IMDBDataset.csv')
print(dataset.describe())
print(dataset['sentiment'].value_counts())

# DO ALL THE AIN210 STUFF
dataset = ain210.ain210(dataset)

# creating bag of words model
cv = CountVectorizer(max_features = 10000)

X = cv.fit_transform(dataset['review']).toarray()
print(X)
print('X type is ', type(X))

#y = dataset.iloc[:,1].values
y = dataset.sentiment

# splitting the data set into training set and test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
		X, y, test_size = 0.2, random_state = 0)

# fitting naive bayes to the training set
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

classifier = GaussianNB();
classifier.fit(X_train, y_train)

# predicting test set results
y_pred = classifier.predict(X_test)

# making the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print('\n\nThe confusion matrix for positive and negative reviews:')
print(cm)
print('\n\nAccuracy score for this model:',accuracy_score(y_test,y_pred))


