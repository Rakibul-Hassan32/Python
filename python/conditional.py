marks=int(input("Enter the mark of this exam: "))

"""if marks >= 90:
    print("3.95")
elif 90 > marks >= 60:
    print("pass")
else:
    print("thank you")
    
# nested
if marks >= 80:
    print("You will get a phone")
    if marks>= 95:
        print("You can go on a trip")
    else:
        print("Be happy with what you got")
elif 80 > marks >= 70:
    print("You will get a cycle")
    if marks >= 75:
        print("You can get choclates")
        if marks == 79:
            print("Congrats")
    else:
        print("Be happy with what you got")
else:
    print("Thank you")
    
# short 'hand if'
if marks >= 90: print("you will get a new phone")"""

# short 'hand if-else'
print("you will get a new phone") if marks >= 90 else print("Thank you")
