
from Tic_Tac_Toe_All_Functions import *

print("Welcome to Tic-Tac-Toe game")

# game loop
current_player = 1
while True:
    print(player_chosen_marker())
    while True:
        while True:
            if current_player == 1:
                player_1_code(board,board_with_numbers,available_positions)
                if player_1_win_check(board):

                    break
                elif to_check_blank_space(board) == False:
                    break
                current_player = 2
            else:
                player_2_code(board, board_with_numbers,available_positions)
                if player_2_win_check(board):

                    break
                elif to_check_blank_space(board) == False:
                    break
                current_player = 1

        if player_1_win_check(board):
            print("\n" * 1)
            to_display_board(board,board_with_numbers)
            print("Player 1 is the Winner !")
            break

        elif player_2_win_check(board):
            print("\n" * 1)
            to_display_board(board,board_with_numbers)
            print("Player 2 is the Winner !")
            break


        elif not player_1_win_check(board) and not player_2_win_check(board):
            print("\n" * 1)
            to_display_board(board,board_with_numbers)
            print("No one wins.it's a TIE")
            break

    if replay() == "y":
        board = list(" ") * 10
        board_with_numbers = [0, "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        available_positions = list(range(1, 10))
        #to_display_board(board,board_with_numbers)
        current_player = 1
        continue
    else:
        print("Ashfak says..thanks for playing")
        break
