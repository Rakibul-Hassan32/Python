import numpy as np
a = [[10,20,30],[40,50,60]]
arr = np.array(a)
print(arr)
print(arr.shape)  # row, column
print(len(arr))  # only rows
print(np.size(arr))
print(type(arr))
print(arr.dtype)  # data type
print(arr.astype(float))  # type conversion
