import random
import string
my_list=[]
cc=''
for i in range(0,4):
    generate_char=random.choice(string.ascii_uppercase)
    cc=cc+generate_char
for i in range(0,4):
    generate_int=random.randint(1,9)
    cc=cc+str(generate_int)
print(cc)

# Or
# def gen_cc():
#     a_to_z='abcdefghijklmnopqrstuvwxyz'
#     n='0123456789'
#     char=[random.choice(a_to_z).upper() for i in range(1,5)]
#     num=[random.choice(n) for i in range(1,5)]
#     print("".join(char+num))
# for i in range(1,2):
#     gen_cc()

# without loop:

# a_to_z='abcdefghijklmnopqrstuvwxyz'
# n='0123456789'
# char="".join(random.choices(a_to_z,k=4))
# num=str(int(random.randint(1000,9999)))
# print(char.upper()+num)