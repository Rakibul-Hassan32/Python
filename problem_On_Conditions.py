# if a number positive or not and alphabet is vowel or not and number is odd or even
b = int(input("Enter the number: "))
# a = input("Enter a character: ")
# print("The number is positive") if a>=0 else print("The number is negative")
# print("The number is even") if a%2==0 else print("The number is odd")
# print("The letter is alphabet") if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' else print("The letter is consonant")
# number length
if 9 >= b >=0:
    print("The number is single digit")
elif 99 >= b >=10:
    print("The number is two digit")
elif 999 >= b >=100:
    print("The number is three digit")
elif 9999 >= b >= 1000:
    print("The number is four digit")
elif 99999 >= b >= 10000:
    print("The number is five digit")
else:
    print("The number is multi digit")