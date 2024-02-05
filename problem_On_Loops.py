# 1: sum of even numbers from 0 to 50
"""sum=0
for i in range(0,51,2):
    sum+=i
print(sum)
sum=0
for i in range(0,51):
    if i%2==0:
        sum+=i
print(sum)"""
# 2: square of numbers from 1 to 20
"""for i in range(1,21):
    print(i,i**2)"""
# 3: sum of first 10 odd numbers
"""count=1
i=0
sum = 0
while i!=10:
    sum+=count
    count+=2
    i+=1
print(sum)"""
# 5: for shopping mall payment
while True:
    Name = input("Enter customer name: ")
    total = 0
    while True:
        quantity = int(input("Enter product quantity: "))
        amount = int(input("Enter product price: "))
        total+=amount*quantity
        con = input("If you want to buy other things: ")
        if con == "no":
            break
    print("-"*40)
    print("Name: ", Name)
    print("Amount to be paid: ", total)
    print("-"*40)
    print("Happy Shopping")

    con1 = input("Do you want to go to next customer: ")
    if con1 == "no":
        break

