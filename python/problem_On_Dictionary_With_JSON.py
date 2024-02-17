import json
# student_data = {"name": "David", "age": 13, "marks": 87}

# convert json to string
# data = json.dumps(student_data)
# print(data, type(data))

# access the data
# print(student_data["age"])
# data1 = json.loads(student_data)

# pretty print
"""data = json.dumps(student_data,indent=4,separators=(",", "="))
print(data)"""

# sort the following json keys and write them into a file
"""f = open("demo.json", "w")
data = json.dumps(student_data,indent=4,sort_keys=True)
f.write(data)"""

# access the nested key marks from the following nested data
student_data = """{ "student":
                   { "grade":
                    { "name":"David", "marks": 87 }
                   }
               }"""

data = json.loads(student_data)
print(data["student"]["grade"]["marks"])









