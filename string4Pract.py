def Removewhite(s):
    st=''
    for i in range(len(s)):
        if s[i]==' ':
            i=i+1
        else:
            st=st+s[i]
    return st
st="Hello sir ji"
print(Removewhite(st))