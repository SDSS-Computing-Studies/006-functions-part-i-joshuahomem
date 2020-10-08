#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math
def distance(x,y):
    one=x[0]
    two=x[1]
    three=y[0]
    four=y[1]
    dist1=one-three
    dist2=two-four
    acdist=(dist1**2 + dist2**2)**(1/2)
    acdist=round(acdist,3)
    return acdist

p=distance((1,1),(2,2))
print(p)