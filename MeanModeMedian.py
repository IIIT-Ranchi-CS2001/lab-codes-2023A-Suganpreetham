li=[5,6,2,9,5,1,7,9,3,6,9,5,5]

so_li=sorted(li)
print("Printing sorted list :",so_li)

ma=1
mode=so_li[0]
count=1
x=1
sum=so_li[0]
n=len(so_li)
while(x<n):
    sum+=so_li[x]
    if(so_li[x]==so_li[x-1]):
        count+=1
    elif(ma<count):
        ma=count
        mode=so_li[x-1]
        count=1
    else:
        count=1
    x+=1    

print("Mean is :",sum/n)
if(n%2==0):
    med=(so_li[(n-1)//2]+so_li(n/2))/2
    print("Median is:",med)
else:
    med=so_li[(n-1)//2]
    print("Median is:",med)     
print("Mode is :",mode)