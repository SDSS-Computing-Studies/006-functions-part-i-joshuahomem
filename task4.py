#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""
def isInteger(a):
    a=float(a)
    b=int(a)
    if a==b:
        return True
    elif a!=b:
        return False

f=isInteger(2)
print(f)

