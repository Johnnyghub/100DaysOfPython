import random
from functions import display_board, input_marker, check_for_win

game_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  # gameboard starts with the value you need to input for each space

print("Welcome to Tic Tac Toe! This board is a reference for what number you need to enter to put a marker in a "
      "particular spot! Player 1 is X and player 2 is O. Good luck!")
display_board(game_board)
print("\n------------------------------------------------------")

game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # reinitialize game_board with blank values

player_1_markers = []  # stores the positions where an X is to make checking for a winner easier later
player_2_markers = []  # same but for Os

turn = random.randint(1,2)  # randomly select a player to start each time
game_over = False

while not game_over:
    display_board(game_board)  # display the board every turn
    print(f"\nPlayer {turn}'s turn.\n")

    position = input_marker() - 1  # subtract 1 because we need it to be an index

    playable_input = False  # only when this turns true does the marker get placed, we need to check if the place is occupied first

    while not playable_input:
        if game_board[position] != " ":
            print("There is already a marker at that location. Please enter new coordinates.\n")
            position = input_marker() - 1
        else:
            playable_input = True  # if there isn't already a marker there, let the player proceed

    if turn == 1:
        game_board[position] = 'X'  # place marker for that player
        player_1_markers.append(position+1)  # add the index + 1 of that position to the array for that player
        turn = 2  # switch player
    else:
        game_board[position] = 'O'
        player_2_markers.append(position+1)
        turn = 1

    game_over = check_for_win(x=player_1_markers, o=player_2_markers, board=game_board)

