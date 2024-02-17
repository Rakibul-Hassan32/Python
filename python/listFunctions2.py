a = ["Ironman", "Thor", "Captain America", "Hulk"]
# to create a copy of list
"""b = []
print(b)
b = a.copy()
print(b)"""
# to access an index
# print(a.index("Hulk"))

# to extend
"""c = ["Vision", "Spiderman"]
c.extend(a)
print(c)
print(a)"""

# to reverse the list without slicing
"""a.reverse()
print(a)"""

# to sort
"""a.sort()
print(a)
d=[8, 5, 6, 2, 1, 0, 7]
d.sort()
print(d)"""
# to clear all the data from the list like erase
"""a.clear()
print(a)"""

# list comprehension
l1=[30,40,50,60]
# l2=[]
"""for i in l1:
    if i > 45:
        l2.append(i)"""
l2 = [i for i in l1 if i > 45]
print(l1, "\n", l2)






