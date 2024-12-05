#starts from 0,1,1,2,3,5,8,13,21,34,55,89....so on.
n=int(input("How many Fibonacci numbers do you want: "))
if(n==0):
    print("NOTHING TO PRINT.")
elif(n==1):
    print(f"The Fibonacci series of first {n} numbers is: 0.")
else:
    ls=0
    l=1
    print(f"The Fibonacci series of first {n} numbers is: 0,1",end="")
    n=n-2
    while(n>0):
        d=l+ls
        ls=l
        l=d
        print(f",{d}",end="")
        n-=1
    print(".")