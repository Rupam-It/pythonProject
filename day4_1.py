# we are making a game of rock paper seasor 
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_move=input("what will you choose? type 0 for Rock, 1 for paper, 2 for scissor: ")
computer_move=random.randint(0,2)

if user_move=='0': # user give rock move
    print("your move")
    print(game_images[0])

    if computer_move==0:
        print("AI generated move")
        print(game_images[0])
        # boths are rock so draw
        print("==> match draw....!!!")

    elif computer_move==1:
        print("AI generated move")
        print(game_images[1])
        #rock and paper so user ai win
        print("==> you loose....!!!")

    elif computer_move==2:
        print("AI generated move")
        print(game_images[2])
        # boths are rock so draw
        print("==> you win....!!!")


elif  user_move=='1': #user give paper
    print("your move")
    print(game_images[1])

    if computer_move==0:
        print("AI generated move")
        print(game_images[0]) # ai give rock
        print("==>you win....!!!")

    elif computer_move==1:
        print("AI generated move")
        print(game_images[1]) # ai give paper
        print("==>match draw....!!!")

    elif computer_move==2:
        print("AI generated move")
        print(game_images[2]) # ai give scissor
        print("==>you loose....!!!")

elif  user_move=='2': #user give scissor
    print("your move ")
    print(game_images[2])

    if computer_move==0:
        print("AI generated move")
        print(game_images[0]) # ai give rock
        print("==> you loose....!!!")

    elif computer_move==1:
        print("AI generated move")
        print(game_images[1]) # ai give paper
        print("==> you win....!!!")

    elif computer_move==2:
        print("AI generated move")
        print(game_images[2]) # ai give scissor
        print("==> match draw....!!!")
else: 
    print("You have choose an invalid number!!!!.. please choose 0,1 or 2....")