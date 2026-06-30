l=[1,2,3,4,5]
lst=[]
for i in l:
    if i%2==0:
        lst.append(f"{i}:Even")
    else:
        lst.append(f"{i}:Odd")
print(lst)