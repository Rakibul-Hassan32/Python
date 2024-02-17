# normal functions
# a=" hello world {}, stay blessed "
"""print(a.index("e"))
print(a.capitalize())
print(len(a))
print(a.upper())
print(a.lower())
print(a.casefold())  # lower case conversion
print(a.title())
print(a.find("w"))"""

# special functions
"""name = "to everyone "
a = a.format(name)
print(a)  # it replaces with curly braces
print(a.center(80, '*'))  # fill any characters
print(a.center(100))  # space"""

# some other functions
"""a = "hello"
b = "hello123"
c = "12346"
d = "HELLO"
e = " "
f = "Hello 123@"
g = "1.234" """

# if all characters are alphanumeric = isalnum()
"""print(a.isalnum())
print(b.isalnum())
print(f.isalnum())  # false because special character
print(e.isalnum())  # false of space
print(g.isalnum())  # false decimal points"""

# if all characters are alphabet = isalpha()
"""print(a.isalpha())
print(b.isalpha())"""

# if all characters are decimal = isdecimal()
"""print(a.isdecimal())
print(c.isdecimal())
print(g.isdecimal())  # false because of point"""

# if all digit = isdigit() = isnumeric()
"""print(g.isdigit())  # # false because of point
print(c.isdigit())"""

# check upper or lower = isupper(), islower()
"""print(d.isupper())
print(a.islower())"""

# check only space = isspace()
# print(e.isspace())

# istitle = first character of every word is capital or not
"""print(a.istitle())
print(f.istitle())"""

# endswith what symbol
# a = "Harry Potter"
"""print(a.endswith("r"))
print(a.endswith("e",6,11))
print(a.index("e"))"""

# startswith
"""print(a.startswith("h"))
print(a.index("p"))
print(a.startswith("p",6,11))"""

# swap case = lower becomes upper and vice versa
# print(a.swapcase())

# strip = trimmed version
"""a = "   .Harry Potter   *"
print(a)
print(a.strip(".,*, "))"""

# split the string
"""a = "#OOFD#BRB#OMW#TB"
b = "hello. my name is rakib. how are you?"
print(a.split("#"))
print(b.split("."))"""

# ljust = left justified version
"""a = "harry potter"
x = a.ljust(20,"*")
print(x,"is my fav movie")

# rjust
y = a.rjust(20,"x")
print(y,"is my fav movie")"""

# replace
"""a = "jhon banega don"
print(a.replace("jhon","bob"))"""

# rindex()/rfind/find/index
# that returns the last position/ same as index
a = "jhon banega don fy hfj gfya"
print(a.rindex("a",7,16))
print(a.rfind("fy"))
print(a.rfind("fy", 14, 20))
print(len(a))







