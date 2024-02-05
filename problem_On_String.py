A = "Why fit in, When you are Born to Stand Out!"
# to find length
print(len(A))
# how many "o" is occurring
# hard method
"""count=0
for i in range(0,len(A)):
    if A[i] == 'o':
        count += 1
print(count)"""
# easy method
print(A.count("o"))

# lower and upper case
a = A.lower()
print(a)
b = A.upper()
print(b)

# string into a title
c = A.title()
print(c)

# index number of a string
print(A.find("fit in"))



