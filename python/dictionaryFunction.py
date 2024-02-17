student = {"name": "Jhon", "class": "6th", "roll_no": 23}
# get
x = student.get("roll_no")
print(x)
# items
a = student.items()
print(a)
# keys
b = student.keys()
print(b)
# values
c = student.values()
print(c)
# copy
d = student.copy()
print(d)
# set default
y = student.setdefault("roll_no",24)
print(y)