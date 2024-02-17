import numpy as np
"""arr = np.array([[50, 20, 60], [50, 70, 60]])  # array size must be equal
print(arr)
print(type(arr))
arr = np.array([50, 20, 60, 20, 30])
print(arr[::-1])"""

arr = np.array([[50, 20, 60, 30], [50, 70, 60, 40], [100, 70, 20, 90]])
# print(arr[::-1, ::-1])   even in slicing for n-dimensional array the values must be same
"""print(arr[1, 2:4])  # indexing 2d array
print(arr[2, 2:4]) """

print(np.shape(arr))  # shape of array (row, column)
print(np.size(arr))  # total elements (row * column)
print(np.ndim(arr))  # dimensions
print(arr.dtype)  # data type



















