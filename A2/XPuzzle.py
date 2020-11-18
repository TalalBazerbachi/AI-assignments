import numpy as np

class XPuzzle:
    initialState = np.array([])
    emptyTilePosition = [0,0]

    def __init__(self, initState):
        self.initialState = initState
        tempEmptyTilePosition = np.where(initState == 0)
        self.emptyTilePosition[0] = tempEmptyTilePosition[0][0]
        self.emptyTilePosition[1] = tempEmptyTilePosition[1][0]
    
    ###### Helper methods ######
    def isEmptyTileAtCorner(self):
        #check left-top corner, right-top corner, left-bottom corner and right-bottom corner
        return np.array_equal(self.emptyTilePosition,[0,0]) or np.array_equal(self.emptyTilePosition,[0,len(self.initialState[0])-1]) or np.array_equal(self.emptyTilePosition,[len(self.initialState)-1,0]) or np.array_equal(self.emptyTilePosition,[len(self.initialState)-1,len(self.initialState[0])-1])

    ###### Operators ######
    def slideDown(self):
        #the empty tile is at the bottom of the matrix
        if((len(self.initialState)-1) == self.emptyTilePosition[0]):
            return None

        newState = np.copy(self.initialState)
        newState[self.emptyTilePosition[0]][self.emptyTilePosition[1]], newState[self.emptyTilePosition[0]+1][self.emptyTilePosition[1]] = newState[self.emptyTilePosition[0]+1][self.emptyTilePosition[1]], newState[self.emptyTilePosition[0]][self.emptyTilePosition[1]]

        return newState

    def slideUp(self):
        #the empty tile is at the top of the matrix
        if(0 == self.emptyTilePosition[0]):
            return None
        
        newState = np.copy(self.initialState)
        newState[self.emptyTilePosition[0]][self.emptyTilePosition[1]], newState[self.emptyTilePosition[0]-1][self.emptyTilePosition[1]] = newState[self.emptyTilePosition[0]-1][self.emptyTilePosition[1]], newState[self.emptyTilePosition[0]][self.emptyTilePosition[1]]
        
        return newState
    
    def slideRight(self):
        #the empty tile is at the right edge of the matrix
        if((len(self.initialState[0])-1) == self.emptyTilePosition[1]):
            return None

        newState = np.copy(self.initialState)
        newState[self.emptyTilePosition[0]][self.emptyTilePosition[1]], newState[self.emptyTilePosition[0]][self.emptyTilePosition[1]+1] = newState[self.emptyTilePosition[0]][self.emptyTilePosition[1]+1], newState[self.emptyTilePosition[0]][self.emptyTilePosition[1]]
        
        return newState

    def slideLeft(self):
        #the empty tile is at the left edge of the matrix
        if(0 == self.emptyTilePosition[1]):
            return None
        
        newState = np.copy(self.initialState)
        newState[self.emptyTilePosition[0]][self.emptyTilePosition[1]], newState[self.emptyTilePosition[0]][self.emptyTilePosition[1]-1] = newState[self.emptyTilePosition[0]][self.emptyTilePosition[1]-1], newState[self.emptyTilePosition[0]][self.emptyTilePosition[1]]
        
        return newState

    def wrappingSlide(self):
        #check if the empty tile is at one of the corners
        if(not self.isEmptyTileAtCorner()):
            return None
        
        newState = np.copy(self.initialState)
        if(self.emptyTilePosition[0] == 0): #top row in the matrix
            newState[0][0], newState[0][len(newState[0])-1] = newState[0][len(newState[0])-1], newState[0][0]
        else: #bottom row in the matrix
            newState[len(newState)-1][0], newState[len(newState)-1][len(newState[0])-1] = newState[len(newState)-1][len(newState[0])-1], newState[len(newState)-1][0]
        
        return newState
    
    def diagonalSlideInside(self):
        #check if the empty tile is at one of the corners
        if(not self.isEmptyTileAtCorner()):
            return None

        newState = np.copy(self.initialState)
        if(np.array_equal(self.emptyTilePosition,[0,0])):#top-left corner
            newState[0,0], newState[1,1] = newState[1,1], newState[0,0]
        elif(np.array_equal(self.emptyTilePosition,[0,len(self.initialState[0])-1])):#top-right corner
            newState[0,len(self.initialState[0])-1], newState[1,len(self.initialState[0])-2] = newState[1,len(self.initialState[0])-2], newState[0,len(self.initialState[0])-1]
        elif(np.array_equal(self.emptyTilePosition,[len(self.initialState)-1,0])):#bottom-left corner
            newState[len(self.initialState)-1,0], newState[len(self.initialState)-2,1] = newState[len(self.initialState)-2,1], newState[len(self.initialState)-1,0]
        else:#bottom-right corner
            newState[len(self.initialState)-1,len(self.initialState[0])-1], newState[len(self.initialState)-2,len(self.initialState[0])-2] = newState[len(self.initialState)-2,len(self.initialState[0])-2], newState[len(self.initialState)-1,len(self.initialState[0])-1]

        return newState

    def diagonalSlideOpposed(self):
        #check if the empty tile is at one of the corners
        if(not self.isEmptyTileAtCorner()):
            return None
        
        newState = np.copy(self.initialState)
        if(np.array_equal(self.emptyTilePosition,[0,0]) or np.array_equal(self.emptyTilePosition,[len(self.initialState)-1,len(self.initialState[0])-1])):#top-left and bottom-right corners
            newState[0,0], newState[len(newState)-1,len(newState[0])-1] = newState[len(newState)-1,len(newState[0])-1], newState[0,0]
        else:#top-right and bottom-left corners
            newState[0,len(newState[0])-1], newState[len(newState)-1,0] = newState[len(newState)-1,0], newState[0,len(newState[0])-1]

        return newState

#check if a state is the goal state
def isGOAL1(state):
    GOALSTATE1 = np.array([[1,2,3,4],[5,6,7,0]])
    return np.array_equal(state,GOALSTATE1)

def isGOAL2(state):
    GOALSTATE2 = np.array([[1,3,5,7],[2,4,6,0]])
    return np.array_equal(state,GOALSTATE2)


initStt = np.array([[1,2,3,4],[5,6,7,0]])
print(isGOAL2(initStt))

# x = XPuzzle(initStt)  

# print(x.isEmptyTileAtCorner())
# print(x.diagonalSlideOpposed())
# print(x.initialState)