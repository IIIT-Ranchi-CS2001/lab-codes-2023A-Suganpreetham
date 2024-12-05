S=str(input("Enter the string: "))
l=len(S)
if(l%2==0):
    i=0
    x=0
    while(i<=l/2):
        if(S[i]==S[l-1-i]):
            i=i+1
        else:
            print(S,"not a palindrome.")
            x=1
            break
    if(x==0):
        print(S,"is a palindrome.")
else:
    i=0
    x=0
    while(i<=(l/2)-1):
        if(S[i]==S[l-1-i]):
            i=i+1
        else:
            print(S,"is not a palindrome.")
            x=1
            break

    if(x==0):
        print(S,"is a palindrome.")
