# unordered, unique and mutable
a = {"Ironman", "Thor", "Hulk", "Captain America"}
b = {"Superman","Batman","Wonder-Women"}
c = {"Hulk","Thor"}
"""print(a)
print(type(a))
# iteration
for i in a:
    print(i)
# functions of sets
# add
a.add("Vision")
print(a)
# pop
a.pop()
print(a)
# remove
a.remove("Hulk")
print(a)
# discard
a.discard("Thor")
print(a)
# copy
b = a.copy()
print(b)"""
# isdisjoint or intersection
print(a.isdisjoint(c))  # same = false else true
# issubset
print(a.issubset(c))
# issuperset = complete set present or not
print(a.issuperset(c))
# update or union
a.update(c)
print(a)
# clear
a.clear()
print(a)








