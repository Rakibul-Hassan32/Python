# tuples = ordered and un-mutable(not changeable) --> no modification possible
"""a = "apple","mango","banana",1.67
print(a)
print(type(a))
# when we have only one element in the tuple we can
b = ("banana",)
print(type(b))
"""
# slicing and iteration in tuples
a = "oneplus","vivo","redmi","samsung","nokia"
"""print(a[::-1])
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[::2])
print(a[2::-1])"""

# using for loops
"""for i in a:
    print(i)
 """
# along with range and length in for loop
"""for i in range(len(a)):
    print(a[i])"""
# along with while loop
"""i = 0
while i < len(a):
    print(a[i])
    i += 1"""

# conversion of tuples and related functions
"""print("before conversion: ", a, " :", type(a))
a = list(a)  # conversion of tuple to list because we can't update a tuple
print("after conversion: ", a, " :", type(a))
a.append("vivo")
print(a)
a = tuple(a)  # conversion of list to tuple
print("again tuple conversion: ", a, " :", type(a))"""

# some functions in tuple
print(a.count("vivo"))
print(a.index("samsung"))





