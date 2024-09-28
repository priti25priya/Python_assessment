import numpy as np

def CalculateFloorCeilRint(arr):
    result = []
    for num in arr:
        floor_value = np.floor(num)
        ceil_value = np.ceil(num)
        rint_value = np.rint(num)
        result.append((floor_value, ceil_value, rint_value))
    return result
