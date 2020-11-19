import XPuzzle
import numpy as np
import Heuristics
import sys
import time

class Node:
    def __init__(self, data, data_parent, cost, movedTile):
        self.child_node = data
        self.parent_node = data_parent
        self.heuristicCost = cost
        self.moved_tile = movedTile

def checkInClosedList(toCompare):
    for i in range(len(closed_list)):
        if np.array_equal(closed_list[i].child_node.initialState,toCompare):
            return True
    return False

def checkInOpenList(toCompare):
    for i in range(len(open_list)):
        if np.array_equal(open_list[i].child_node.initialState,toCompare):
            if Heuristics.getHammingDist_GOAL(toCompare) < Heuristics.getHammingDist_GOAL(open_list[i].child_node.initialState):
                return i
            else:
                return -1 #ignore toComapre
    return -2 #insert as usual

init_state = np.array([[1, 0, 3, 6],[5, 2, 7, 4]])

#GBS initial phase
#H1: Hamming Distance - GOAL1
puzzleIni = XPuzzle.XPuzzle(init_state)
open_list = [Node(puzzleIni,None,Heuristics.getHammingDist_GOAL(init_state),None)]
closed_list = []

#end time is set after 60 seconds
t_end = time.time() + 60
count = 0
while time.time() < t_end:
    #pop the least cost element in the open_list and push it to hte closed_list
    closed_list.append(open_list.pop(0))
    nodeToGenerateChildren = closed_list[len(closed_list)-1]

    #check if it's the goal state
    if XPuzzle.isGOAL1(nodeToGenerateChildren.child_node.initialState):
        print("GOAL!\n")
        print(nodeToGenerateChildren.child_node.initialState)
        break

    #Generate Children    
    child_slideDown, movedTile = nodeToGenerateChildren.child_node.slideDown()
    if(not (child_slideDown is None) and not checkInClosedList(child_slideDown)):
        index = checkInOpenList(child_slideDown)
        if index > -1:
            open_list[index] = Node(XPuzzle.XPuzzle(child_slideDown),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDown),movedTile)
        elif index == -2:
            open_list.append(Node(XPuzzle.XPuzzle(child_slideDown),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDown),movedTile))
    
    child_slideUp, movedTile = nodeToGenerateChildren.child_node.slideUp()
    if(not (child_slideUp is None) and not checkInClosedList(child_slideUp)):
        index = checkInOpenList(child_slideUp)
        if index > -1:
            open_list[index] = Node(XPuzzle.XPuzzle(child_slideUp),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideUp), movedTile)
        elif index == -2:
            open_list.append(Node(XPuzzle.XPuzzle(child_slideUp),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideUp), movedTile))

    child_slideRight, movedTile = nodeToGenerateChildren.child_node.slideRight()
    if(not (child_slideRight is None) and not checkInClosedList(child_slideRight)):
        index = checkInOpenList(child_slideRight)
        if index > -1:
            open_list[index] = Node(XPuzzle.XPuzzle(child_slideRight),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideRight), movedTile)
        elif index == -2:
            open_list.append(Node(XPuzzle.XPuzzle(child_slideRight),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideRight), movedTile))

    child_slideLeft, movedTile = nodeToGenerateChildren.child_node.slideLeft()
    if(not (child_slideLeft is None) and not checkInClosedList(child_slideLeft)):
        index = checkInOpenList(child_slideLeft)
        if index > -1:
            open_list[index] = Node(XPuzzle.XPuzzle(child_slideLeft),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideLeft), movedTile)
        elif index == -2:
            open_list.append(Node(XPuzzle.XPuzzle(child_slideLeft),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideLeft), movedTile))
    
    child_slideWrappingSlide, movedTile = nodeToGenerateChildren.child_node.wrappingSlide()
    if(not (child_slideWrappingSlide is None) and not checkInClosedList(child_slideWrappingSlide)):
        index = checkInOpenList(child_slideWrappingSlide)
        if index > -1:
            open_list[index] = Node(XPuzzle.XPuzzle(child_slideWrappingSlide),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideWrappingSlide), movedTile)
        elif index == -2:
            open_list.append(Node(XPuzzle.XPuzzle(child_slideWrappingSlide),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideWrappingSlide), movedTile))

    child_slideDiagonalSlideInside, movedTile = nodeToGenerateChildren.child_node.diagonalSlideInside()
    if(not (child_slideDiagonalSlideInside is None) and not checkInClosedList(child_slideDiagonalSlideInside)):
        index = checkInOpenList(child_slideDiagonalSlideInside)
        if index > -1:
            open_list[index] = Node(XPuzzle.XPuzzle(child_slideDiagonalSlideInside),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDiagonalSlideInside), movedTile)
        elif index == -2:
            open_list.append(Node(XPuzzle.XPuzzle(child_slideDiagonalSlideInside),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDiagonalSlideInside), movedTile))

    child_slideDiagonalSlideOpposed, movedTile = nodeToGenerateChildren.child_node.diagonalSlideOpposed()
    if(not (child_slideDiagonalSlideOpposed is None) and not checkInClosedList(child_slideDiagonalSlideOpposed)):
        index = checkInOpenList(child_slideDiagonalSlideOpposed)
        if index > -1:
            open_list[index] = Node(XPuzzle.XPuzzle(child_slideDiagonalSlideOpposed),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDiagonalSlideOpposed), movedTile)
        elif index == -2:
            open_list.append(Node(XPuzzle.XPuzzle(child_slideDiagonalSlideOpposed),nodeToGenerateChildren,Heuristics.getHammingDist_GOAL(child_slideDiagonalSlideOpposed), movedTile))

    #sort element in open_list
    open_list.sort(key=lambda x: x.heuristicCost, reverse=False)