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




initStt = np.array([[7,2,0,3],[6,4,1,5]])
x = XPuzzle(initStt)    
print(x.slideUp())
# print(x.initialState)