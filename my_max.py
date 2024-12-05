def my_max(li):
    m='0'
    for x in range(len(li)):
        if(m<li[x]):
            m=li[x]
    return m

li=list((input("Enter the numbers in list with space separated : ")).split())

m=my_max(li)
print("Maximum number in the list is :",m)