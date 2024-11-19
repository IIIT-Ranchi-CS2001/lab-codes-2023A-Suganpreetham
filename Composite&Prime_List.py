import math
import matplotlib.pyplot as plt

def compri(self,len):
    for i in range(0,len):
        c=int(0)
        if(int(self[i])==1):
            print("1 is neither prime nor composite.")
            self[i]=int(self[i])
            continue
        if(int(self[i])==2):
            prime.append(int(self[i]))
            continue
        for j in range(2,int(self[i])):
            if(int(self[i])%j==0):
                composite.append(int(self[i]))
                c=1
                break
        if(c==0):
            prime.append(int(self[i]))

def squares(c,p,lc,lp):
    for i in range(0,lc):
        sc.append(pow(int(c[i]),2))
    for i in range(0,lp):
        sp.append(pow(int(p[i]),2))

l=input("Enter the numbers of the list: ")
list=l.split(" ")
length=len(list)
composite=[]
prime=[]
compri(list,length)
print("The composite numbers are:",composite)
print("The prime numbers are:",prime)
sc=[]
sp=[]
squares(composite,prime,len(composite),len(prime))
print("The squares of composite numbers are:",sc)
print("The squares of prime numbers are:",sp)

plt.scatter(prime,sp)
plt.xlabel('X-axis(Prime)')
plt.ylabel('Y-axis(Squares of Prime)')
plt.title('Scatter Plot Example')
plt.show()

plt.scatter(composite,sc)
plt.xlabel('X-axis(Composite)')
plt.ylabel('Y-axis(Squares of Composite)')
plt.title('Scatter Plot Example')
plt.show()