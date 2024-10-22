print("Enter the customer names with , between them:",end="")
customername=str(input())
customer_name = customername.split(",")
print(customer_name)

print("Enter the customer ID's with , between them:",end="")
customerid=str(input())
customer_id = customerid.split(",")
print(customer_id)

print("Enter the customer points with , between them:",end="")
customerpoints=str(input())
customer_points = customerpoints.split(",")
print(customer_points)

#using zip
using_zip=list(zip(customer_name,customer_id,customer_points))
print(using_zip)

l1=len(customer_name)
l2=len(customer_id)
l3=len(customer_points)
mini=min(l1,l2,l3)

#without using zip
customer_data=[(customer_name[i],customer_id[i],customer_points[i]) for i in range(mini)]
print(customer_data)

# #with sorted function

sort=sorted(customer_data, key=lambda x:x[2])#based on points
print(sort)

#without sorted function (based on id)

for i in range(len(customer_data)):
    for j in range(0, len(customer_data) - i - 1):
        if customer_data[j][1] > customer_data[j + 1][1]:
            # Swap if the current element is greater than the next element
            customer_data[j], customer_data[j + 1] = customer_data[j + 1], customer_data[j]

print(customer_data)