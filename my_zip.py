def my_zip(Customer_name, Customer_id, Shopping_point):
    ans=[]
    a=len(Customer_name)
    b=len(Customer_id)
    c=len(Shopping_point)
    
    
    if(a==b==c):
        for x in range(a):
            tu=(Customer_name[x],Customer_id[x],Shopping_point[x])
            ans.append(tu)
    else:
        m=min(a,b,c)
        for x in range(m):
            tu=(Customer_name[x],Customer_id[x],Shopping_point[x])
            ans.append(tu)
    
    return ans

Customer_name = tuple(input("Enter Customer names with comma separated : ").split(","))
Customer_id = tuple(input("Enter Customer IDs with comma separated : ").split(","))
Shopping_point = tuple(input("Enter Shopping points with comma separated : ").split(","))

result = my_zip(Customer_name, Customer_id, Shopping_point)
print(result)