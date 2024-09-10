n=int(input("Which table do you want: "))
x=int(input("How mant lines do you want to print: "))
print("The table is: ")
i=1
while(i<=x):
    print(f"{n} X {i} = {n*i}")
    i+=1
