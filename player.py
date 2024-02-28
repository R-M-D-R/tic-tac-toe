################################
#                              #
# Homework Set #2 - Problem #2 #
#  'Tic-Tac-Toe - One Player'  #
#        by Robin Ryder        #
#       rmd6050@uncw.edu       #
#                              #
################################

class Player:
    def __init__(self, number):
        self.number = number
        self.win_status = False

    def validate_input(self, board):
        while True:
            board.display()
            while True:
                question = "\nPlayer choose a spot (1–9) or type '?' to see a reference board: "
                choice = input(question)
                if choice == "?":
                    print(board.reference_board)
                    continue
                elif choice.lower() == "q":
                    exit()
                else:
                    try:
                        choice = int(choice) - 1
                        if choice not in board.open:
                            print("\nSpot already taken.")
                            continue
                        elif choice in board.open:
                            board.open.remove(choice)
                            board.update(choice, self.number)
                            board.played.append(choice)
                            not_valid = False
                            break
                    except:
                        print(choice + " is an invalid choice. Please choose again.")
                        continue
            break

    def turn(self, board):
        self.validate_input(board)  # get correct input and update board data
        board.number_of_turns += 1  # increment the total number of moves played
        board.check_winner(self)    # check if they won -- if so, the game is over
        if self.win_status == True:
            board.display()
