s=input("Enter your string : ")
b=input("Enter the character of which you want to find the ocurrence : ")

count=0
i=0
a=len(s)
while(i<a):
    if(s[i]==b):
        count+=1
    i+=1    

print(f"Number of occurence of '{b}' in given string '{s}' is:",count)