################################
#                              #
# Homework Set #2 - Problem #2 #
#  'Tic-Tac-Toe - One Player'  #
#        by Robin Ryder        #
#       rmd6050@uncw.edu       #
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

number_of_computer_wins = 0
number_of_player_wins = 0

print("\nWelcome to Tic-Tac-Toe")
first_game = True

playing = True
while playing:
    if first_game == False:
        display_wins("\nPlayer", number_of_player_wins)
        display_wins("Computer", number_of_computer_wins)
    else:
        first_game = False

    # initialize the elements of the game
    player = Player(2)      # create Player object
    computer = Computer(3)  # create Computer object
    board = Board()         # create the empty board
    goes_first = random.choice(["player", "computer"])
    #goes_first = "player"
    #goes_first = "computer"

    if goes_first == "player":
        print("\nThe player goes first.")

        # the game loop
        while True:

            # player takes a turn, check for win, check for draw
            player.turn(board)
            if board.dev_mode == True: print(board.played)
            if player.win_status == True:
                with open("gamedata1.txt", "a") as file: file.write(str(board.played) + "\n")
                number_of_player_wins += 1
                break
            if board.number_of_turns == 9:
                board.display()
                print("\nGame is a draw!")
                break

            # computer takes a turn, check for win, check for draw
            #try:    file2 = open('gamedata2.txt', 'r')
            #except: file2 = False
            file2 = False
            computer.turn(board, file2)
            if file2 != False: file2.close()
            if board.dev_mode == True: print(board.played)
            if computer.win_status == True:
                with open("gamedata2.txt", "a") as file: file.write(str(board.played) + "\n")
                number_of_computer_wins += 1
                break
            if board.number_of_turns == 9:
                board.display()
                print("\nGame is a draw!")
                break

    elif goes_first == "computer":
        print("\nThe computer goes first.")

        # the game loop
        while True:

            # computer takes a turn, check for win, check for draw
            #try:    file1 = open('gamedata1.txt', 'r')
            #except: file1 = False
            file1 = False
            computer.turn(board, file1)
            if file1 != False: file1.close()
            if board.dev_mode == True: print(board.played)
            if computer.win_status == True:
                with open("gamedata1.txt", "a") as file: file.write(str(board.played) + "\n")
                number_of_computer_wins += 1
                break
            if board.number_of_turns == 9:
                board.display()
                print("\nGame is a draw!")
                break

            # player takes a turn, check for win, check for draw
            player.turn(board)
            if board.dev_mode == True: print(board.played)
            if player.win_status == True:
                with open("gamedata2.txt", "a") as file: file.write(str(board.played) + "\n")
                number_of_player_wins += 1
                break
            if board.number_of_turns == 9:
                board.display()
                print("\nGame is a draw!")
                break

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == "n":
        playing = False

print("\n")
display_wins("Player", number_of_player_wins)
display_wins("Computer", number_of_computer_wins)
print("\nGood-bye.")
