import random
print("Rock==0 ,Paper==1,Scissor==2 ")
user=int(input("type 0 for rock,type 1 for paper,type 2 for scissor:"))
print(f"User chooses {user}")
computer=random.randint(0,2)
print(f"Computer chooses {computer}")
if  computer == user:
        print("....It's a Draw....")
elif computer==0 and user==2 or computer==1 and user==0 or computer==2 and user==1:
        print("....Computer wins...")
else:
        print("...User wins....")