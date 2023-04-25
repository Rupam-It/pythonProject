# this is black jack game 
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
print(logo)
    
import random
cards_value=[11,2,3,4,5,6,7,8,9,10,10,10,10] # a=1/11 and j=10, k=10, Q=10


def distributation_of_card(cards):
    your_card=[]
    for i in range(2):
        your_card.append(random.choice(cards))
    return your_card

def sum_of_my_cards(cards):
    value=0
    for i in cards:
        value+=i
    if value>21 and 11 in cards:
        value-=10
    return value


def player_third_card(cards,your_card):
    your_card.append(random.choice(cards))
    return your_card


def computer_third_card(cards,your_card):
    your_card.append(random.choice(cards))
    return your_card

def compare(value_user, value_comp):
    if value_comp> value_user or value_user>21:
        print("you loose...!!!!")
    elif value_user== value_comp or (value_user>25 and value_comp>25):
        print("There is a try")
    else: 
        print("You Win......!!!!")


def over_value(cards:list):
    s=sum_of_my_cards(cards)
    if s>21:
        print(f"your final hand:{cards}, final score:{s}")
        return True
    return False



while True:
    play=input("Do you want to play a game of blackjack? type 'y' or 'n' : ")
    if play=='n':
        break
    else: 
        user_card=distributation_of_card(cards_value)
        computer_card=distributation_of_card(cards_value)
        user_score=sum_of_my_cards(user_card)
        computer_score=sum_of_my_cards(computer_card)
        print(f"Your cards:{user_card}, current score:{user_score}")
        print(f"Computer's first card: {computer_card[0]}")
        another_card=input("type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card=='n':
            print(f"Your cards:{user_card}, final score:{user_score}")
            print(f"Your cards:{computer_card}, final score:{computer_score}")
            compare(user_score,computer_score)
            continue
        elif another_card=='y':
            user_card_add=player_third_card(cards_value,user_card)
            update_score_user=sum_of_my_cards(user_card_add)
            if over_value(user_card_add):
                print(f"Your cards:{user_card_add}, final score:{update_score_user}")
                print(f"Your cards:{computer_card}, final score:{computer_score}")
                print("You Loose..")
                continue
            else:
                if computer_score<17:
                    computer_card=computer_third_card(cards_value,computer_card)
                    update_score_computer=sum_of_my_cards(computer_card)
                update_score_computer=sum_of_my_cards(computer_card)

                print(f"Your cards:{user_card_add}, final score:{update_score_user}")
                print(f"Your cards:{computer_card}, final score:{update_score_computer}")
                compare(update_score_user,update_score_computer)
                continue