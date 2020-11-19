import time
import numpy as np

# from output_writer import OutputWriter
import UCNode
# from algorithms.helper import Helper
# from algorithms.helper import get_state_as_string
import XPuzzle


class UniformCost:
    """
    This class is responsible for executing the "uniform cost" search algorithm on the provided puzzle instance.
    """

    def __init__(self, currentPuzzleNum, puzzle, puzzleRows):
        self.puzzle = puzzle
        self.timeout = 60
        # self.helper = Helper(len(puzzle), puzzleRows)
        self.xpuzzle = XPuzzle.XPuzzle(puzzle)
        print("am here!!!")
        # self.output_writer = OutputWriter(currentPuzzleNum, "ucs")
        self.openList = [UCNode.UCNode(puzzle, None, 0, None)]
        self.closedList = []

    def solve(self):
        initialTime = time.time()
        currentTime = 0
        timedout = False
        goalFound = False
        goalPuzzle = None 
        openListNotEmpty = len(self.openList) > 0
        modelTimedOut = currentTime > self.timeout
        
        while  openListNotEmpty and not modelTimedOut:
            if currentTime>self.timeout:
                "model is taking too long to build"
                break
            currentPuzzle = self.openList.pop(0)
            self.closedList.append(currentPuzzle)

            if self.xpuzzle.isGOAL1(currentPuzzle.state) or self.xpuzzle.isGOAL2(currentPuzzle): 
                goalFound = True
                goalPuzzle = currentPuzzle
                break
            
            succesors = self.getSucessors(self.xpuzzle, currentPuzzle.state, currentPuzzle)
            self.pushPossibleSucessors(currentPuzzle, succesors)
            self.openList.sort(key=lambda node: node.cost)
            currentTime = time.time() - initialTime

        if goalFound:
            print("goal is found! \n")

        else:
            if currentTime >= self.timeout:

                print("model timed out, goal state was not found")
            else:
                print("goal state was not found")

  
        print("Uniform Cost Search is done, it took"+currentTime)


    def getSucessors(self, xpuzzle, currentPuzzleState, currentPuzzle):
        movesList = []

        # Generate Possible sucessors of the current state based on possible moves allowed
        print("parent node of the new sucessors: ")
        ts = currentPuzzleState.tostring()
        print(np.fromstring(ts, dtype=int))
        moveUpCopy = currentPuzzleState.copy()
        upPuzzle=XPuzzle.XPuzzle(moveUpCopy)
        if upPuzzle.slideUp()is not None:
            movesList.append((upPuzzle.slideUp(),currentPuzzleState, currentPuzzle.cost+1, 'move_up'))
            ts = upPuzzle.slideUp().tostring()
            print(np.fromstring(ts, dtype=int))
            print("\n")

        moveDownCopy = currentPuzzleState.copy()
        downPuzzle=XPuzzle.XPuzzle(moveDownCopy)
        if downPuzzle.slideDown()is not None:
            movesList.append((downPuzzle.slideDown(),currentPuzzleState, currentPuzzle.cost+1, 'moveDown'))
            ts = downPuzzle.slideDown().tostring()
            print(np.fromstring(ts, dtype=int))
            print("\n")

        moveLeftCopy = currentPuzzleState.copy()
        leftPuzzle=XPuzzle.XPuzzle(moveLeftCopy)
        if leftPuzzle.slideLeft()is not None:
            movesList.append((leftPuzzle.slideLeft(),currentPuzzleState, currentPuzzle.cost+1, 'moveLeft'))
            ts = leftPuzzle.slideLeft().tostring()
            print(np.fromstring(ts, dtype=int))
            print("\n")

        moveRightCopy = currentPuzzleState.copy()
        rightPuzzle=XPuzzle.XPuzzle(moveRightCopy)
        if rightPuzzle.slideRight()is not None:
            movesList.append((rightPuzzle.slideRight(),currentPuzzleState, currentPuzzle.cost+1, 'move_Rght'))
            ts = rightPuzzle.slideRight().tostring()
            print(np.fromstring(ts, dtype=int))
            print("\n")

        wrappingSlideCopyCopy = currentPuzzleState.copy()
        wrapPuzzle=XPuzzle.XPuzzle(wrappingSlideCopyCopy)
        if wrapPuzzle.wrappingSlide()is not None:
            movesList.append((xpuzzle.wrappingSlide(),currentPuzzleState, currentPuzzle.cost+1, 'wrappingSlide'))
            ts = wrapPuzzle.wrappingSlide().tostring()
            print(np.fromstring(ts, dtype=int))
            print("\n")
            
        
        diagonalSlideCopy = currentPuzzleState.copy()
        diagonalPuzzle=XPuzzle.XPuzzle(diagonalSlideCopy)
        if diagonalPuzzle.diagonalSlideInside()is not None:
            movesList.append((diagonalPuzzle.diagonalSlideInside(),currentPuzzleState, currentPuzzle.cost+1, 'diagonalSlideInside'))
            ts = diagonalPuzzle.diagonalSlideInside().tostring()
            print(np.fromstring(ts, dtype=int))
            print("\n")
        return movesList


    def pushPossibleSucessors(self, node, sucessors):

        for s in sucessors:
            sNode = UCNode.UCNode(s[0], s[1], s[2],(s[0] - s[1]))

            inClosedList = False
            for closedNosed in self.closedList:
                if (np.array(sNode.state) == np.array(closedNosed.state)).all():
                    inClosedList = True
                    break
 
            inOpenList = False
            if not inClosedList:
                for i in range(len(self.openList)):
                    closedNosed = self.openList[i]
                    if (np.array(sNode.state) == np.array(closedNosed.state)).all():
                        if closedNosed.cost < sNode.cost:
                            inOpenList = True
                        else:
                            self.openList[i] = sNode
                        break

            if not inClosedList and not inOpenList:
                self.openList.append(sNode)
