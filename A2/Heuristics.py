import numpy as np
def getHammingDist_GOAL(state_list, goal=1):
    hammingDistResult = 0
    
    GOAL = np.array([1,2,3,4,5,6,7,0]) if goal == 1 else np.array([1,3,5,7,2,4,6,0])
    arrToCompare = state_list.flatten()

    for i in range(len(arrToCompare)):
        if(arrToCompare[i]!=0 and arrToCompare[i]!=GOAL[i]):
            hammingDistResult+=1
        i+=1
    return hammingDistResult

def getManhattanDist_GOAL(state_list, goal=1):
    ManhattanDistResult = 0
    
    GOAL = np.array([[1,2,3,4],[5,6,7,0]]) if goal == 1 else np.array([[1,3,5,7],[2,4,6,0]])
    
    for i in range(8):
        if i == 0:#skip i = 0
            continue
        
        #getting the positions in goal and passed matrix
        goalPosition = np.where(GOAL == i)
        positionToCompare = np.where(state_list == i)
        
        #calculate number of moves needed
        x = abs(goalPosition[0][0] - positionToCompare[0][0]) 
        y = abs(goalPosition[1][0] - positionToCompare[1][0])
        z = x+y

        ManhattanDistResult +=z
    return ManhattanDistResult