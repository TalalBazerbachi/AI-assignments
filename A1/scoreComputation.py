from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import numpy as np
import csv
from sklearn.metrics import confusion_matrix

def computeScores(labels_test1,predictedClass,filePath, toCSV=True):
    print("Writing precision, recall, and f1-measure for each class...")
   
    #Compute precision, recall, and f1-measure for each class
    percisionPerClass,recallPerClass,f1MeasurePerClass,ignore=precision_recall_fscore_support(labels_test1,predictedClass,average=None)

    perClassMeasures = [percisionPerClass,recallPerClass,f1MeasurePerClass]
    namesToPrint = ['Recall',"Percision",'F1-Measure']

    with open(filePath, 'a', newline='') as file:
        writer = csv.writer(file)

        for numOfMeasure in range(len(perClassMeasures)):
            if(toCSV):
                writer.writerow([namesToPrint[numOfMeasure]])
            else:
                print([namesToPrint[numOfMeasure]])
            for index in range(len(perClassMeasures[numOfMeasure])):
                if(toCSV):
                    writer.writerow([(index),perClassMeasures[numOfMeasure][index]])
                else:
                    print([(index),perClassMeasures[numOfMeasure][index]])
        print("Done writing precision, recall, and f1-measure for each class")

    #Model measures
    #macro/weighted f1-measure and accuracy
    print("Writing macro/weighted f1-measure and accuracy for the model...")
    with open(filePath, 'a', newline='') as file:
        writer = csv.writer(file)

        #macro f1 measurement
        macroF1 = f1_score(labels_test1,predictedClass, average="macro")
        if(toCSV):
            writer.writerow(["Macro-F1",macroF1])
        else:
            print(["Macro-F1",macroF1])

        #weighted f1 measurement
        weightedF1 = f1_score(labels_test1,predictedClass, average="weighted")
        if(toCSV):
            writer.writerow(["Weighted-F1",weightedF1])
        else:
            print(["Weighted-F1",weightedF1])

        #accuracy
        modelAccuracy = accuracy_score(labels_test1,predictedClass)
        if(toCSV):
            writer.writerow(["Accuracy",modelAccuracy]) 
        else:
            print(["Accuracy",modelAccuracy])
    print("Done writing macro/weighted f1-measure and accuracy for the model")

def printConfusionMatrix(labels_test1,predictedClass, fileNum):
    confusionMatrix = confusion_matrix(labels_test1,predictedClass)
    print("Confusion matrix for test set #%d:" %(fileNum+1))
    print(confusionMatrix)