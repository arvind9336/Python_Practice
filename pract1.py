em=["Arvind","Akash"]
cap=[]
for x in em:
    s=''
    for i in range(len(x)):
        s=s+x[i].upper()
    cap.append(s)
print(cap)