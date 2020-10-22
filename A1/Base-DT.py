import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
import scoreComputation
import csv

for fileNum in range(2):
    #importing training dataset
    x = pd.read_csv("./Dataset/train_%d.csv" %(fileNum+1), sep=',', header=None)
    featureVals_training1 = (x.values[:,:-1]) #get all columns except last one
    labels_training1 = (x.values[:,-1:].flatten()) #.flatten will map 2D array into 1D array

    #importing validation dataset
    x = pd.read_csv("./Dataset/val_%d.csv" %(fileNum+1), sep=',', header=None)
    featureVals_val1 = (x.values[:,:-1]) #get all columns except last one
    labels_val1 = (x.values[:,-1:].flatten()) #.flatten will map 2D array into 1D array

    #importing test dataset
    x = pd.read_csv("./Dataset/test_with_label_%d.csv" %(fileNum+1), sep=',', header=None)
    featureVals_test1 = (x.values[:,:-1]) #get all columns except last one
    labels_test1 = (x.values[:,-1:].flatten()) #.flatten will map 2D array into 1D array

    #train the model
    clf = DecisionTreeClassifier(criterion='entropy')
    clf.fit(featureVals_training1, labels_training1)

    #predict the validation set
    print('Prediction of validate set:\n ')
    predictionsOfValidationSet = clf.predict(featureVals_val1)
    scoreComputation.computeScores(labels_val1, predictionsOfValidationSet,".\\resultsA\\dummyFile.csv",toCSV=False)

    print("\n-------------------------------------------------------\n")

    #predict the test set
    print('Prediction of test set:\n ')
    predictionsOfTestSet = clf.predict(featureVals_test1)
    #write predicts to csv file
    filePath = ".\\resultsA\\Base-DT-DS%d.csv" %(fileNum+1)
    with open(filePath, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(predictionsOfTestSet)):
            writer.writerow([(i+1),predictionsOfTestSet[i]])

    #print confusion matrix
    scoreComputation.printConfusionMatrix(labels_test1,predictionsOfTestSet,fileNum)

    #write scores into the csv file    
    scoreComputation.computeScores(labels_test1, predictionsOfTestSet,filePath)

    print("Dataset #%d execution is done" %(fileNum+1))

print('Execusion is DONE!')