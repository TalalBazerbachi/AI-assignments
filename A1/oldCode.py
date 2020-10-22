'''
This code is the old code for computing each class percision, recall and f1-measurement.
All done without using external libraries
Just for reference...
'''

#print percision of classes
percisions = []
print("Writing percision for each class...")
# with open(filePath, 'a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow("P")

#     percisionVal=0.0
#     for outerIndex in range(len(confusionMatrix)):
#         diagonalValue = confusionMatrix[outerIndex][outerIndex]
#         rowSum = np.sum(confusionMatrix[outerIndex])
#         percisionVal=diagonalValue/rowSum
#         writer.writerow([(outerIndex+1),percisionVal])
#         percisions.append(percisionVal)
#         percisionVal=0.0
print("Done with writing percision for each classe")

#printing recall of classes
recalls = []
print("Writing recall for each class...")
# with open(filePath, 'a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow("R")

#     colSum = 0.0
#     recall=0
#     for innerIndex in range(len(confusionMatrix[0])):
#         for outerIndex in range(len(confusionMatrix)):
#             colSum += confusionMatrix[outerIndex][innerIndex]

#         if colSum==0:
#             recall = 0
#         else:
#             recall = confusionMatrix[innerIndex][innerIndex]/colSum

#         writer.writerow([(innerIndex+1),recall]) #writing to csv file
#         recalls.append(recall)
#         colSum = 0.0
print("Done with writing recall for each classe")

#printing f1 measure for each classe
print("Writing f1-measure for each class...")
# percisionPerClass,recallPerClass,f1MeasurePerClass,ignore=precision_recall_fscore_support(labels_test1,predictedClass,average=None)
# print(percisionPerClass)
# print(recallPerClass)
# print(f1MeasurePerClass)

# with open(filePath, 'a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow("F")

#     for x in range(len(percisions)):
#         if (percisions[x]+recalls[x]) == 0:
#             f1 = 0.0
#         else:
#             f1 = (2*percisions[x]*recalls[x])/(percisions[x]+recalls[x])
#         writer.writerow([(x+1),f1])
print("Done with writing f1-measure for each classe")

#Model measures
#macro/weighted f1-measure and accuracy
print("Writing macro f1-measure for the model...")
# with open(filePath, 'a', newline='') as file:
#     writer = csv.writer(file)

#     #macro f1 measurement
#     macroF1 = f1_score(labels_test1,predictedClass, average="macro")
#     writer.writerow(["Macro-F1",macroF1])

#     #weighted f1 measurement
#     weightedF1 = f1_score(labels_test1,predictedClass, average="weighted")
#     writer.writerow(["Weighted-F1",macroF1])

#     #accuracy
#     modelAccuracy = accuracy_score(labels_test1,predictedClass)
#     writer.writerow(["Accuracy",modelAccuracy])