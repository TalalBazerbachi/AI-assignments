import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.naive_bayes import MultinomialNB


def textToWords(text):
    #convert text to array to remove white spaces
    words = text.lower().split()
    spacedRemoved = [w for w in words]    
    #return a string with only the words that are important
    return(" ".join(spacedRemoved))
    
def train(trainData, testData):
    # finding the number of reviews
    trainSize = trainData.text.size
    testSize = testData.text.size

    # storing text in arrays
    trainTweets = []
    for i in range(trainSize):
        trainTweets.append(textToWords(trainData.text[i]))
    testTweets = []
    for i in range(testSize):
        testTweets.append(textToWords(testData.text[i]))

    # take only words that appeared more than once
    oneSentence= ""
    for w in trainTweets:
        oneSentence = oneSentence + w
    seq = oneSentence.split()
    for word in seq:
        if oneSentence.count(word) == 1:
            for i in range(2,401):
                sentence = trainTweets[i]
                if word in sentence:
                    temp = sentence.replace(word, '')
                    trainTweets[i] = temp
        else:
            pass

    # CountVectorizer used to convert words to vectors:
    vectorizer = CountVectorizer()
    vectorizer2 = CountVectorizer()                            

    # convert text to features:
    trainDataFeatures = vectorizer.fit_transform(trainTweets)
    testDataFeatures = vectorizer2.fit_transform(testTweets)

    #convert features objects to arrays
    xTrain = trainDataFeatures.toarray()
    xTest = testDataFeatures.toarray()

    # get label for train and test dataset
    yTrain = trainData.q1_label 
    yTest = testData.q1_label
    return xTrain, yTrain

trainData = pd.read_csv("covid_training.tsv", header=0, delimiter="\t", quoting=3)
testData = pd.read_csv("covid_test_public.tsv",header=0, delimiter="\t", quoting=3)

trainText= train(trainData, testData)[0]
trainLabel= train(trainData, testData)[1]
X_train, X_test, y_train, y_test = train_test_split(trainText, trainLabel,test_size=0.12,random_state=123)

model = MultinomialNB(alpha = 0.01)
bowMNB = model.fit(X_train,y_train)
trained = bowMNB.predict(X_test)
cm = confusion_matrix(trained,y_test)
accuracy = cm.trace()/cm.sum()
print(accuracy)

metrics_data2 = classification_report(y_test, trained, output_dict=True)
metrics_report2 = pd.DataFrame(metrics_data2).transpose()
print(metrics_report2)