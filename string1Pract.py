def RemoveVowelsWord(s):
    l=s.split()
    l1=[]
    v='aeiou'
    for x in l:
        c=0
        for i in range(len(x)):
            if x[i].lower() in v:
                c=c+1
        if c==0:
            l1.append(x)
    return ''.join(l1)

st1="This is python code in vs"
print(RemoveVowelsWord(st1))