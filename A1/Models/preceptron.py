import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report

# opening files
info_1=pd.read_csv("../Dataset/info_1.csv")
info_2=pd.read_csv("../Dataset/info_2.csv")
train_1=pd.read_csv("../Dataset/train_1.csv")
train_2 = pd.read_csv("../Dataset/train_2.csv")
val_1=pd.read_csv("../Dataset/val_1.csv")
val_2=pd.read_csv("../Dataset/val_2.csv")
test_1=pd.read_csv("../Dataset/test_with_label_1.csv")
test_2 = pd.read_csv("../Dataset/test_with_label_2.csv")

# DataSet 1
train_1X=train_1.loc[:, :'1.827']
train_1Y=train_1['1.828']
val_1X=val_1.loc[:, :'1.842']
val_1Y=val_1['1.843']
test_1X=test_1.loc[:, :'1.849']
test_1Y=test_1['4']

perceptron1 = Perceptron(tol=1e-3, random_state=0)
perceptron1.fit(train_1X, train_1Y)
perceptron1_test1=perceptron1.predict(test_1X)

DS1Results = "../Results/DS1Results.csv"
results = np.arange(1,perceptron1_test1.shape[0])
with open(DS1Results, "w", newline="") as file:
    writer = csv.writer(file)    
    writer.writerow(["\nResults for DataSet1:\n"])
    for i in zip(results, perceptron1_test1):
        writer.writerow([i])

# Metrics Report
metrics_data = classification_report(test_1Y, perceptron1_test1, output_dict=True)
metrics_report = pd.DataFrame(metrics_data).transpose()
with open(DS1Results, "a", newline="") as file:
    writer = csv.writer(file)    
    writer.writerow(["\nPerformance Metrics for DataSet1:\n"])
metrics_report.to_csv(DS1Results, mode="a")        

# The confusion matrix
confusion_matrix1_data = confusion_matrix(test_1Y, perceptron1_test1)
confusion_matrix1= pd.DataFrame(confusion_matrix1_data).transpose()
print("Confusion Matrix for Data Set1\n")
print(confusion_matrix1)   
print("\n------\n")       
# ------------------------------------------------------------------------------------------------------------------------------------

# DataSet 2
train_2X=train_2.loc[:, :'1.872']
train_2Y=train_2['9']
val_2X=val_2.loc[:, :'1.881']
val_1Y=val_2['8']
test_2X=test_2.loc[:, :'1.849']
test_2Y=test_2['9']

perceptron2= Perceptron(tol=1e-3, random_state=0)
perceptron2.fit(train_2X, train_2Y)
perceptron2_test2=perceptron2.predict(test_2X)


DS2Results = "../Results/DS2Results.csv"
results2 = np.arange(1,perceptron2_test2.shape[0])
with open(DS2Results, "w", newline="") as file:
    writer = csv.writer(file)    
    writer.writerow(["\nResults of DataSet 2:\n"])
    for i in zip(results2, perceptron2_test2):
        writer.writerow([i])
          
# Metrics Report 2
metrics_data2 = classification_report(test_2Y, perceptron2_test2, output_dict=True)
metrics_report2 = pd.DataFrame(metrics_data2).transpose()
with open(DS2Results, "a", newline="") as file:
    writer = csv.writer(file)    
    writer.writerow(["\n Performance Metrics for DataSet 2: \n"])
metrics_report2.to_csv(DS2Results, mode="a")

# The confusion matrix
confusion_matrix2_data = confusion_matrix(test_2Y, perceptron2_test2)
confusion_matrix2 = pd.DataFrame(confusion_matrix2_data).transpose()
print("Confusion Matrix for Data Set1\n")
print(confusion_matrix2)  
print("\n------\n")
