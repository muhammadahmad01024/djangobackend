import numpy as np
import math


def normalize(array):
    min = math.inf
    max = - math.inf

    for row in array:
        for col in row:
            if min > col:
                min = col
            if max < col:
                max = col

    array = (array - min) / (max - min)
    return array


r = int(input("Enter Row size: "))
c = int(input("Enter Col size: "))
range = 10
M1 = np.random.randint(range, size=(r, c))

M2 = normalize(M1)
print(M2)
