l=["python Programming"] # output:["programming python"]
# for word in l:
#     lst.append(word[::-1])
# print(lst)
res=[' '.join(s.split()[::-1]) for s in l]
print(res)