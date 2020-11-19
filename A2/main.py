import os
import numpy as np
import glob
import time
import UnfiormCostSearch
def read_samples(input_filename):
    """
    Read in the sample initial states.
    :param input_filename: The filename to use for reading-in the data.
    :return: The array of samples.
    """
    # Define an array to store the initial puzzle states
    initial_states = []

    # Read the sample initial-states from the input file line-by-line and add
    # each one into our array
    file = open(input_filename, "r")

    while True:
        # Get the next line from the file
        line = file.readline()

        # If the line is empty, we are done reading
        if not line:
            break

        # Write our sample initial-state to our array (strip out the newline character)
        initial_states.append(line.strip())
    # end: while

    # Don't forget to close our file connection
    file.close()

    return initial_states


print("am here")
input_file = "inputs/sample_inputs.txt"
sample_puzzles = read_samples(input_file)
uniformcost = UnfiormCostSearch.UniformCost(0, np.array([[3, 0, 1, 4], [2, 6, 5, 7]]) , 2)
uniformcost.solve()
