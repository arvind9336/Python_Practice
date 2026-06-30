import random
# my_list=["arvind","akash","dishant","aman","anmol","gaurav"]
# res=random.choice(my_list)
# print(res)



# user max attempt=6
# each attempt random number generate
# random number generate sum
# fix_value=150 

m=6
s=0
fix_value=150
for i in range(0,m):
    generate_number=random.randint(1,50)
    s=s+generate_number
if s==fix_value:
    print("You are winner",s)
elif s>=140 and s<=160:
    print("You are very close",s)
else:
    print("Too far",s)