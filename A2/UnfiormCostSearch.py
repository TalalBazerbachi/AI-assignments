import time
import numpy as np
import UCNode
import XPuzzle

# The class uniform cost is used to solve puzzles using Uniform cost model
class UniformCost:
    def __init__(self, currentPuzzleNum, puzzle):
        # puzzle is the intial puzzle passed
        self.puzzle = puzzle
        
        # the attribute pNumber is used to write the names of the output files
        self.pNumber = currentPuzzleNum

        # open and closed list are used during findIng the goal puzzle
        self.openList = [UCNode.UCNode(puzzle, None, 0,0)]
        self.closedList = []

    # The function findGoal is used to find the goal state if it exists
    def findGoal(self):
        initialTime = time.time()
        currentTime = 0
        goalFound = False
        goalPuzzle = None 


        while  (len(self.openList) > 0) and not (currentTime > 60):

            currentPuzzle = self.openList.pop(0)
            self.closedList.append(currentPuzzle)

            # first we check if the current state is the goal state
            if XPuzzle.isGOAL1(np.array(currentPuzzle.state)) or XPuzzle.isGOAL2(np.array(currentPuzzle)): 
                goalFound = True
                self.goalPuzzle = currentPuzzle
                break
            
            # if it's not the goal state we generate it's sucessors and sort them based on the cost
            succesors = self.getSucessors(currentPuzzle)
            self.openList.sort(key=lambda node: node.cost)

            currentTime = time.time() - initialTime

        # At this point the function either found the goal or it didn't 
        # (either because the goal is unreachable or it took more than 60 seconds)
        f = open("50 puzzles output files/"+str(self.pNumber)+" ucs solution.txt", "w")
        searchWriter = open("50 puzzles output files/"+str(self.pNumber)+" ucs search.txt", "w")        
        #to write the solution first I need to generate it by adding all the accepted state to a list 
        # every time I reach a new state I change the 'currentState attribute to be the parent of the previuos current state
        # until we reach teh initial state were the parent is None
        solution=[]
        if goalFound:
            i=0
            currentPuzzle=self.goalPuzzle
            while True:
                if currentPuzzle.parent is not None:
                    solution.append(currentPuzzle)
                    currentPuzzle=currentPuzzle.parent
                else :
                    solution.append(currentPuzzle)
                    break
                i=i+1
            
            # In this loop I am adding the solution path to it's uotput file
            count = len(solution)-1
            while count>=0:
                toWrite=str(solution[count].tileMoved)+" "+ str(solution[count].cost)+" "+str(solution[count].state)+"\n"
                toWrite = toWrite.replace("[", "")
                toWrite = toWrite.replace("]", "")
                toWrite = toWrite.replace("\n", "")
                f.write(toWrite)
                f.write("\n")
                count-=1
            
            # In this section I am adding the searched state (states in the closed list)
            count =0
            while count <= len(self.closedList)-1:
                toWrite=str(self.closedList[count].cost)+" "+ str(self.closedList[count].cost)+" "+str(0)+" "+str(self.closedList[count].state)+"\n"
                toWrite = toWrite.replace("[", "")
                toWrite = toWrite.replace("]", "")
                toWrite = toWrite.replace("\n", "")                
                searchWriter.write(toWrite)
                searchWriter.write("\n")
                count+=1

        else:
            f.write("no solution\n")
            searchWriter.write("no solution\n")

        b =currentTime>60
        return len(solution), len(self.closedList), currentTime, b

    # AddSuccessor is used to add a new node to the open list if it's not their and it's not in the closed list 
    # if the current state's cost is less than the same state in the open list we swap them
    def AddSuccessor(self,sNode):
        newNode = UCNode.UCNode(sNode[0], sNode[1], sNode[2], sNode[3])
        inClosedList = self.checkInClosedList(newNode)
        inOpenList = self.checkInOpenList(newNode)
        if not inClosedList and not inOpenList:
            self.openList.append(newNode)  

    # This functio is used to generate possible successors based on the functions of XPuzzle
    def getSucessors(self, currentPuzzle):
        puzzleO=XPuzzle.XPuzzle(currentPuzzle.state)

        if puzzleO.slideDown()[0]is not None:
            sNode=puzzleO.slideDown()[0],currentPuzzle, currentPuzzle.cost+1,puzzleO.slideDown()[1]
            self.AddSuccessor(sNode)

        if puzzleO.slideUp()[0]is not None:
            sNode = puzzleO.slideUp()[0],currentPuzzle, currentPuzzle.cost+1,puzzleO.slideUp()[1]
            self.AddSuccessor(sNode)

        if puzzleO.slideRight()[0]is not None:
            sNode= puzzleO.slideRight()[0],currentPuzzle, currentPuzzle.cost+1,puzzleO.slideRight()[1]
            self.AddSuccessor(sNode)

        if puzzleO.slideLeft()[0]is not None:
            sNode = puzzleO.slideLeft()[0],currentPuzzle, currentPuzzle.cost+1,puzzleO.slideLeft()[1]
            self.AddSuccessor(sNode)

        if puzzleO.wrappingSlide()[0]is not None:
            sNode = puzzleO.wrappingSlide()[0],currentPuzzle, currentPuzzle.cost+2,puzzleO.wrappingSlide()[1]
            self.AddSuccessor(sNode)
 
        if puzzleO.diagonalSlideInside()[0]is not None:
            sNode = puzzleO.diagonalSlideInside()[0],currentPuzzle, currentPuzzle.cost+3,puzzleO.diagonalSlideInside()[1]
            self.AddSuccessor(sNode)

        if puzzleO.diagonalSlideOpposed()[0]is not None:
            sNode = puzzleO.diagonalSlideOpposed()[0],currentPuzzle, currentPuzzle.cost+3,puzzleO.diagonalSlideOpposed()[1]
            self.AddSuccessor(sNode)

    # This function is used to check if a state is in the closed list
    def checkInClosedList(self,toCompare):
        for i in range(len(self.closedList)):
            if np.array_equal(self.closedList[i].state,toCompare.state):
                return True
        return False

    # This function is used to check if a state is in the open list
    # If a state is in the open list and the incoming state has a lower cost the old version is romved
    # and the incoming state is added to the open list
    def checkInOpenList(self,toCompare):
        for i in range(len(self.openList)):
            if np.array_equal(self.openList[i].state,toCompare.state):
                if (toCompare.cost < self.openList[i].cost):
                    openList[i]=toCompare
                return True
            else:
                return False
        
