board = list(" ") * 10
board_with_numbers = [0,"1","2","3","4","5","6","7","8","9"]


def display_board(board):
    row1=(board[7] + "|" + board[8] + "|" + board[9])
    row2=(board[4] + "|" + board[5] + "|" + board[6])
    row3=(board[1] + "|" + board[2] + "|" + board[3])
    return row1, row2, row3

def cardinal_showing_board(board_with_numbers):
    row1=(board_with_numbers[7] + "|" + board_with_numbers[8] + "|" + board_with_numbers[9])
    row2=(board_with_numbers[4] + "|" + board_with_numbers[5] + "|" + board_with_numbers[6])
    row3=(board_with_numbers[1] + "|" + board_with_numbers[2] + "|" + board_with_numbers[3])
    return row1, row2, row3


def to_display_board():
    for b1,c1 in zip(display_board(board), cardinal_showing_board(board_with_numbers)):
        print(b1 + "    " + c1)

 
def to_put_marker(board, position, marker):
    board[position] = marker


def to_check_if_position_is_empty(board, position):
    if board[position] == " ":
        return True
    else:
        return False

def to_check_blank_space(board):
    var = " "
    if var in (board[1:11]):
        return True
    else:
        return False


def player_marker_choosing():
    while True:
        player_1_marker = (input("Player 1, Pls choose your marker, either 'X' or 'O': ")).upper()

        if player_1_marker not in ("X", "O"):
            print("Player 1, your marker must be,either 'X' or 'O'")
            continue

        if player_1_marker == "X":
            return ("X", "O")
        else:
            return ("O", "X")


player_1_chosen_marker = " "
player_2_chosen_marker = " "


def player_chosen_marker():
    global player_1_chosen_marker
    global player_2_chosen_marker

    player_1_chosen_marker, player_2_chosen_marker = player_marker_choosing()

    return (f"So,\nPlayer 1 marker: {player_1_chosen_marker}\nPlayer 2 marker: {player_2_chosen_marker}")


def player_1_win_check():
    if ((board[7] == board[8] == board[9] == player_1_chosen_marker) or
            (board[4] == board[5] == board[6] == player_1_chosen_marker) or
            (board[1] == board[2] == board[3] == player_1_chosen_marker) or
            (board[1] == board[4] == board[7] == player_1_chosen_marker) or
            (board[2] == board[5] == board[8] == player_1_chosen_marker) or
            (board[3] == board[6] == board[9] == player_1_chosen_marker) or
            (board[1] == board[5] == board[9] == player_1_chosen_marker) or
            (board[3] == board[5] == board[7] == player_1_chosen_marker)):
        return True


def player_2_win_check():
    if ((board[7] == board[8] == board[9] == player_2_chosen_marker) or
            (board[4] == board[5] == board[6] == player_2_chosen_marker) or
            (board[1] == board[2] == board[3] == player_2_chosen_marker) or
            (board[1] == board[4] == board[7] == player_2_chosen_marker) or
            (board[2] == board[5] == board[8] == player_2_chosen_marker) or
            (board[3] == board[6] == board[9] == player_2_chosen_marker) or
            (board[1] == board[5] == board[9] == player_2_chosen_marker) or
            (board[3] == board[5] == board[7] == player_2_chosen_marker)):
        return True


available_positions = list(range(1, 10))


def player_1_code():
    print("\n" * 1)
    to_display_board()
        
    while True:
        
        try:

            position = int(input(f"Player 1,enter your desired position, from available_positions: {available_positions}"))
    
            if position not in available_positions:
                print(
                    f"Invalid entry. Your chosen position must be (an integer) from these available_positions: {available_positions}: ")
                continue
        except:
            print(f"Invalid entry. Your chosen position must be (an integer) from these available_positions: {available_positions}: ")
            continue
               

        marker = player_1_chosen_marker

        to_put_marker(board, position, marker)
        to_display_board()
        available_positions.remove(position)
        board_with_numbers[position] = " "

        break


def player_2_code():
    print("\n" * 1)
    to_display_board()

    while True:
        
        try:

            position = int(input(f"Player 2,enter your desired position, from available_positions: {available_positions}"))
    
            if position not in available_positions:
                print(
                    f"Invalid entry. Your chosen position must be (an integer) from these available_positions: {available_positions}: ")
                continue
        except:
            print(f"Invalid entry. Your chosen position must be (an integer) from these available_positions: {available_positions}: ")
            continue

        marker = player_2_chosen_marker

        to_put_marker(board, position, marker)
        to_display_board()
        available_positions.remove(position)
        board_with_numbers[position] = " "

        break


def replay():
    while True:
        user_input = input("Wanna play again: y or n: ")
        if user_input not in ("y", "n"):
            print("You must input 'y' to play .. or ..'n' to quit")
            continue
        return user_input
