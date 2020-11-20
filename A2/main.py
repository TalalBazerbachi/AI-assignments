import os
import numpy as np
import glob
import time
import UnfiormCostSearch
import readInputFile


puzzles=readInputFile.getPuzzles("radomInput.txt",(2,4))

i=0
# Analysis array is used  to store information used for the model analysis
analysis=[]

for puzzle in puzzles:
    print("trying to solve puzzle "+ str(i)+"...")
    puzzle=np.array(puzzle)
    uniformcost = UnfiormCostSearch.UniformCost(i, puzzle)
    analysis.append(uniformcost.findGoal())
    i+=1

# the arrays and attributes are used to caclulate the average and total values of anaylsis requirements
solutionPath=[]
solPath=0

searchPath=[]
sPath=0

execution=[]
totalExecution=0

noSol=[]
totalNoSol=0
for a in analysis:
    solutionPath.append(a[0])
    solPath+=a[0]

    searchPath.append(a[1])
    sPath+=a[1]

    execution.append(a[2])
    totalExecution+=a[2]

    noSol.append(a[3])


analysisWRiter = open("ModelAnalysis/ ucs analysis.txt", "w")
analysisWRiter.write("Data For Solution Path:\n\n")
analysisWRiter.write("total solution path:\n")
analysisWRiter.write(str(solPath))
analysisWRiter.write("\n\navrage solution path:\n")
analysisWRiter.write(str(solPath/len(solutionPath)))
analysisWRiter.write("total search path:\n")
analysisWRiter.write(str(sPath))
analysisWRiter.write("\n\navrage search path:\n")
analysisWRiter.write(str(sPath/len(searchPath)))
analysisWRiter.write("\ntotal no solution :\n")
analysisWRiter.write(str(noSol.count(True)))
analysisWRiter.write("\ntotal no solution :\n")
analysisWRiter.write(str(noSol.count(True)/len(noSol)))
analysisWRiter.write("\n\ntotal execution time:\n")
analysisWRiter.write(str(totalExecution))
analysisWRiter.write("\n\naverage execution path:\n")
analysisWRiter.write(str(sPath/len(execution)))