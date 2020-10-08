#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""

def hypotenuse(a,b,c,):
    import math    
    if c==True:
        Hypo=(a**2)+(b**2)
        ans=Hypo**(1/2)
        return ans
    elif c==False and a>b:
        short1= (a**2)-(b**2)
        ans2=short1**(1/2)
        return ans2
    elif c==False and b>a:
        short2=  (b**2)-(a**2)
        ans3=short2**(1/2)
        return ans3

lenght=hypotenuse(4,3,False)
print(lenght)