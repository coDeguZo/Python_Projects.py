# Rock Paper Scissors Game

import random

# Need input from user and from Computer

game = ["Rock", "Paper", "Scissors"]
computer_wins = 0
player_wins = 0
tie_draw = 0
computer = random.choice(game)
no_of_chances = random.randint(1, 3)
totalgames = no_of_chances
player = input("Choose Rock, Paper, or Scissors: ")

while no_of_chances != 0:
    if computer == player:
        print("You Both Win")
        tie_draw += 1
        no_of_chances -= 1
    elif (computer == "Rock" and player=="Scissors") or (computer == "Scissors" and player == "Paper") or (computer == "Paper" and player == "Scissors"):
        print("Computer Wins!")
        computer_wins += 1
        no_of_chances -= 1
    else:
        print("Player Wins!!!!!")
        player_wins += 1
        no_of_chances -= 1

if no_of_chances ==0:
    print("Game Over")
    print("Total Games: ", totalgames)
    print("Games won by player: ", player_wins)
    print("Games won by computer: ", computer_wins)
    print("Tie: ", tie_draw)

if player_wins > computer_wins:
    print("Player is the Best!!!")
