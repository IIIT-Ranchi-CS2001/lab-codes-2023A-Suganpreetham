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
        sc.append(pow(int(c[i]),0.5))
    for i in range(0,lp):
        sp.append(pow(int(p[i]),2))

l=input("Enter the numbers of the list: ")
list=l.split(" ")
length=len(list)
composite,prime=[],[]
compri(list,length)
print("The composite numbers are:",composite)
print("The prime numbers are:",prime)
sc,sp=[],[]
squares(composite,prime,len(composite),len(prime))
print("The square roots of composite numbers are:",sc)
print("The squares of prime numbers are:",sp)

fig, axs = plt.subplots(2, 1, figsize=(8, 10))
# Subplot for prime numbers vs their squares
axs[0].scatter(prime, sp, color='blue')
axs[0].set_title("Prime Numbers vs Their Squares")
axs[0].set_xlabel("Prime Numbers")
axs[0].set_ylabel("Squares of Prime Numbers")
# Subplot for composite numbers vs their square roots
axs[1].scatter(composite, sc, color='red')
axs[1].set_title("Composite Numbers vs Their Square Roots")
axs[1].set_xlabel("Composite Numbers")
axs[1].set_ylabel("Square Roots of Composite Numbers")

plt.tight_layout()
plt.show()