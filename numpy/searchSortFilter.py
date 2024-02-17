import numpy as np
# for sorting
"""arr = np.array([[7, 8, 9, 4, 3, 1, 56, 0], [12, 80, 9, 40, 3, 10, 56, 200]])
print(np.sort(arr))"""

# for searching
"""arr = np.array([7, 8, 9, 4, 3, 1, 56, 0])
s = np.where(arr % 2 == 0)  # will search the indexes not the value
p = np.where(arr == 4)
print(s, p)"""

# sorted search
"""arr = np.array([1,2,3,4,5])
ss = np.searchsorted(arr, 2)
print(ss)"""

# filter
arr = np.array([20, 30, 40, 50])
"""fa = [True, False, True, False]
new = arr[fa]
print(new)"""

fa = arr > 30  # any condition
new = arr[fa]
print(new)








