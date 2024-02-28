################################
#                              #
# Homework Set #2 - Problem #2 #
#  'Tic-Tac-Toe - One Player'  #
#        by Robin Ryder        #
#       rmd6050@uncw.edu       #
#                              #
################################

import random
import json

class Computer:
    def __init__(self, number):
        self.number = number
        self.win_status = False
        self.read_data = False

    # a random choice used in data generation
    def random_turn(self, board):
        computer_choice = random.choice(board.open)
        board.open.remove(computer_choice)
        board.update(computer_choice, self.number)
        board.played.append(computer_choice)
        board.number_of_turns = board.number_of_turns + 1
        board.check_winner(self)

    # the computer takes their turn during a game against a human being
    def turn(self, board, file):
        board.display()
        input("\nComputer's turn. Press enter.")
        if file == False:                               # if the data file does not exist,
            computer_choice = random.choice(board.open) # computer makes a random choice
        else:
            options = self.get_next_move(board, file)   # get all the possible options for where to play next
                                                        # in list form (sorted from most to least)
            if board.dev_mode == True: print("OPTIONS:", options)
            for i in range(0, len(options)):            # go through the options list
                if options[i] in board.played:          # if a particular option has already been played, continue the loop
                    continue
                else:
                    computer_choice = options[i]        # choose this as the computer's next move
                    break
        board.open.remove(computer_choice)
        board.update(computer_choice, self.number)
        board.played.append(computer_choice)
        board.number_of_turns = board.number_of_turns + 1
        board.check_winner(self)
        if self.win_status == True:
            board.display()
            print("\nComputer wins!")

    def next_move_count(self, next_list):
        counts = dict()
        for element in next_list:
            if element in counts:
                counts[element] = counts[element] + 1
            else:
                counts[element] = 1
        return counts

    # reading the data file to calculate the next best move
    def get_next_move(self, board, file):
        next_moves = []                     # initialize the list that will contain the potential next move
        for line in file:                   # go through each line in the file
            lst = json.loads(line)          # convert each line into a list (because they're a string by default)
            L1 = len(lst)
            L2 = len(board.played)
            if len(board.played) > 0:
                L = min(L1, L2)
                for i in range(1, L):
                    if lst[L1 - (i + 1) : L1] == board.played[L2 - i : L2]:
                        next_moves.append(lst[-1])
        next = self.next_move_count(next_moves).items()
        next_move = sorted(next, key = lambda item: item[1])
        print("sorted:", next_move)
        options = []
        L = len(next_move)
        for i in range(0, L):
            options.append(next_move[L-(i+1)][0])
        if len(board.played) == 0:
            options = [0, 2, 6, 8]
            random.shuffle(options)
        return options
