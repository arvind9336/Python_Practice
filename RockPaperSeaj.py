import random
n=int(input("How many time you want to play the gaame: "))
print("Please read the instruction carefully: ")
print("press the key 1 for rock")
print("press the key 2 for paper")
print("press the key 3 for scissor")
# my_list=["rock","paper","scissor"]
# y=0
# s=0
def game():
    my_list=["rock","paper","scissor"]
    y=0
    s=0
    for i in range(1,n+1):
        str1=input("it's totaly depend on you, what are you choose like 1 or 2 or 3 : ")
        if str1 in '123':
            choose1=''.join(random.choices(my_list,k=1))
            if (str1=='1' and choose1=='rock') or (str1=='2' and choose1=='scissor') or (str1=='3' and choose1=='paper'):
                print(f"{i} round Tie")
            elif (str1=='1' and choose1=='scissor') or (str1=="2" and choose1=='paper'):
                print(f"{i} round you won")
                y=y+1
            else:
                print(f"{i} round system won")
                s=s+1
        else:
            print("Please ! Enter valid input")
            break
    if y>s:
        print("You are winner !")
    elif s>y:
        print("system are winner !")
    else:
        print("no anyone not winner !")
game()
d=input("Do you want to continue this game, please enter yes otherwise no: ")
if (d.lower()=='yes'):
    print("Restart the Game")
    game()
else:
    print("You are out of the game")