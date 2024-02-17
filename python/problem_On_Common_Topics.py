# for fibonacci series
"""a=0
b=1

for i in range(2, 11):
    c=a+b
    a = b
    b = c
    print(c)
"""
# prime or not
"""a = int(input("enter the number: "))
if a <= 1:
    print("not prime")
else:
    for i in range(2, a):
        if a%i == 0:
            print("not prime")
            break
    else:
        print("prime")"""
# palindrome
a = int(input("enter the number: "))
temp = a
rev=0
while a>0:
    dig=a%10
    rev = rev*10+dig
    a //=10  # floor division


if rev == temp:
    print("palindrome")
else:
    print("not palindrome")