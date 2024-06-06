from Tic_Tac_Toe_All_Functions import *


print("Welcome to Tic-Tac-Toe game")

# Game loop
current_player = 1
while True:

    print(player_chosen_marker())
    while True:
        if current_player == 1:

            player_1_code()
            if player_1_win_check() or not to_check_blank_space(board):
                break
            current_player = 2
        else:
            player_2_code()
            if player_2_win_check() or not to_check_blank_space(board):
                break
            current_player = 1

    if player_1_win_check():
        print("\n" * 1)
        to_display_board()
        print("Player 1 is the Winner!")
    elif player_2_win_check():
        print("\n" * 1)
        to_display_board()
        print("Player 2 is the Winner!")
    else:
        print("\n" * 1)
        to_display_board()
        print("No one wins. It's a TIE")

    if replay() == "y":
        board = [" "] * 10
        board_with_numbers = [0, "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        available_positions = list(range(1, 10))
        continue
    else:
        print("Ashfak says..thanks for playing")
        break
