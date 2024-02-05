# dictionaries are hold inside {} = keys and values
"""employee_data = {"name": "John", "age": 24, "gender": "Male"}
print(employee_data)
# for specific data
print(employee_data["age"])
"""
# iteration in dictionaries
# student = {"name": "Jhon", "class": "6th", "roll_no": 23}

# printing all the keys and value one by one. Also both
"""for i in student:
    print(i) -> for keys only
    print(student[i]) ->  for values only
    print(i, ":", student[i])  -> for both """
# value function
"""for x in student.values():
    print(x) -> values only"""
# items function for both
"""for x,y in student.items():
    print(x, "-", y)"""

#  nested dictionaries
employe = {1: {"name": "Jhon", "age": 23, "gender": "Male"},
           2: {"name": "Luvna", "age": 24, "gender": "Female"},
           3: {"name": "Peter", "age": 27, "gender": "Male"}}
print(employe[3]["name"])



