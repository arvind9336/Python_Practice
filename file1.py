f=open('demo.txt','r+')
data=f.read()
s=''
for i in data:
    if i not in """^&*()#$%^?!@'/.,0123456789\"""":
        s=s+i
file=open('new_demo.txt','w+')
file.write(s)
file.close()