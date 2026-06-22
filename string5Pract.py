def wordReverse(l):
    l1=[]
    for x in l:
        l1.append(x[::-1])
    return l1
l=["Python","Java","script"]
print(wordReverse(l))