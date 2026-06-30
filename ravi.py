n=int(input("Enter any number: "))
l=[]
if n==1:
    print("It is not prime number")
elif n>=2:
    for i in range(2,n+1):
        for j in range(2,n+1):
            if i%j==0:
                break
        if j not in l:
            l.append(j)
else:
    print("Enter valid number")
print(l)