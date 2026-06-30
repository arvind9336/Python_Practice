# l=["python Programming"]
# lst=[]
# for x in l:
#     s=''
#     for i in range(len(x)):
#         if x[i].lower() not in 'hm':
#             s=s+x[i]
#     lst.append(s)
# print(lst)

l=["python Programming"]
lst=[]
for x in l:
    s=''
    for i in range(len(x)):
        if x[i].lower() not in 'hm':
            s=s+x[i]
    lst.append(s)
print(lst)