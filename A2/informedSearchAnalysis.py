fResults = open("./results/analysis/astar-h1.txt",'w')
#1. average & total length of the solution and search paths
fResults.write("1. average & total length of the solution and search paths")
fileTpyes = ['solution','search']
for fileType in fileTpyes:
    totalLengthOfPaths = 0
    for i in range(50):
        search = '_search'
        solutionF = ' solution'
        temp = search if fileType == 'search' else solutionF
        fPath = './results/astar-h1/'+fileType+'/'+str(i)+'_astar-h1'+temp+'.txt'
        f = open(fPath,'r')
        
        fileContent = f.readlines()
        totalLengthOfPaths+=len(fileContent)-1 if fileType=='solution' else len(fileContent)
        f.close()

    # calculate the average length of paths
    averageLengthOfPaths = totalLengthOfPaths/50

    fResults.write("\nTotal length of %s path = %d" %(fileType,totalLengthOfPaths))
    fResults.write("\nAverage length of %s path = %.2f" %(fileType,averageLengthOfPaths))

#2. average & total number of no solution
fResults.write("\n2. average & total number of no solution")
numOfNoSol = 0
for i in range(50):
    fileType = 'solution'
    fPath = './results/astar-h1/'+fileType+'/'+str(i)+'_astar-h1 '+fileType+'.txt'
    f = open(fPath,'r')

    line = f.readline()
    if line == 'No solution':
        numOfNoSol+=1

# calculate average number of no solution
averageNumOfNoSolution = numOfNoSol/50

fResults.write("\nTotal number of 'No Solution' = %d" %numOfNoSol)
fResults.write("\nAverage number of 'No Solution' = %.2d" %averageNumOfNoSolution)

# 3. average & total cost and execution time
fResults.write("\n3. average & total cost and execution time")
###Has been computed in the respective algorithms files###

#4. optimality of the solution path
fResults.write("\n4. optimality of the solution path")
totalCost = 0
for i in range(50):
    fileType = 'solution'
    fPath = './results/astar-h1/'+fileType+'/'+str(i)+'_astar-h1 '+fileType+'.txt'
    f = open(fPath,'r')

    fileContent = f.readlines()
    cost = fileContent[len(fileContent)-1]
    if len(fileContent) >2:
        totalCost +=int(cost)

#calculate average cost
averageCost = totalCost/50

fResults.write("\nTotal solution cost = %d" %totalCost)
fResults.write("\nAverage solution cost = %.2f" %averageCost)

fResults.close()