# this is a program for secrect oction
# one can bid one time 
# at the end highest bid win
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
import os


def max_bid(dic):
    l1=[]
    for name in dic:
        l1.append(dic[name])
    m=max(l1)
    for name in dic: 
        if dic[name]==m:
            r_name=name
    return r_name,m
    
        



print("Welcome to the secrect auction program.")
name_and_bid={}
while True:
    name=input("what is your name? ")
    bid=input("Wnat's your bid?: $")
    name_and_bid[name]=bid
    choice=input("Are there any other bidders? Type'yes' or 'no': ")
    choice=choice.lower()


    
    if choice=="yes":
        os.system('cls')
        continue
    elif choice=="no":
        os.system('cls')
        h_name,h_bid=max_bid(name_and_bid)
        print(f"The winner is {h_name} with a bid of ${h_bid}")
        break
    else: 
        print("Give a valid input")
