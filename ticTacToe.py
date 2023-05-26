# Anna Arnett
# 5/26/23
# Two-user Tic Tac Toe Game created in Jupyter Notebook

possible_values = [0, 1, 2, 3, 4, 5, 6, 7, 8] #possible index values on 3x3 board



# function that can print out current board
def display_board(board):
    print("   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")  #display row 1
    print("   |   |   ")
    print("-----------")
    
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")  #display row 2
    print("   |   |   ")
    print("-----------")
    
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")  #display row 3
    print("   |   |   ")
    print("-----------")
    
    
    
# function that takes player input and assigns their marker as either 'X' or 'O'
def player_input():
    
    input_marker = 'wrong'
    
    while input_marker != 'X' and input_marker != 'O':
        input_marker = input("Player 1: Do you want to be X or O? ").upper()  #take user input for marker choice
        if input_marker != 'X' and input_marker != 'O':
            print("Please input X or O. Try again. ")   #ensure user input is valid
    
    if input_marker == 'X':
        return ('X', 'O')   # assign player to X marker
    elif input_marker == 'O':
        return ('O', 'X')   # assign player to O marker
    
    return input_marker
  
  
  
  
# function that takes in the board list object, a marker ('X' or 'O'), and a desired position (0-8) and assigns it to the board
def place_marker(board, marker, position):
        
    board[position] = marker  #assigns X or O to user-specified position on the board
    
    
 
# function that takes a board and a mark (X or O) and checks to see if that mark has won
def win_check(board, mark):
    
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or # across the top row
    (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle row
    (board[6] == mark and board[7] == mark and board[8] == mark) or # across the bottom row
    (board[0] == mark and board[3] == mark and board[6] == mark) or # down column 1
    (board[1] == mark and board[4] == mark and board[7] == mark) or # down column 2
    (board[2] == mark and board[5] == mark and board[8] == mark) or # down column 3
    (board[0] == mark and board[4] == mark and board[8] == mark) or # across diagonal 1
    (board[6] == mark and board[4] == mark and board[2] == mark)) # across diagonal 2
  
  
  
# function that uses the random module to randomly decide which player goes first
import random

def choose_first():
    
    rand_num = random.randint(1, 2) # randomly pic 1 or 2
    
    if rand_num == 1:
        return "Player 1"   # Player 1 goes first
    elif rand_num == 2:
        return "Player 2"   # Player 2 goes first
    else:
        print("Error in choose_first function")
        
        
        
        
# function that returns True if a space on the board is freely available and False if not
def space_check(board, position):
    
    if board[position] == ' ':  # if space is empty
        return True
    else:
        return False
      
      
      
# checks if the board is full and returns true if full and false otherwise
def full_board_check(board):
    
    if ' ' in board:  # if there is an empty space in the board
        return False  # board is not full
    else:
        return True   # board is full
      
      
      
# asks for the player's next position then checks if the space is free

def position_choice(board):
    
    user_position = 'wrong'
    
    while user_position not in possible_values:
        user_position = int(input("Choose a position (0-8) "))   # user chooses position
        if user_position not in possible_values:
            print("Please try again.")    # ensures user input is valid
    
    if space_check(board, user_position):   # checks to ensure space is open
        return user_position
  
  
  
  # after the game ends, asks if user wants to play again and ends the game if not
  def replay():
    
    user_play = 'wrong'
    
    while user_play != "Y" and user_play != "N":
        user_play = input("Do you want to play again? (Y or N) ").upper()   #user chooses if they want to play again
        if user_play != "Y" and user_play != "N":
            print("Please input Y or N: ")    # ensures user input is valid
    
    if user_play == "Y":
        return True   # plays again
    elif user_play == "N":
        return False  # stops program
    else:
        print("Error in replay function")
        
        
        
        
# play game!!

print("Welcome to Tic Tac Toe!")
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']   # creates blank board to begin game

while True:
    
    play1_marker, play2_marker = player_input()   # assigns the markers 
    user_turn = choose_first()                    # decides who goes first randomly
    print(f'{user_turn} goes first.')             # prints first player

    ready2play = 'wrong'

    while ready2play != 'Y' and ready2play != 'N':
        ready2play = input("Are you ready to play? (Y or N): ").upper()   # asks user if they are ready to play to begin game
        if ready2play != 'Y' and ready2play != 'N':
            print("Please input Y or N ")                                 # ensures user input is valid

    if ready2play == 'Y':                                                 # if user is ready to play, begin game
        game_on = True
        display_board(board)
    else:
        game_on = False
        break
    
    while game_on:
        
        if user_turn == 'Player 1':                                      # Player 1's turn
            position = position_choice(board)
            place_marker(board, play1_marker, position)
            display_board(board)
            
            if win_check(board, play1_marker):
                print('Congratulations! Player 1 wins.')
                break
            else:
                if full_board_check(board):
                    print("Tie!")
                    break
                else:
                    user_turn = 'Player 2'
        else:
            position = position_choice(board)                         # Player 2's turn
            place_marker(board, play2_marker, position)
            display_board(board)
            
            if win_check(board, play2_marker):
                print('Congratulations! Player 2 wins.')
                break
            else:
                if full_board_check(board):
                    print('Tie!')
                    break
                else:
                    user_turn = 'Player 1'
                    
    if not replay():
        break
