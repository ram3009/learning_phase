# Global variables
board=["-","-","-","-","-","-","-","-","-"]
game_on=True
current_player='X'
input_list=["1","2","3","4","5","6","7","8","9"]

#----------------------------------------------------

# Displaying board 
def display_board(board):
    global game_on
    print(board[0], "|",board[1],"|",board[2])
    print(board[3], "|",board[4],"|",board[5])
    print(board[6], "|",board[7],"|",board[8])
    if "-" not in board:
        print("Tie")
        game_on=False

display_board(board)

# Function to flip player
def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
        return 
    else:
        current_player='X'
        return 

# Function to get input from User and checks if valid or no
def get_input():
    valid_input=True
    print(f"{current_player}'s turn")
    while valid_input: 
        user_position=input("Enter your position: ")
        if user_position not in input_list:
            print("Invalid input, try again..!")
        elif user_position in input_list:
            temp=int(user_position) 
            temp-=1       
            if board[temp]!="-":
                print("Position already taken, choose again..!")    
            else:
                valid_input=False     
        
    user_position=int(user_position) 
    user_position-=1       
    board[user_position]=current_player
    display_board(board)


def check_if_win():
    check_row()
    check_column()
    check_diagonal()
    
def check_row():
    global game_on
    if board[0]==board[1]==board[2] and board[0]!="-":
        print(f"Winner is {board[0]}") 
        game_on=False
    if board[3]==board[4]==board[5] and board[3]!="-":
        print(f"Winner is {board[3]}") 
        game_on=False
    if board[6]==board[7]==board[8] and board[6]!="-":
        print(f"Winner is {board[6]}") 
        game_on=False
        
def check_column():
    global game_on
    if board[0]==board[3]==board[6] and board[0]!="-":
        print(f"Winner is {board[0]}") 
        game_on=False
    if board[1]==board[4]==board[7] and board[1]!="-":
        print(f"Winner is {board[1]}") 
        game_on=False
    if board[2]==board[5]==board[8] and board[2]!="-":
        print("fWinner is {board[2]}") 
        game_on=False
        
def check_diagonal():
    global game_on
    if board[0]==board[4]==board[8] and board[0]!="-":
        print(f"Winner is {board[0]}") 
        game_on=False
    if board[2]==board[4]==board[6] and board[2]!="-":
        print(f"Winner is {board[2]}") 
        game_on=False

# Handling the game , main function
def game_play():
    while game_on:
        get_input()
        check_if_win()
        flip_player()

game_play()
