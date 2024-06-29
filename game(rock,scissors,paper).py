"""
create gamming ( rock, scissors, paper) by random library 
"""

#import random library 
import random

#list of name choices
game = ["rock","scissors","paper"]

# define int variable to score user 
u = 0
#define int variable to score computer
c = 0

#define bool variable to change condition while loop 
x = True
while x:

    #enter choice user
    user = input(f"Enter a choice ({game[0]}, {game[1]}, {game[2]}): ").lower()

    #select choice computer by random library 
    computer = random.choice(game)

    #log out from game if user inter "quitgame"
    if user == "quitgame":
        print("FINISH")
        break

    #print alert message if user enter other word out the list game 
    elif not user in game:
        print("You chose a wrong choice, please try again\n")

    #writing conditions for games and calculate evrey time score for user or computer 
    elif user in game:
        print(f"You chose {user}, computer chose {computer}")
        if user == computer:
            print(f"Both players selected {user}. It's a tie!\n")
        elif user == game[0] and computer == game[1]:
            u+=1
            print(f"{game[0]} smashes {game[1]}! you scored 1 point, your score is {u}, computer score is {c}\n")
        elif user == game[1] and computer == game[0]:
            c+=1
            print(f"{game[0]} smashes {game[1]}! computer scored 1 point, your score is {u}, computer score is {c}\n")
        elif user == game[0] and computer == game[2]:
            c+=1
            print(f"{game[2]} covers {game[0]}! computer scored 1 point, your score is {u}, computer score is {c}\n")
        elif user == game[2] and computer == game[0]:
            u+=1
            print(f"{game[2]} covers {game[0]}! You scored 1 point, your score is {u}, computer score is {c}\n")
        elif user == game[1] and computer == game[2]:
            u+=1
            print(f"{game[1]} cuts {game[2]}! You scored 1 point, your score is {u}, computer score is {c}\n")
        elif user == game[2] and computer == game[1]:
            c+=1
            print(f"{game[1]} cuts {game[2]}! computer scored 1 point, your score is {u}, computer score is {c}\n")

    #if one of user or computer reash ten, print who win and quit from game 
    if u == 10 :
        print("="*50)
        print("Your score reach 10. YOU WIN!")
        print("="*50)
        x == False
        break
    elif c == 10 :
        print("="*50)
        print(f"Your score is {u}, computer reach 10. YOU LOST, GOOD LUCK!")
        print("="*50)
        x == False
        break
