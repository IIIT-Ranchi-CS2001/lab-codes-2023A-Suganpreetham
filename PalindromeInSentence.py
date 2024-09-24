s=input(str("Write the sentence:"))
list=s.split()

l=len(list)
for i in range(0,l):
    palindrome=1
    c=0
    length=len(list[i])
    while(c<length/2):
        if(list[i][c]==list[i][length-1-c]):
            c+=1
            continue
        else:
            palindrome=0
            break

    if(palindrome==1):
        print(list[i])