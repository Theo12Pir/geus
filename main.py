from rich import print
from random import randint
print("[bold blue]guess a number![/bold blue]")
nuber = randint(0,100)
nubers=[]
max_tries = 7
current_try = 0
while current_try <= max_tries:
    current_try+1
    user_geus = int(input("Geuss new numer: "))
    if user_geus in nubers:
        print("same mubers,try again")
        continue
    else:
        nubers.append(user_geus)
    if user_geus == nuber:
        print (f"you won with {current_try}tries!")
        break
    elif user_geus > nuber:
        print("lower")
    else:
        print("higher") 
if current_try > max_tries:
    print("LOSER!!!")


