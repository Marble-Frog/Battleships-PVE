# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Legend
# 'X' for placing and hit battleships
# ' ' for available spaces
# '-' for missed shot

from random import randint

# Defines the board and mapping
hidden_board = [[' '] * 8 for _ in range(8)]
guess_board = [[' '] * 8 for _ in range(8)]
letters_to_numbers = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3,
    'E': 4, 'F': 5, 'G': 6, 'H': 7
}


# For each row iterated, a separator is added
def print_board(board):
    print('  A B C D E F G H')
    print(' -----------------')
    row_number = 1
    for row in board:
        print(f"{row_number}|{'|'.join(row)}|")
        row_number += 1


# Creates 5 ships and places them randomly on the board
# If a ship is already placed there it will reroll
def create_ships(board):
    for _ in range(50):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "X"


def get_ship_location():
    # Ask the player for their row guess
    row = input('Please enter a ship row (1-8): ')
    while row not in '12345678':
        print('Please enter a valid row.')
        row = input('Please enter a ship row (1-8): ')

    # Ask the player for their column guess
    column = input('Please enter a ship column (A-H): ').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column.')
        column = input('Please enter a ship column (A-H): ').upper()

    # Converts the player's guess into usable data
    return int(row) - 1, letters_to_numbers[column]


# By looping through the board spaces, when an 'X' is found the counter goes up
def count_remaining_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':  # Only count unhit ships
                count += 1
    return count

def play_game(): 
    """
    Starts and manages the Battleship game loop.

    Initializes the game, handles player inputs, 
    updates game boards,and manages the remaining number
    of turns. Continues until all ships are hit or the player
    runs out of turns.
    """
    remaining_turns = 16

    # Create ships on the hidden board
    create_ships(hidden_board)
    for turn in range(remaining_turns, 0, -1):  # Start at 16 and count down to 1
        print(f"\nTurn {turn}")  # Display turn number, counting down from 16
        print_board(guess_board)

        try:
            row, column = get_ship_location()
            if guess_board[row][column] in ["X", "-"]:
                print("You've already guessed here, silly!")

            elif hidden_board[row][column] == "X":
                print("Hit! :3")
                guess_board[row][column] = "X"
                hidden_board[row][column] = " "  # Mark the ship as hit

            else:
                print("Miss! :/")
                guess_board[row][column] = "-"

            # Count remaining ships after each guess
            remaining_ships = count_remaining_ships(hidden_board)
            print(f"Remaining ships: {remaining_ships}")

            if remaining_ships == 0:
                print("Congratulations! You've won!")
                break

        except (IndexError, ValueError) as e:
            print(f"Invalid input or error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    else:
        print("Game Over! You've run out of turns.")


# Start the game
play_game()
