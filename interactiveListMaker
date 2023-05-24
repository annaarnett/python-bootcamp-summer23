# Interactive List Maker
# Anna Arnett
# 5/24/23

# Simple interactive program that displays a list, has the user
# choose an index position and an input value, and replaces the
# value at the index position with the user's chosen value


# Function to display game list

game_list = [0, 1, 2]

def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)
    
# Function to get user input for position choice

def position_choice():
    
    choice = 'wrong'
    
    while choice not in ['0', '1', '2']:
        choice = input("Pick a position (0, 1, 2): ")
        
        if choice not in ['0', '1', '2']:
            print("Sorry, invavlid choice! ")
    
    return int(choice)
    
# Function to get user input for replacement choice

def replacement_choice(game_list, position):
    
    user_placement = input("Type a string to place at position: ")
    
    game_list[position] = user_placement
    
    return game_list
    
# Ensures user still wants to keep playing

def gameon_choice():
    
    choice = 'wrong'
    
    while choice not in ['Y', 'N']:
        
        choice = input("Keep playing? (Y or N): ")
        
        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand, please choose Y or N")
    
    if choice == "Y":
        return True
    else:
        return False

# runs game

game_on = True
game_list = [0, 1, 2]

while game_on:
    
    #displays current list
    display_game(game_list)
    print("\n")
    
    # asks the user for the position
    position = position_choice()
    print("\n")
    
    # updates the list with user's chosen replacement
    game_list = replacement_choice(game_list, position)
    print("\n")
    
    # display updated list
    display_game(game_list)
    print("\n")
    
    # ensure user still wants to play
    game_on = gameon_choice()
    print("\n")
