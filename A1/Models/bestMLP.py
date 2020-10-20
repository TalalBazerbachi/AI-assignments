import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV
import warnings
warnings.filterwarnings("ignore")
# opening files
headers = ["f" + str(i) for i in range(1025)]
headers[1024] = "symbol"
train_1 = pd.read_csv("../Dataset/train_1.csv", sep=",", header=0, names=headers)
test_1 = pd.read_csv("../Dataset/test_with_label_1.csv", sep=",", header=0, names=headers)
train_2 = pd.read_csv("../Dataset/train_2.csv", sep=",", header=0, names=headers)
test_2 = pd.read_csv("../Dataset/test_with_label_2.csv", sep=",", header=0, names=headers)

# DataSet 2
train_1X = train_1.drop("symbol", axis=1)
train_1Y = train_1["symbol"]
test_1X = test_1.drop("symbol", axis=1)
test_1Y = test_1["symbol"]

param_grid=[
    { 'activation': ['logistic','tanh','relu','identity'], 'hidden_layer_sizes':[(30,50),(10,10,10)], 'solver':['adam','sgd']}
]
mlp = MLPClassifier()
clf = GridSearchCV(mlp, param_grid, verbose=2).fit(train_1X, train_1Y)
best_MLP1_test1 = clf.predict(test_1X)

DS1Results ='../results/Best_MLP-DS1.csv'
base_MLP_results1 = np.arange(1, best_MLP1_test1.shape[0])
with open(DS1Results, "w", newline="") as file:
    writer = csv.writer(file)    
    writer.writerow(["\nResults for DataSet1:\n"])
    for i in zip(base_MLP_results1, best_MLP1_test1):
        writer.writerow([i])
               
metrics_data = classification_report(test_1Y, best_MLP1_test1, output_dict=True)
metrics_report = pd.DataFrame(metrics_data).transpose()
with open(DS1Results, "a", newline="") as file:
    writer = csv.writer(file)    
    writer.writerow(["\nPerformance Metrics for DataSet1:\n"])
metrics_report.to_csv(DS1Results, mode="a")

# Confusion Matrix: 
confusion_matrix1_data = confusion_matrix(test_1Y, best_MLP1_test1)
confusion_matrix1 = pd.DataFrame(confusion_matrix1_data).transpose()
print(confusion_matrix1)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# DataSet 2:
train_2X = train_2.drop("symbol", axis=1)
train_2Y = train_2["symbol"]
test_2X = test_2.drop("symbol", axis=1)
test_2Y = test_2["symbol"]

param_grid2=[
    { 'activation': ['logistic','tanh','relu','identity'], 'hidden_layer_sizes':[(0.1,0.1),(10,10,10)], 'solver':['adam','sgd']}
]
mlp = MLPClassifier()
clf = GridSearchCV(mlp, param_grid2, verbose=2).fit(train_2X, train_2Y)
best_MLP1_test2 = clf.predict(test_2X)

DS2Results ='../results/Best_MLP-DS2.csv'
base_MLP_results2 = np.arange(1, best_MLP1_test2.shape[0])
with open(DS2Results, "w", newline="") as file:
    writer = csv.writer(file)    
    writer.writerow(["\nResults for DataSet2:\n"])
    for i in zip(base_MLP_results2, best_MLP1_test2):
        writer.writerow([i])

# Metrics Report
metrics_data2 = classification_report(test_2Y, best_MLP1_test2, output_dict=True)
metrics_report = pd.DataFrame(metrics_data2).transpose()
with open(DS2Results, "a", newline="") as file:
    writer = csv.writer(file)    
    writer.writerow(["\nPerformance Metrics for DataSet2:\n"])
metrics_report.to_csv(DS2Results, mode="a")
 
# Confusion Matrix:    
confusion_matrix2_data = confusion_matrix(test_2Y, best_MLP1_test2)
confusion_matrix2 = pd.DataFrame(confusion_matrix2_data).transpose()
print(confusion_matrix2)

sns.countplot(train_1["symbol"])
plt.savefig("../results/bestMLP1.png")
plt.show()
sns.countplot(train_2["symbol"])
plt.savefig("../results/bestMLP2.png")
plt.show()
        