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

    return player1_details, player2_details

def get_player_move(board, player_details):

    while True:
        move = input(f"{player_details[0]}, where do you want to move? ")

        if move not in list("123456789"):
            print("Please enter a valid space, as a number between 1 and 9. Try again below: ")
            continue

        for row in board:
            i = 0
            for space in row:
                if space == move:
                    if row[i] == move:
                        row[i] = player_details[1].upper()
                    else:
                        print("Invalid move. Please try again below: ")
                        continue
                i += 1

        return board

def get_computer_move(board):
    while True:
        computer_move = random.choice(list("123456789"))

        for row in board:
            if row.index(computer_move) == 'X' or row.index(computer_move) == "O":
                continue

        break



def check_winner(board, player_details):
    letter = player_details[1].upper()
    
    if (board[0][0] == board[0][1] == board[0][2] == letter) or (board[1][0] == board[1][1] == board[1][2] == letter) or (board[2][0] == board[2][1] == board[2][2] == letter) or (board[0][0] == board[1][0] == board[2][0] == letter) or (board[0][1] == board[1][1] == board[2][1] == letter) or (board[0][2] == board[1][2] == board[2][2] == letter) or (board[0][0] == board[1][1] == board[2][2] == letter) or (board[2][0] == board[1][1] == board[0][2] == letter):
        return True
    else:
        return False

def loading_screen():
    print("\033[H\033[J", end="")                     # \033[H moves the cursor to the top-left corner of the screen. \033[J clears the screen from the cursor to the end of the window. end="" prevents Python from printing a trailing blank newline.
    
    dot = "."
    counter = 0

    while counter <= 3:
        dots = ""
        for i in range(5):
            print("\033[H\033[J", end="")                   # \033[H moves the cursor to the top-left corner of the screen. \033[J clears the screen from the cursor to the end of the window. end="" prevents Python from printing a trailing blank newline.
            dots = dots + dot
            print("Picking a which player starts" + dots)
            time.sleep(0.15)

        counter += 1

def get_current_player():
    loading_screen()
    return random.choice([0, 1])

def get_playing_computer():
    while True:
        playing_computer = input("Do you want to play a computer, or another player? Enter 'c' for computer, 'p' for player: ").lower()

        if playing_computer == 'c':
            return True
        elif playing_computer == 'p':
            return False
        else:
            print("Invalid Response, please try again below: ")
            continue
        
            
def main():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]

    playing_computer = get_playing_computer()

    if playing_computer:
        player1_details, computer_details = get_player_details(playing_computer)
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
                print(f"Congradulations, {player[0]}, you won! ")
                break

            moves += 1
            if moves == 9:
                print("You tied. ")
                break


main()