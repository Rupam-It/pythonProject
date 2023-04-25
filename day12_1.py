# this is a number gaussing game
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

print(logo)

import random

number_genarate=random.randint(1,100)

def cheaking_nubmer(number:int,number_genarate:int):
    if number==number_genarate:
        return True
    elif number<number_genarate:
        print("Too Low.")
        return False
    else:
        print("Too high..")
        return False



def easy_level(nubmer_generate:int):
    i=10
    while i>0:
        number=int(input("Make a guess: "))
        if cheaking_nubmer(number,number_genarate):
            print("\nYo.... You make the right guess, number was",number)
            print()
            break
        if i>1: 
            print("guess again.")
            print("You have only "+str(i-1)+" times left..")
            i-=1
            continue
        elif i==1:
            print("\n\nYou Loose..")
        i-=1


def hard_level(nubmer_generate:int):
    i=5
    while i>0:
        number=int(input("Make a guess: "))
        if cheaking_nubmer(number,number_genarate):
            print("\nYo.... You make the right guess, number was",number)
            print()
            break
        if i>1: 
            print("guess again.")
            print("You have only "+str(i-1)+" times left..")
            i-=1
            continue
        elif i==1:
            print("\n\nYou Loose..")
        i-=1


print("Welcome to nubmer guessing Game..")
print("I'm thinking a number of between 1 to 100")

level=input("Choose difficulty,Type 'easy' or 'hard': ").lower()

if level=='easy':
    print("\nYou have 10 chance to guess to right number\n")
    easy_level(number_genarate)
elif level=='hard':
    print("\nYou have 5 chance to guess to right number\n")
    hard_level(number_genarate)
else:
    print("\nYou have 5 chance to guess to right number\n")
    hard_level(number_genarate)