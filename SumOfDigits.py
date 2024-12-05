n=int(input("Enter the number: "))
m=n
sum=0
while(n>0):
    d=n%10
    sum=sum+d
    n=n//10
print(f"The sum of digits of number {m} is: ",sum)