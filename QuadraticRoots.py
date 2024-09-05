import math
from math import *
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))
d=(b**2)-4*a*c
if(d==0):
    print("The roots are real repeated roots:",-b/(2*a))
elif(d>0):
    print("The roots are real distinct roots:",(-b+d**(1/2))/2*a,"and",(-b-d**(1/2))/2*a)
else:
    print("The roots are complex roots, realpart:",-b/(2*a),"imaginarypart:",math.sqrt(-d)/(2*a))