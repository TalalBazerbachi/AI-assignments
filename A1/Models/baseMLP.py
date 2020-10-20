import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
import warnings
warnings.filterwarnings("ignore")
# opening files
headers = ["f" + str(i) for i in range(1025)]
headers[1024] = "symbol"
train_1 = pd.read_csv("../Dataset/train_1.csv", sep=",", header=0, names=headers)
train_2 = pd.read_csv("../Dataset/train_2.csv", sep=",", header=0, names=headers)
test_1 = pd.read_csv("../Dataset/test_with_label_1.csv", sep=",", header=0, names=headers)
test_2 = pd.read_csv("../Dataset/test_with_label_2.csv", sep=",", header=0, names=headers)

# DataSet 1
train_1X = train_1.drop("symbol", axis=1)
train_1Y = train_1["symbol"]
test_1X = test_1.drop("symbol", axis=1)
test_1Y = test_1["symbol"]

base_MLP1 = MLPClassifier(hidden_layer_sizes=(100,), activation='logistic', solver='sgd').fit(train_1X, train_1Y)
base_MLP1_test1 = base_MLP1.predict(test_1X)

DS1Results ='../results/Base_MLPDS1Results1.csv'
base_MLP_results = np.arange(1, base_MLP1_test1.shape[0])
with open(DS1Results, "w", newline="") as file:
    writer = csv.writer(file)    
    writer.writerow(["\nResults for DataSet1:\n"])
    for i in zip(base_MLP_results, base_MLP1_test1):
        writer.writerow([i])
        
# Metrics Report
metrics_data = classification_report(test_1Y, base_MLP1_test1, output_dict=True)
metrics_report = pd.DataFrame(metrics_data).transpose()
with open(DS1Results, "a", newline="") as file:
    writer = csv.writer(file)    
    writer.writerow(["\nPerformance Metrics for DataSet1:\n"])
metrics_report.to_csv(DS1Results, mode="a")

# The confusion matrix
confusion_matrix1_data = confusion_matrix(test_1Y, base_MLP1_test1)
confusion_matrix1 = pd.DataFrame(confusion_matrix1_data).transpose()
print("Confusion Matrix for Data Set1\n")
print(confusion_matrix1)   
print("\n------\n")  
        


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# DataSet 2:
train_2X = train_2.drop("symbol", axis=1)
train_2Y = train_2["symbol"]
test_2X = test_2.drop("symbol", axis=1)
test_2Y = test_2["symbol"]

base_MLP2 = MLPClassifier(hidden_layer_sizes=(100,), activation='logistic', solver='sgd').fit(train_2X, train_2Y)
base_MLP1_test2 = base_MLP2.predict(test_2X)

DS2Results ='../results/Base_MLPDS2Results2.csv'
base_MLP_results2 = np.arange(1, base_MLP1_test2.shape[0])
with open(DS2Results, "w", newline="") as file:
    writer = csv.writer(file)    
    writer.writerow(["\nResults of DataSet 2:\n"])
    for i in zip(base_MLP_results2, base_MLP1_test2):
        writer.writerow([i])

 # Metrics Report
metrics_data2 = classification_report(test_2Y, base_MLP1_test2, output_dict=True)
metrics_report = pd.DataFrame(metrics_data2).transpose()
with open(DS2Results, "a", newline="") as file:
    writer = csv.writer(file)    
    writer.writerow(["\n Performance Metrics for DataSet 2: \n"])
metrics_report.to_csv(DS2Results, mode="a")


# The confusion matrix
confusion_matrix2_data = confusion_matrix(test_2Y, base_MLP1_test2)
confusion_matrix2 = pd.DataFrame(confusion_matrix2_data).transpose()
print("Confusion Matrix for Data Set1\n")
print(confusion_matrix2)   
print("\n------\n")     

sns.countplot(train_1["symbol"])
plt.savefig("../results/baseMLP1.png")
plt.show()        
sns.countplot(train_2["symbol"])
plt.savefig("../results/baseMLP2.png")
plt.show()