# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Legend
# 'X' for placing and hit battleships
# ' ' for available spaces
# '-' for missed shot

from random import randint, choice


# Defines the board size and the sizes of the ships
hidden_board = [[' '] * 8 for _ in range(8)]
guess_board = [[' '] * 8 for _ in range(8)]
Ship_Sizes = (2, 3, 3, 4, 5)
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


# Creates 5 ships with ship_sizes randomly assigns up and sideways to the ship
# If a ship is already placed there it will reroll
def create_ships(board):
    for ship_size in Ship_Sizes:
        placed = False
        while not placed:
            direction = choice(['horizontal', 'vertical'])
            ship_row, ship_column = randint(0, 7), randint(0, 7)

            if direction == 'horizontal':
                if ship_column + ship_size <= 8:
                    if all(board[ship_row][ship_column + i] == ' ' 
                           for i in range(ship_size)):
                        for i in range(ship_size):
                            board[ship_row][ship_column + i] = 'X'
                        placed = True


            else:
                if ship_row + ship_size <= 8:
                    if all(board[ship_row + i][ship_column] == ' ' 
                        for i in range(ship_size)):
                        for i in range(ship_size):
                            board[ship_row + i][ship_column] = 'X'
                        placed = True


# Get player's guess for row and column
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

# Count how many ships remain unhit
def count_remaining_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X': # Only count unhit ships
                count += 1
    return count

def play_game():
    """
    Starts and manages the Battleship game loop.
    Initializes the game, handles player inputs,
    updates game boards, and manages the remaining number
    of turns. Continues until all ships are hit or the player
    runs out of turns.
    """
    remaining_turns = 20

    #Create ships on hidden board
    create_ships(hidden_board)
    turns = remaining_turns

    while turns > 0:
        print(f'\nTurn {remaining_turns - turns + 1}')
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
                turns -= 1

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

    print("\nFinal Hidden Board:")
    print_board(hidden_board)

# Start the game
play_game()
