#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)

"""

def largest(mylist):
    mylist.sort()
    a=mylist[-1]
    return a
x=largest([1,3,6542,9])
print(x)
    