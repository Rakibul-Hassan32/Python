import pandas as pd
# "keys": ["k1", "k2", "k1", "k2"],

dict1 = {"Names": ["John", "Ben", "David", "Peter"],
         "Houses": ["red", "blue", "green", "red"],
         "Grades":["3rd", "8th", "9th", "8th"]}
df = pd.DataFrame(dict1)
#                               pivot
# print(df)
# customized format of Dataframes as identical matrices
# print(df.pivot(index="keys", columns="Names", values=["Houses", "Grades"]))
#                              Melting
"""
   Names variable  value
0   John   Houses    red
1    Ben   Houses   blue
2  David   Houses  green
3  Peter   Houses    red
"""
print(pd.melt(df, id_vars=["Names"], value_vars=["Houses", "Grades"], var_name="Houses&Grades",value_name="values"))



