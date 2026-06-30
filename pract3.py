str1="Hello Arvind"
s=''
for i in range(len(str1)):
    if str1[i].lower() in "aeiou":
        print(str1[i],i)