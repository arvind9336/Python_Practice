str1="Hello Arvind 123"
s=''
for i in range(len(str1)):
    if str1[i].isdigit():
        print(str1[i],i)