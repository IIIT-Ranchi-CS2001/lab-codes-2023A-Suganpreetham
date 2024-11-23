from random import randint
K=int(input("How many random numbers required(>=10)? "))
N=int(input("What is the limit of the random numbers? "))
i=int(1)
list=[]
while(i<=K):
    list.append(randint(1,N))
    i=i+1
print(list)