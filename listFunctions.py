a = ["Ironman", "Thor", "Captain America", "Thor", "Hulk", "Thor"]
print(a)
# length of list
print(len(a))
# occurrences of a particular element
print(a.count("Thor"))
# add an element in the last position of a list
a.append("Superman")
print(a)
# to add in a specific position
a.insert(2, "Vision")
print(a)
# to remove an element in the last position
a.pop()
print(a)
# to remove an element specifying its name
a.remove("Thor")
print(a)
# to remove from a certain location
a.pop(2)  # by giving the index inside
print(a)

