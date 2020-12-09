import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
import nltk 
import time
from nltk.corpus import stopwords
#to remove HTML tags from the doc
from bs4 import BeautifulSoup 
#removing numbers,punctuations,i.e regular expressions from the doc
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split,StratifiedKFold
from sklearn import metrics
from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
import nltk
import os

trainData = pd.read_csv("covid_training.tsv", header=0, delimiter="\t", quoting=3)

testData = pd.read_csv("covid_test_public.tsv",header=0, delimiter="\t", quoting=3)

def reviewToWords(raw_review):
    #creating an array , resolving whitespaces
    words = raw_review.lower().split()
    meaningfulWords = [w for w in words]    
    #return a string with only the words that are important
    return(" ".join(meaningfulWords))

# finding the number of reviews
trainSize = trainData.text.size
testSize = testData.text.size

# storing all cleaned reviews in one place
trainRev = []
for i in range(trainSize):
    trainRev.append(reviewToWords(trainData.text[i]))
testRev = []
for i in range(testSize):
    testRev.append(reviewToWords(testData.text[i]))


# creating a function, vectorizer to convert the words into vectors
vectorizer = CountVectorizer(analyzer="word",
                            preprocessor=None,
                            stop_words=None,  # stop_words = none
                            max_features=5000)

# creating a function, vectorizer to convert the words into vectors
vectorizer2 = CountVectorizer(analyzer="word",
                            preprocessor=None,
                            stop_words=None,  # stop_words = none
                            max_features=5000)                            

# converting reviews from text into features
trainDataFeatures = vectorizer.fit_transform(trainRev)

testDataFeatures = vectorizer2.fit_transform(testRev)
#change the classifier into array
xTrain = trainDataFeatures.toarray()
xTest = testDataFeatures.toarray()

yTrain = trainData.q1_label 
yTest = testData.q1_label


# splitting the training data into test and train
X_train, X_test, y_train, y_test = train_test_split(xTrain, yTrain,test_size=0.12,random_state=123)

# Applying MultinomialNaiveBayes for classification 
model = MultinomialNB(alpha = 0.01)
classifier = model.fit(X_train,y_train)
trained = classifier.predict(X_test)
cm = confusion_matrix(trained,y_test)
accuracy = cm.trace()/cm.sum()
print(accuracy)

metrics_data2 = classification_report(y_test, trained, output_dict=True)
metrics_report2 = pd.DataFrame(metrics_data2).transpose()
print(metrics_report2)