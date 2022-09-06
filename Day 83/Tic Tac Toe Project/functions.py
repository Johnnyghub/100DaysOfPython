def display_board(game_board):
    """Simply displays the current game board. No while loop used since there is only 3 rows and it would be more
    time consuming to create a condition to only print two of the dashed lines to seperate rows instead of 3 when
    using a for loop."""

    print(f"\n {game_board[0]} | {game_board[1]} | {game_board[2]}")
    print(f"-----------")
    print(f" {game_board[3]} | {game_board[4]} | {game_board[5]}")
    print(f"-----------")
    print(f" {game_board[6]} | {game_board[7]} | {game_board[8]}")


def input_marker():
    """this code contains a while loop which also contains a try-catch loop so it's better to keep it out of the
    main game loop in order to keep it tidy."""

    value = 0  # placeholder value

    while True:  # loop until a valid input is given
        try:
            value = int(input("Enter the position you would like to place your marker at: "))

            if (value < 1) or (value > 9):  # if the value is out of range, raise an exception
                raise ValueError("Out of Range Input.")
        except ValueError:  # if the input was not an integer
            print("Please only enter an integer between 1 to 9.\n")
            continue
        else:
            break  # if there is no exception raised, break out of the while loop

    return value


def check_for_win(x, o, board):
    """Compares current placement of markers with all possible winning combos and decides if there has been a winner.
     Returns a boolean indicating that there has been a winner which should be saved into the game_over function in
     order to exit the while loop continuing the game. Also handles print statements for the winner (under the guise of
     X being player 1 and O being player 2."""

    winning_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    x_win = False
    o_win = False  # default values to avoid IDE telling me there might not be a value

    for combo in winning_combos:
        # checks if the 3 numbers in that particular combo are also available in each player's array, if they are,
        # then that means someone has won

        x_win = all(position in x for position in combo)
        o_win = all(position in o for position in combo)

    if x_win:
        print("\n\nPlayer 1 wins the game!")
        print("\nFinal Game Board:")
        display_board(board)
        return True  # game_over = True
    elif o_win:
        print("\n\nPlayer 2 wins the game!")
        print("\nFinal Game Board:")
        display_board(board)
        return True  # game_over = True
    else:
        if " " not in board:  # check if the board is full
            print("\n\nThe board is full and there are no winners. It's a tie!")
            print("\nFinal Game Board:")
            display_board(board)
            return True  # game_over = True
        return False  # game_over = False, continue




