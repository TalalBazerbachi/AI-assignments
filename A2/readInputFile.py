import numpy as np

def getPuzzles(filePath,dimensions):
    #read all lines in the file
    file = open(filePath, 'r')
    lines = file.readlines()
    file.close()

    puzzles = []#will store the puzzles

    for line in lines:
        nums = [int(n) for n in line.split()]#convert from string list to array of ints
        puzzles.append(np.reshape(nums, dimensions))#re-shape on depending on the dimensions tuple 

    return puzzles

# print(getPuzzles('puzzles.txt',(2,4)))