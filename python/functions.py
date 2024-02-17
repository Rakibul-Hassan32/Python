"""def hello():
    print("hello world")


hello()


def add():
    x = 56
    y = 54
    print(x+y)


add()"""


# parameterized function
"""a = int(input("enter the first value: "))
b = int(input("enter the second value: "))


def add(x, y):
    print(x*y)


add(a,b)"""

# arbitrary function


"""def hello(*name):
    print("my name is: ", name[1])

hello("John", "Gurenge", "Nanimo")"""

# return and recursion


"""def hello():
    return "Hello world"


print(hello())

x = int(input("enter the first value: "))
y = int(input("enter the second value: "))
def add(a,b):
    return a+b

print(add(x,y))"""

# recursion of fibonacci and factorial number
n = int(input("enter the first value: "))


def hello(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return hello(n-1)+hello(n-2)


print("The n-th fibonacci number is: ", hello(n))


def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)


print("The factorial of n-th number is: ", fac(n))



