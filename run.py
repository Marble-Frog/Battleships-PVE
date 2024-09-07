# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
#Legend
#X for placing and hit battleships
#' ' for avalible spaces
#'-' for missed shot

from random import randint

hidden_board = [[''] * 8 for x in range(8) ]
guess_board = [[''] * 8 for x in range(8) ]
letters_to_numbers = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F ': 5, 'G': 6, 'H': 7}

def print_board(board):
    print('  A B C D E F H')
    print(' --------------')
    row_number = 1
    for row in board:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number += 1
        #For each row iterated a seporator is added 

def create_ships():
    for ship in range(5):
        ship_row, ship_collumn = randint(0,7) , randint(0,7)
        while board [ship_row][ship_collumn] == "X":
            ship_row, ship_collumn = radint(0,7) , randint(0,7)

def get_ship_location():
    pass

def count_hit_ships():
    pass