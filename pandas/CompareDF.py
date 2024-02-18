import pandas as pd

dict1 = {"Fruits": ["Mango", "Banana", "Apples", "Papaya"],
         "Prices": [100, 50, 150, 35],
         "Quantity": [15, 10, 10, 3]}
df1 = pd.DataFrame(dict1)
# print(df1)

df2 = df1.copy()
# change prices
df2.loc[0, "Prices"] = 120
df2.loc[1, "Prices"] = 40
df2.loc[3, "Prices"] = 60
# change quantities
df2.loc[0, "Quantity"] = 13
df2.loc[2, "Quantity"] = 11
df2.loc[3, "Quantity"] = 2
print(df2)

# compare
# print(df1.compare(df2))
"""print(df1.compare(df2, align_axis=0))  # row wise / horizontal"""
"""print(df1.compare(df2, keep_equal=True))  # includes the non-changeable unlike compare"""
print(df1.compare(df2, keep_shape=True))  # compares all parameters
# NaN = not a number



