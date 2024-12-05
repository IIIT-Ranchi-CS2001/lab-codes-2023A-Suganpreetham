import math
from math import *
a=float(input("Enter 1st side:"))
b=float(input("Enter 2st side:"))
c=float(input("Enter 3st side:"))
perimeter=a+b+c
s=(perimeter)/2
area=(s*(s-a)*(s-b)*(s-c))**(0.5)
print("Perimeter of Triangle is:",perimeter)
print("Area of Triangle is:",area)
a1=degrees(acos((b**2+c**2-a**2)/(2*b*c)))
a2=degrees(acos((c**2+a**2-b**2)/(2*a*c)))
a3=degrees(acos((a**2+b**2-c**2)/(2*b*a)))
print("The three angle of the triangle are:","\n","A: ",a1,"\n","B: ",a2,"\n","B: ",a3)