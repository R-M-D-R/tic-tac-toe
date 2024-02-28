#
#   This is the data generator file.
#   It creates the data used by the
#   computer when playing a one-player
#   game against the computer.
#

import random
from board import *
from player import *
from computer import *


print("Tic-Tac-Toe DATA GENERATOR")

number = int(input("How many games do you want the computer to win? "))

file1 = open("gamedata1.txt", "w")
computer1_won = 0
while computer1_won < number:

    # initialize the elements of the game
    computer1 = Computer(2) # create Player object
    computer2 = Computer(3) # create Computer object
    board = Board()         # create the empty board
    while True:
        # computer1 goes first, check for win, check for draw
        computer1.random_turn(board)
        if computer1.win_status == True:
            file1.write(str(board.played) + "\n")
            computer1_won = computer1_won + 1
            print("Number of wins: " + str(computer1_won))
            break
        if board.number_of_turns == 9:
            break

        # computer2 goes second, check for win, check for draw
        computer2.random_turn(board)
        if computer2.win_status == True:
            break
        if board.number_of_turns == 9:
            break
file1.close()

file2 = open("gamedata2.txt", "w")
computer2_won = 0
while computer2_won < number:

    # initialize the elements of the game
    computer1 = Computer(2) # create Player object
    computer2 = Computer(3) # create Computer object
    board = Board()         # create the empty board
    while True:
        # computer1 goes first, check for win, check for draw
        computer1.random_turn(board)
        if computer1.win_status == True:
            break
        if board.number_of_turns == 9:
            break

        # computer2 goes second, check for win, check for draw
        computer2.random_turn(board)
        if computer2.win_status == True:
            file2.write(str(board.played) + "\n")#     f'{list_item}\n'
            computer2_won = computer2_won + 1
            print("Number of wins: " + str(computer2_won))
            break
        if board.number_of_turns == 9:
            break
file2.close()

print("Data creation complete.")
