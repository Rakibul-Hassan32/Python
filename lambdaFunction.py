# a = lambda b: b*5
# print(a(5))

# x = lambda a,b,c: (a+b)*c
# print(x(3, 7, 3))

# local and global variable
x = 24
print(x)
def funv():
    global x
    x = 25
    return x
print(funv())
print(x)
