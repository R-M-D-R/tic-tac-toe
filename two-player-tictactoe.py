################################
#                              #
# Homework Set #2 - Problem #1 #
# 'Tic-Tac-Toe - Two Player'   #
# by Robin Ryder               #
# rmd6050@uncw.edu             #
#                              #
################################

############
# Packages #
############

import random
from board import *
from player import *
from computer import *

#############
# Functions #
#############

def display_wins(player, number):
    number = str(number)
    if number == "1":
        statement = str(player) + " has won 1 game."
        print(statement)
    else:
        statement = str(player) + " has won " + number + " games."
        print(statement)

#############
# Main Loop #
#############

print("Welcome to Tic-Tac-Toe")

playing = True
while playing:

    # initialize the elements of the game
    player1 = Player(2) # create Player object
    player2 = Player(3) # create Player object
    board = Board()     # create the empty board
    goes_first = random.choice(["player", "computer"])
    #goes_first = "player"
    game = True

    # the game loop
    while True:
        
        # Player 1 takes a turn, check for win, check for draw
        print("\nPlayer 1's turn.")
        player1.turn(board)
        if board.dev_mode == True: print(board.played)
        if player1.win_status == True:
            print("\nPlayer 1 wins!")
            with open("gamedata1.txt", "a") as file: file.write(str(board.played) + "\n")
            break
        if board.number_of_turns == 9:
            board.display()
            print("\nGame is a draw!")
            break

        # Player 2 takes a turn, check for win, check for draw
        print("\nPlayer 2's turn.")
        player2.turn(board)
        if board.dev_mode == True: print(board.played)
        if player2.win_status == True:
            print("\nPlayer 2 wins!")
            with open("gamedata2.txt", "a") as file: file.write(str(board.played) + "\n")
            break
        if board.number_of_turns == 9:
            board.display()
            print("\nGame is a draw!")
            break

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == "n":
        playing = False
print("Good-bye.")
