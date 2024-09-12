# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
#Legend
#X for placing and hit battleships
#' ' for avalible spaces
#'-' for missed shot
   # The code to test


    
from random import randint

# Defines the board and mapping
hidden_board = [[' '] * 8 for _ in range(8)]
guess_board = [[' '] * 8 for _ in range(8)]
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

# For each row iterated a separator is added
def print_board(board):
    print('  A B C D E F G H')
    print(' -----------------')
    row_number = 1
    for row in board:
        print(f"{row_number}|{'|'.join(row)}")
        row_number += 1


# Creates 5 ships and places them randomly on the board
# If a ship is already placed there the function will loop until it finds an empty spot

def create_ships(board):
    for _ in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "X"

    
def get_ship_location():
    
    # Askes the player for their row guess
    row = input('Please enter a ship row (1-8): ')
    while row not in '12345678':
        print('Please enter a valid row.')
        row = input('Please enter a ship row (1-8): ')
    
    # Askes the player for their column guess
    column = input('Please enter a ship column (A-H): ').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column.')
        column = input('Please enter a ship column (A-H): ').upper()
    
    # Takes the row guess and decreases its value so it matches the list
    # Changes the column guess to number and returns the data value of the players guess 
    return int(row) - 1, letters_to_numbers[column]

# By looping through the board spaces, when a X is found the counter goes up, possible overlapping bug 
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


def player_guess():
    row, column = get_ship_location()
    if guess_board[row][column] in ["X","-"]:
        print("You've already guessed here silly")
    
    elif hidden_board[row][column] == "X":
        print("Hit! :3")
        guess_board[row][column] = "X"
    else: 
        print("Miss! :/")
        guess_board[row][column] = "-"

for turns in range(turns)
    print(f"\nTurn {turn + 1}")
    player_guess()
    print("\nGuess Board:")
    print_board(guess_board)

    remaining_ships = count_hit_ships(hidden_board)
    if remaining ships == 0:
        print("Congradulations you won!")
        break
    else:
        print("GameOver! you ran out of turns.")

# Create ships on the hidden board
create_ships(hidden_board)

# Initialize game parameters
turns = 10

# Print initial state of the board
print("Hidden Board (for testing purposes):")
print_board(hidden_board)  # This will display the hidden board
print("\nGuess Board:")
print_board(guess_board)