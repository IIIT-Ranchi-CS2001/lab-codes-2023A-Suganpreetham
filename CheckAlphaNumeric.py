s=str(input("Enter the string: "))
is_aphanumeric=s.isalnum()
if(is_aphanumeric==True):
    print(f"The string '{s}' : is alphanumeric.")
else:
    print(f"The string '{s}' : is not alphanumeric.")