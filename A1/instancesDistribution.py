import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

def plotInstancesDistributionSet1():
    #importing training dataset
    x = pd.read_csv("./Dataset/test_with_label_1.csv", sep=',', header=None)
    #featureVals_training1 = (x.values[:,:-1]) #get all columns except last one
    labels = (x.values[:,-1:].flatten()) #.flatten will map 2D array into 1D array

    dic = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0}
    for i in range(len(labels)):
        dic[labels[i]]+=1

    #Generate the x-axis labels
    listOfAlpha = []
    listOfAlpha[:0]="abcdefghijklmnopqrstuvwxyz".upper()

    #ploting the bar diagram
    x = np.arange(26)
    plt.bar(x, height=dic.values())
    plt.xticks(x, listOfAlpha)
    plt.show()

def plotInstancesDistributionSet2():
    #importing training dataset
    x = pd.read_csv("./Dataset/test_with_label_2.csv", sep=',', header=None)
    #featureVals_training1 = (x.values[:,:-1]) #get all columns except last one
    labels = (x.values[:,-1:].flatten()) #.flatten will map 2D array into 1D array

    dic = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for i in range(len(labels)):
        dic[labels[i]]+=1

    #Generate the x-axis labels
    listOfSymbols = ['pi','alpha','beta','sigma','gamma','delta','lambda','omega','mu','xi']

    #ploting the bar diagram
    x = np.arange(10)
    plt.bar(x, height=dic.values())
    plt.xticks(x, listOfSymbols)
    plt.show()

plotInstancesDistributionSet1()
plotInstancesDistributionSet2()