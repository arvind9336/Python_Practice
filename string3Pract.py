def StrNum(l):
    l1=[]
    for x in l:
            s=''
            for i in range(len(x)):
                if x[i] in '0123456789':
                    s=s+x[i]
            l1.append(s)
    return l1
l=["abc123","45def","gh6"]
print(StrNum(l))