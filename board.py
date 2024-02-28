################################
#                              #
# Homework Set #2 - Problem #2 #
#  'Tic-Tac-Toe - One Player'  #
#        by Robin Ryder        #
#       rmd6050@uncw.edu       #
#                              #
################################

class Board:
    def __init__(self):
        self.data = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.open = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.played = []
        self.number_of_turns = 0
        self.reference_board =  "\n1 2 3\n4 5 6\n7 8 9"
        self.dev_mode = False

    def available(self):
        print(self.open)

    def played(self):
        print(self.played)

    def character(self, number):
        if number == 2:
            return "X"
        elif number == 3:
            return "O"
        else:
            return "-"

    def update(self, location, number):
        self.data[location] = number

    def display(self):
        row1 = "\n" + self.character(self.data[0]) + " " + self.character(self.data[1]) + " " + self.character(self.data[2])
        row2 = "\n" + self.character(self.data[3]) + " " + self.character(self.data[4]) + " " + self.character(self.data[5])
        row3 = "\n" + self.character(self.data[6]) + " " + self.character(self.data[7]) + " " + self.character(self.data[8])
        display_board = row1 + row2 + row3
        print(display_board)

    def check_winner(self, player):
        row1 = (self.data[0] * self.data[1] * self.data[2]) % 6
        row2 = (self.data[3] * self.data[4] * self.data[5]) % 6
        row3 = (self.data[6] * self.data[7] * self.data[8]) % 6
        column1 = (self.data[0] * self.data[3] * self.data[6]) % 6
        column2 = (self.data[1] * self.data[4] * self.data[7]) % 6
        column3 = (self.data[2] * self.data[5] * self.data[8]) % 6
        diagonal1 = (self.data[0] * self.data[4] * self.data[8]) % 6
        diagonal2 = (self.data[2] * self.data[4] * self.data[6]) % 6

        if row1 + row2 + row3 == player.number:
            player.win_status = True
        elif column1 + column2 + column3 == player.number:
            player.win_status = True
        elif diagonal1 == player.number:
            player.win_status = True
        elif diagonal2 == player.number:
            player.win_status = True
        else:
            pass
