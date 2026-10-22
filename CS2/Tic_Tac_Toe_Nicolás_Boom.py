"""
Name: Nicolás Boom
Description: Tic-tac-toe
Bugs: None known
Date: 10/22/2026
Bonuses: Can play against computer, can play again, 
    10/19/2026: Base code uploaded, no bonuses, many bugs
    10/22/2026 9:10: Bug fixes, can now play against the computer
    10/22/2026 10:20: Added documentaion, now has play again function


"""

import os
import time
import random

def display_board(board):
    """
    Description: Prints the board so the users can see it.
    Uses a for loop and returns no error.

    Parameters:
    - board: the board to be printed

    Returns:
    - None
    """

    printable_board = ""

    for row in board:
        row.append("\n")
        printable_board = printable_board + " | ".join(row) + "----------\n"
        
    print(printable_board)

    for row in board:
        row.pop(3)

def get_player_details(playing_computer):
    """
    Description: Asks the players for their details, or if playing against computer, makes the second player's details that of the computer
    Uses two while loops and returns no error.

    Parameters:
    - playing_computer: a boolean, telling the function if the computer is playing

    Returns:
    - player1_details: literally the details of player 1, first their name, and then their chosen piece, either 'x' or 'o'
    - player2_details: literally the details of player 2, either their name and chosen piece, or the name 'computer' and the other piece that player 1 did not choose
    """
    
    while True:
        player1_name = input('What is your name, player 1? ')
        if player1_name == "":
            print("Please type in a name. Retry below: ")
            continue
        else:
            break

    if not playing_computer:
        while True:
            player2_name = input('What is your name, player 2? ')
            if player2_name == "":
                print("Please type in a name. Retry below: ")
                continue
            else:
                break
        
    while True:
        player1_letter = input('What letter do you want to be? Enter the letter X or the letter O. ').lower()

        if player1_letter == 'x' or player1_letter == "o":
            break
        else:
            print("Invalid response. Make sure to enter either 'X' or 'O'. Please try again below: ")
            continue
    
    player1_details = [f"{player1_name}", f"{player1_letter}"]

    if playing_computer:
        player2_details = ["Computer"]
    else:
        player2_details = [f"{player2_name}"]

    if player1_details[1] == "x":
        player2_details.append("o")
    else:
        player2_details.append("x")

    if playing_computer:
        player2_details.append("Comp.")

    return player1_details, player2_details

def get_player_move(board, player_details):
    """
    Description: Asks the players for thier moves, taking a computer move if there is no player 2, and applying them to the board
    Uses a whil loop and two for loops, and returns no error.

    Parameters:
    - board: the board to which the move will be applied
    - player_details: the details of the current player, so print functions can refer to the name, and so that the function appies the proper piece

    Returns:
    - board: the board after the changes are being applied to them
    """

    available_move = False

    while True:
        if len(player_details) == 3:
            move = get_computer_move(board)
            loading_screen(5, 3, "Computer is thinking")
        else:
            move = input(f"{player_details[0]}, where do you want to move? ")

        if move not in list("123456789"):
            print("Please enter a valid space, as a number between 1 and 9. Try again below: ")
            continue

        
        for row in board:
            for character in row:
                if character == move:
                    available_move = True
        
                if not available_move:
                    continue


        original_board = board
        row_counter = 0

        for row in board:
            space_counter = 0

            for space in row:
                if space == move:
                    board[row_counter][space_counter] = player_details[1].upper()

                space_counter += 1

            row_counter += 1

        return board

def get_computer_move(board):
    """
    Description: gets the random computer move
    Uses a while loop and a for loop, and returns no error.

    Parameters:
    - board: the current game board, so that the move the computer picks is not invalid

    Returns:
    - computer_move: the move the computer picked
    """

    available_move = False
    
    while True:
        computer_move = random.choice(list("123456789"))

        for row in board:
            for character in row:
                if character == computer_move:
                    available_move = True

        if available_move:
            return computer_move

