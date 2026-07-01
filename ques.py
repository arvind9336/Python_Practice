import random
import string
import os
folder="emp_list"
os.mkdir(folder)
target=f"{os.getcwd()}"+"\\"+f"{folder}"
print(target)
os.chdir(target)
print(os.getcwd())
emp_list=["aman","arvind","akash","dishant"]
for i in emp_list:
    f=open(f"{i}.txt","w")
    f.write(f"emp_Name:{i} \nemp_Id: {str(random.randint(999,10000))+''.join(random.choices(string.ascii_uppercase,k=4))}")