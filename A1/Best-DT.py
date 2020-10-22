import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import PredefinedSplit
import numpy as np
import csv
import scoreComputation

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

    #concatenating both training and validation sets
    featureVals_trainingAndVal = np.concatenate([featureVals_training1,featureVals_val1])
    labels_trainingAndVal = np.concatenate([labels_training1,labels_val1])

    #Create iterator object that specifies which portion of dataset is for validation
    #and which for training. Here's an article explaining this notion:
    #https://www.wellformedness.com/blog/using-a-fixed-training-development-test-split-in-sklearn/
    test_fold = np.concatenate([
        np.full(featureVals_training1.shape[0],-1, dtype=np.int8), #training instances
        np.zeros(featureVals_val1.shape[0], dtype=np.int8) #validation instances
    ])
    cvIterator = PredefinedSplit(test_fold)
    print("cvIterator iterator has been produced %s" %(cvIterator))

    #trying hyperparameters
    print("Trying different hyperparameters...")
    hyperparameters = {'criterion':['gini','entropy'], 'max_depth':[10,None],
    'min_samples_split':[4,5,6,7,8,9,10,11], 'min_impurity_decrease':[0.2,0.3,0.5,1],
    'class_weight':['balanced',None]}

    #Why refit = False? https://stackoverflow.com/questions/46815252/using-scikit-learn-gridsearchcv-for-cross-validation-with-predefinedsplit-susp
    gridSearch = GridSearchCV(estimator=DecisionTreeClassifier(), param_grid=hyperparameters, cv=cvIterator, n_jobs=-1, refit=False)
    gridSearch.fit(featureVals_trainingAndVal,labels_trainingAndVal)

    print("Best params are: %s" %(gridSearch.best_params_))

    #Initializing a classifier with the best_params
    optimalCLF = DecisionTreeClassifier(**gridSearch.best_params_)
    optimalCLF.fit(featureVals_training1, labels_training1)

    #predict test data
    predictedClass = optimalCLF.predict(featureVals_test1)

    #write predicts to csv file
    filePath = ".\\resultsA\\Best-DT-DS%d.csv" %(fileNum+1)
    with open(filePath, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(predictedClass)):
            writer.writerow([(i+1),predictedClass[i]])

    #print confusion matrix
    scoreComputation.printConfusionMatrix(labels_test1,predictedClass,fileNum)

    #write scores into the csv file
    scoreComputation.computeScores(labels_test1, predictedClass, filePath, toCSV=False)

    print("Dataset #%d execution is done" %(fileNum+1))

print('Execusion is DONE!')