# for normal pattern
"""
1
1 2
1 2 3
1 2 3 4
"""
"""n = int(input("Enter the last index-1: "))
for i in range(1, n):  # rows
    for j in range(1, i+1):  # columns
        print(j, end=" ")
    print()"""
# for a pattern like this
"""
1
2 2
3 3 3
4 4 4 4

n = int(input("Enter the last index-1: "))
for i in range(1, n):  # rows
    for j in range(1, i+1):  # columns
        print(i, end=" ")
    print()"""
# for a reverse pattern
"""
1 1 1 1
2 2 2
3 3
4

n = int(input("Enter the last index-1: "))
for i in range(1, n):  # rows
    for j in range(n, i, -1):  # columns
        print(i, end=" ")
    print()"""
# for a pattern like
"""
    *
  * *
* * *  
or
    *
  *   *
*   *   *

n = int(input("Enter the last index-1: "))
for i in range(1, n):  # rows
    for j in range(n-1, i, -1):  # columns
        print(" ", end=" ")
    for k in range(i):
        print(" * ",end=" ")
    print()"""

# for a pattern
"""
1
2 1
3 2 1
4 3 2 1 

n = int(input("Enter the last index-1: "))
for i in range(1, n):  # rows
    for j in range(i, 0, -1):  # columns
        print(j, end=" ")
    print()"""
# for a pattern
"""
*
* *
* * *
* *
*
or
     *
   *   *
 *   *   *
   *   *
     *

n = int(input("Enter the last index-1: "))
for i in range(1, n):  # rows
    for j in range(n - 1, i, -1):  # columns
        print(" ", end=" ")
    for k in range(1, i+1):  # columns
        print(" * ", end=" ")
    print()
for i in range(1, n-1):  # rows
    for j in range(1, i+1):  # columns
        print(" ", end=" ")
    for j in range(n-1, i,-1):  # columns
        print(" * ", end=" ")
    print()"""
# for a pattern
"""
1
2 4
3 6 9
4 8 12 16 
"""
n = int(input("Enter the last index-1: "))
for i in range(1, n):  # rows
    for j in range(1,i+1):  # columns
        print(i*j, end=" ")
    print()




