# waf to remove last word from string
def RemoveLast(s):
    l1=[]
    l=s.split()
    for i in range(len(l)-1):
        l1.append(l[i])
    return ' '.join(l1)

st1="This is python code in vs"
print(RemoveLast(st1))