def check_winner(board, player_details):
    """
    Description: checks the current board to see if there is three in a row anywhere, then returns a boolean depending on if there is
    Uses no loops and returns no error.

    Parameters:
    - board: the current board
    - player_details: the details of the current player, so the proper piece can be checked to see if someone won

    Returns:
    - True: a boolean, returned if someone won
    - False: a boolean, returned if someone has not won yet
    """

    letter = player_details[1].upper()
    
    if (board[0][0] == board[0][1] == board[0][2] == letter) or (board[1][0] == board[1][1] == board[1][2] == letter) or (board[2][0] == board[2][1] == board[2][2] == letter) or (board[0][0] == board[1][0] == board[2][0] == letter) or (board[0][1] == board[1][1] == board[2][1] == letter) or (board[0][2] == board[1][2] == board[2][2] == letter) or (board[0][0] == board[1][1] == board[2][2] == letter) or (board[2][0] == board[1][1] == board[0][2] == letter):
        return True
    else:
        return False

def loading_screen(iterations, length, message):
    """
    Description: Effectively, it is a mock loading screen
    Uses a while loop and a for loop, and returns no error.

    Parameters:
    - iterations: the amount of times the full loading screen iteration is repeated
    - length: the amount of periods following the message
    - message: the message to be printed in front of the periods

    Returns:
    - None
    """

    print("\033[H\033[J", end="")                     # \033[H moves the cursor to the top-left corner of the screen. \033[J clears the screen from the cursor to the end of the window. end="" prevents Python from printing a trailing blank newline.
    
    dot = "."
    counter = 0

    while counter <= iterations:
        dots = ""
        for i in range(length):
            print("\033[H\033[J", end="")                   # \033[H moves the cursor to the top-left corner of the screen. \033[J clears the screen from the cursor to the end of the window. end="" prevents Python from printing a trailing blank newline.
            dots = dots + dot
            print(f"{message}" + dots)
            time.sleep(0.15)

        counter += 1

def get_current_player():
    """
    Description: Uses the loading screen, then picks a random number, either 0 or 1
    Uses no loop and returns no error.

    Parameters:
    - None

    Returns:
    - random.choice([0, 1]): the code picking either 0 or 1
    """

    loading_screen(3, 5, "Deciding who is going first")
    return random.choice([0, 1])

def get_playing_computer():

    """
    Description: Asks the user if they want to play against the computer or against another player
    Uses a while loop and returns no error.

    Parameters:
    - None

    Returns:
    - True: boolean, returned if the player wants to play a computer
    - False: boolean, returned if the player wants to play another player
    """

    while True:
        playing_computer = input("Do you want to play a computer, or another player? Enter 'c' for computer, 'p' for player: ").lower()

        if playing_computer == 'c':
            return True
        elif playing_computer == 'p':
            return False
        else:
            print("Invalid Response, please try again below: ")
            continue

def play_again():
    """
    Description: Asks the user if they want to play again
    Uses a while loop and returns no error.

    Parameters:
    - None

    Returns:
    - True: a boolean, returned if the user wants to play again
    - False: a boolean, returned if the user does not want to play again
    """
    
    while True:
        choice = input("Do you want to play again? Enter either 'y' or 'n'. ").lower()

        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid response. Please try again below: ")


def main():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]

    playing_computer = get_playing_computer()

    if playing_computer:
        player1_details, player2_details = get_player_details(playing_computer)
    else:
        player1_details, player2_details = get_player_details(playing_computer)

    moves = 0

    start_player_number = get_current_player()
    if start_player_number == 0:
        print(f"{player2_details[0]} starts!")
    else:
        print(f"{player1_details[0]} starts!")
    

    while True:
        for player in [player1_details, player2_details]:
            start_player_number += 1
            if start_player_number == 1:
                continue

            display_board(board)
            board = get_player_move(board, player)
            print("\033[H\033[J", end="")               # \033[H moves the cursor to the top-left corner of the screen. \033[J clears the screen from the cursor to the end of the window. end="" prevents Python from printing a trailing blank newline.

            won = check_winner(board, player)
            if won:
                print(f"{player[0]} won! ")

                if play_again():
                    main()

            moves += 1
            if moves == 9:
                print("You tied. ")

                if play_again():
                    main()


main()