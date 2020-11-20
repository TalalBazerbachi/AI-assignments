import XPuzzle
import numpy as np
import Heuristics
import sys
import time
import readInputFile

class Node:
    def __init__(self, data, data_parent, h, g, moved):
        self.child_node = data
        self.parent_node = data_parent
        self.heuristicCost = h
        self.actualCost = 0 if data_parent is None else data_parent.actualCost + g
        self.fCost = self.actualCost + self.heuristicCost
        self.moved_tile = moved

def checkInClosedList(toCompare):
    for i in range(len(closed_list)):
        if np.array_equal(closed_list[i].child_node.initialState,toCompare):
            if Heuristics.getHammingDist_GOAL(toCompare) < Heuristics.getHammingDist_GOAL(closed_list[i].child_node.initialState):
                return i
            else:
                return -1 #ignore compare
    return -2 #insert as usual

def checkInOpenList(toCompare):
    for i in range(len(open_list)):
        if np.array_equal(open_list[i].child_node.initialState,toCompare):
            if Heuristics.getHammingDist_GOAL(toCompare) < Heuristics.getHammingDist_GOAL(open_list[i].child_node.initialState):
                return i
            else:
                return -1 #ignore toComapre
    return -2 #insert as usual

start_time = time.time()

fileNum = 0
for initialConfig in readInputFile.getPuzzles('puzzles.txt',(2,4)):
    IsASol = False
    init_state = np.array(initialConfig)

    #A* initial phase
    #H1: Hamming Distance - GOAL1
    puzzleIni = XPuzzle.XPuzzle(init_state)
    open_list = [Node(puzzleIni,None,Heuristics.getHammingDist_GOAL(init_state),0, None)]
    closed_list = []

    #end time is set after 60 seconds
    t_end = time.time() + 60
    count = 0 
    while time.time() < t_end:
        if len(open_list) == 0:#check if open_list is empty
            print("No solution")
            break

        #pop the least cost element in the open_list and push it to hte closed_list
        closed_list.append(open_list.pop(0))
        nodeToGenerateChildren = closed_list[len(closed_list)-1]

        #check if it's the goal state
        if XPuzzle.isGOAL1(nodeToGenerateChildren.child_node.initialState):
            IsASol = True
            print("GOAL!\n")
            #print(nodeToGenerateChildren.child_node.initialState)
            break

        #Generate Children    
        child_slideDown, movedTile = nodeToGenerateChildren.child_node.slideDown()
        if(not (child_slideDown is None)):
            indexClosed = checkInClosedList(child_slideDown)
            index = checkInOpenList(child_slideDown)
            
            if  indexClosed > -1:#it's in closed_list and has > f value
                closed_list.pop(i)

            if indexClosed != -1:#not already in closed_list and has < f value
                if index > -1:
                    open_list[index] = Node(XPuzzle.XPuzzle(child_slideDown),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDown),1, movedTile)
                elif index == -2:
                    open_list.append(Node(XPuzzle.XPuzzle(child_slideDown),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDown),1, movedTile))
    
        child_slideUp, movedTile = nodeToGenerateChildren.child_node.slideUp()
        if(not (child_slideUp is None)):
            indexClosed = checkInClosedList(child_slideUp)
            index = checkInOpenList(child_slideUp)
            
            if  indexClosed > -1:#it's in closed_list and has > f value
                closed_list.pop(i)

            if indexClosed != -1:#not already in closed_list and has < f value
                if index > -1:
                    open_list[index] = Node(XPuzzle.XPuzzle(child_slideUp),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideUp),1, movedTile)
                elif index == -2:
                    open_list.append(Node(XPuzzle.XPuzzle(child_slideUp),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideUp),1, movedTile))
    
        child_slideRight, movedTile = nodeToGenerateChildren.child_node.slideRight()
        if(not (child_slideRight is None)):
            indexClosed = checkInClosedList(child_slideRight)
            index = checkInOpenList(child_slideRight)
            
            if  indexClosed > -1:#it's in closed_list and has > f value
                closed_list.pop(i)

            if indexClosed != -1:#not already in closed_list and has < f value
                if index > -1:
                    open_list[index] = Node(XPuzzle.XPuzzle(child_slideRight),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideRight),1, movedTile)
                elif index == -2:
                    open_list.append(Node(XPuzzle.XPuzzle(child_slideRight),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideRight),1, movedTile))
        

        child_slideLeft, movedTile = nodeToGenerateChildren.child_node.slideLeft()
        if(not (child_slideLeft is None)):
            indexClosed = checkInClosedList(child_slideLeft)
            index = checkInOpenList(child_slideLeft)
            
            if  indexClosed > -1:#it's in closed_list and has > f value
                closed_list.pop(i)

            if indexClosed != -1:#not already in closed_list and has < f value
                if index > -1:
                    open_list[index] = Node(XPuzzle.XPuzzle(child_slideLeft),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideLeft),1, movedTile)
                elif index == -2:
                    open_list.append(Node(XPuzzle.XPuzzle(child_slideLeft),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideLeft),1, movedTile))
    
        child_slideWrappingSlide, movedTile = nodeToGenerateChildren.child_node.wrappingSlide()
        if(not (child_slideWrappingSlide is None)):
            indexClosed = checkInClosedList(child_slideWrappingSlide)
            index = checkInOpenList(child_slideWrappingSlide)
            
            if  indexClosed > -1:#it's in closed_list and has > f value
                closed_list.pop(i)

            if indexClosed != -1:#not already in closed_list and has < f value
                if index > -1:
                    open_list[index] = Node(XPuzzle.XPuzzle(child_slideWrappingSlide),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideWrappingSlide),2, movedTile)
                elif index == -2:
                    open_list.append(Node(XPuzzle.XPuzzle(child_slideWrappingSlide),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideWrappingSlide),2, movedTile))
    
        child_slideDiagonalSlideInside, movedTile = nodeToGenerateChildren.child_node.diagonalSlideInside()
        if(not (child_slideDiagonalSlideInside is None)):
            indexClosed = checkInClosedList(child_slideDiagonalSlideInside)
            index = checkInOpenList(child_slideDiagonalSlideInside)
            
            if  indexClosed > -1:#it's in closed_list and has > f value
                closed_list.pop(i)

            if indexClosed != -1:#not already in closed_list and has < f value
                if index > -1:
                    open_list[index] = Node(XPuzzle.XPuzzle(child_slideDiagonalSlideInside),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDiagonalSlideInside),3, movedTile)
                elif index == -2:
                    open_list.append(Node(XPuzzle.XPuzzle(child_slideDiagonalSlideInside),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDiagonalSlideInside),3, movedTile))
        
        child_slideDiagonalSlideOpposed, movedTile = nodeToGenerateChildren.child_node.diagonalSlideOpposed()
        if(not (child_slideDiagonalSlideOpposed is None)):
            indexClosed = checkInClosedList(child_slideDiagonalSlideOpposed)
            index = checkInOpenList(child_slideDiagonalSlideOpposed)
            
            if  indexClosed > -1:#it's in closed_list and has > f value
                closed_list.pop(i)

            if indexClosed != -1:#not already in closed_list and has < f value
                if index > -1:
                    open_list[index] = Node(XPuzzle.XPuzzle(child_slideDiagonalSlideOpposed),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDiagonalSlideOpposed),3, movedTile)
                elif index == -2:
                    open_list.append(Node(XPuzzle.XPuzzle(child_slideDiagonalSlideOpposed),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDiagonalSlideOpposed),3, movedTile))
    
        #sort element in open_list
        open_list.sort(key=lambda x: x.fCost, reverse=False)
    
    #################################################
    ##### outputting solution files #####
    # file_name = "./results/astar-h2/solution/"+str(fileNum)+"_astar-h2_solution.txt"
    # f = open(file_name,'w')
    # if IsASol:
    #     #gathering the solution path
    #     solutionPath = [closed_list[len(closed_list)-1]]
    #     while True:
    #         child = solutionPath[len(solutionPath)-1]
    #         parent = child.parent_node

    #         if parent is None:
    #             break

    #         solutionPath.append(parent)

    #     #outputting the results to the file
    #     count = len(solutionPath)-1
    #     totalCost = 0
    #     while count>=0:
    #         move = solutionPath[count].moved_tile if not solutionPath[count].moved_tile is None else 0
    #         move_cost = solutionPath[count].actualCost
    #         totalCost+=move_cost
    #         puzzleConfig = ' '.join(str(e) for e in solutionPath[count].child_node.initialState.flatten())
    #         strX = str(move)+' '+str(move_cost)+' '+str(puzzleConfig)+'\n'
    #         # print(strX)
    #         f.write(strX)
    #         count-=1
    #         if count<0:#print total cost
    #             f.write(str(totalCost))
    # else:#print no solution
    #     f.write("No solution")

    #################################################
    ##### outputting search files #####
    # file_name = "./results/astar-h2/search/"+str(fileNum)+"_astar-h2_search.txt"
    # f = open(file_name,'w')
    # for node in closed_list:
    #     puzzleConfig = ' '.join(str(e) for e in node.child_node.initialState.flatten())
    #     gCost = node.actualCost
    #     hCost = node.heuristicCost
    #     fCost = node.fCost
    #     outputStr = str(fCost) + ' ' + str(gCost) + ' ' + str(hCost) + ' ' + puzzleConfig
    #     f.write(outputStr+'\n')


    solutionPath = []
    closed_list = []
    open_list = []
    fileNum+=1

end_time = time.time()

print("--- %s seconds ---" %(end_time - start_time))