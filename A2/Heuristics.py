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