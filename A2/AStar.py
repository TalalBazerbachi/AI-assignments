import XPuzzle
import numpy as np
import Heuristics
import sys
import time

class Node:
    def __init__(self, data, data_parent, h, g):
        self.child_node = data
        self.parent_node = data_parent
        self.heuristicCost = h
        self.actualCost = 0 if data_parent is None else data_parent.actualCost + g
        self.fCost = self.actualCost + self.heuristicCost

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


init_state = np.array([[1, 0, 3, 6], [5, 2, 7, 4]])

#A* initial phase
#H1: Hamming Distance - GOAL1
puzzleIni = XPuzzle.XPuzzle(init_state)
open_list = [Node(puzzleIni,None,Heuristics.getHammingDist_GOAL(init_state),0)]
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
        print("GOAL!\n")
        print(nodeToGenerateChildren.child_node.initialState)
        break

    #Generate Children    
    child_slideDown = nodeToGenerateChildren.child_node.slideDown()
    if(not (child_slideDown is None)):
        indexClosed = checkInClosedList(child_slideDown)
        index = checkInOpenList(child_slideDown)
        
        if  indexClosed > -1:#it's in closed_list and has > f value
            closed_list.pop(i)

        if indexClosed != -1:#not already in closed_list and has < f value
            if index > -1:
                open_list[index] = Node(XPuzzle.XPuzzle(child_slideDown),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDown),1)
            elif index == -2:
                open_list.append(Node(XPuzzle.XPuzzle(child_slideDown),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDown),1))
  
    child_slideUp = nodeToGenerateChildren.child_node.slideUp()
    if(not (child_slideUp is None)):
        indexClosed = checkInClosedList(child_slideUp)
        index = checkInOpenList(child_slideUp)
        
        if  indexClosed > -1:#it's in closed_list and has > f value
            closed_list.pop(i)

        if indexClosed != -1:#not already in closed_list and has < f value
            if index > -1:
                open_list[index] = Node(XPuzzle.XPuzzle(child_slideUp),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideUp),1)
            elif index == -2:
                open_list.append(Node(XPuzzle.XPuzzle(child_slideUp),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideUp),1))
   
    child_slideRight = nodeToGenerateChildren.child_node.slideRight()
    if(not (child_slideRight is None)):
        indexClosed = checkInClosedList(child_slideRight)
        index = checkInOpenList(child_slideRight)
        
        if  indexClosed > -1:#it's in closed_list and has > f value
            closed_list.pop(i)

        if indexClosed != -1:#not already in closed_list and has < f value
            if index > -1:
                open_list[index] = Node(XPuzzle.XPuzzle(child_slideRight),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideRight),1)
            elif index == -2:
                open_list.append(Node(XPuzzle.XPuzzle(child_slideRight),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideRight),1))
    

    child_slideLeft = nodeToGenerateChildren.child_node.slideLeft()
    if(not (child_slideLeft is None)):
        indexClosed = checkInClosedList(child_slideLeft)
        index = checkInOpenList(child_slideLeft)
        
        if  indexClosed > -1:#it's in closed_list and has > f value
            closed_list.pop(i)

        if indexClosed != -1:#not already in closed_list and has < f value
            if index > -1:
                open_list[index] = Node(XPuzzle.XPuzzle(child_slideLeft),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideLeft),1)
            elif index == -2:
                open_list.append(Node(XPuzzle.XPuzzle(child_slideLeft),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideLeft),1))
  
    child_slideWrappingSlide = nodeToGenerateChildren.child_node.wrappingSlide()
    if(not (child_slideWrappingSlide is None)):
        indexClosed = checkInClosedList(child_slideWrappingSlide)
        index = checkInOpenList(child_slideWrappingSlide)
        
        if  indexClosed > -1:#it's in closed_list and has > f value
            closed_list.pop(i)

        if indexClosed != -1:#not already in closed_list and has < f value
            if index > -1:
                open_list[index] = Node(XPuzzle.XPuzzle(child_slideWrappingSlide),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideWrappingSlide),2)
            elif index == -2:
                open_list.append(Node(XPuzzle.XPuzzle(child_slideWrappingSlide),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideWrappingSlide),2))
 
    child_slideDiagonalSlideInside = nodeToGenerateChildren.child_node.diagonalSlideInside()
    if(not (child_slideDiagonalSlideInside is None)):
        indexClosed = checkInClosedList(child_slideDiagonalSlideInside)
        index = checkInOpenList(child_slideDiagonalSlideInside)
        
        if  indexClosed > -1:#it's in closed_list and has > f value
            closed_list.pop(i)

        if indexClosed != -1:#not already in closed_list and has < f value
            if index > -1:
                open_list[index] = Node(XPuzzle.XPuzzle(child_slideDiagonalSlideInside),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDiagonalSlideInside),3)
            elif index == -2:
                open_list.append(Node(XPuzzle.XPuzzle(child_slideDiagonalSlideInside),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDiagonalSlideInside),3))
    
    child_slideDiagonalSlideOpposed = nodeToGenerateChildren.child_node.diagonalSlideOpposed()
    if(not (child_slideDiagonalSlideOpposed is None)):
        indexClosed = checkInClosedList(child_slideDiagonalSlideOpposed)
        index = checkInOpenList(child_slideDiagonalSlideOpposed)
        
        if  indexClosed > -1:#it's in closed_list and has > f value
            closed_list.pop(i)

        if indexClosed != -1:#not already in closed_list and has < f value
            if index > -1:
                open_list[index] = Node(XPuzzle.XPuzzle(child_slideDiagonalSlideOpposed),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDiagonalSlideOpposed),3)
            elif index == -2:
                open_list.append(Node(XPuzzle.XPuzzle(child_slideDiagonalSlideOpposed),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDiagonalSlideOpposed),3))
   
    #sort element in open_list
    open_list.sort(key=lambda x: x.fCost, reverse=False)
    
