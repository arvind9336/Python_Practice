str1="Hello Arvind"
s=''
for i in range(len(str1)):
    if str1[i].lower() not in "aeiou":
        s=s+str1[i]
print(s)