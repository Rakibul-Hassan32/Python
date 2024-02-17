# maximum of 3 numbers
"""def maxi(val1,val2,val3):
    return max(val1,val2,val3)
print(maxi(56, 70, 30))"""


# square of 1 to 30

"""def create_list():
    l = []
    for i in range(1,31):
        l.append(i**2)
    return l

print(create_list())"""

# check a number prime or not
"""a = int(input("enter the number: "))


def prime(x):
    if x == 0 or x==1:
        print("not prime")
    else:
        for i in range(2,x):
            if x%i == 0:
                print("not prime")
                break
        else:
            print("prime")


prime(a)"""

# sum of all numbers in a list


"""def add(numbers):
    answer = 0
    for i in numbers:
        answer += i
    return answer


print(add([5, 67, 9, 23, 0, 25, 60]))"""

# using recursion


def add(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0]+add(numbers[1:])


print(add([5, 67, 9, 23, 0, 25, 60]))

# fibonacci
n = int(input("enter the first value: "))


def hello(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return hello(n-1)+hello(n-2)


print("The n-th fibonacci number is: ", hello(n))























