import numpy as np

class XPuzzle:
    initialState = np.array([])
    # GOALSTATE1 = np.array([[1,2,3,4],[5,6,7,0]])
    # GOALSTATE2 = np.array([[1,3,5,7],[2,4,6,0]])
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

    # def wrappingSlide(self):




initStt = np.array([[0,7,1,6],[3,4,2,5]])
x = XPuzzle(initStt)  
print([len(x.initialState)-1,len(x.initialState[0])-1])
print(x.emptyTilePosition)
print(x.isEmptyTileAtCorner())
# print(x.initialState)