import math 
from math import *
print("Enter the values of X1,X2,Y1 and Y2 in the respective order:")
user_input = [int(input(f"{i+1}: ")) for i in range(4)]
m=(user_input[0]-user_input[1])/(user_input[2]-user_input[3])

print(f"X - {user_input[0]} = {m}*(Y - {user_input[2]})")