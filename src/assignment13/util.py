import numpy as np
def find_max_and_min(x, y, matrix):
    arr = np.array(matrix)
    min_values = np.min(arr, axis=1)  # Find min in each row
    result = np.max(min_values)       # Find max of those min values
    return result  # Return the result
