print("Enter the string:",end="")
s=str(input())
dict={}
l=len(s)
for char in s:
    if char in dict:
        dict[char] += 1
    else:
        dict[char]=1

for ch in dict:
    print(ch,":",dict[ch])
