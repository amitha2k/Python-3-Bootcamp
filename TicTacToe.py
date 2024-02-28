#types of lines to print in a board:
box_part = "   |   |   "
line = "-----------"
value_in_box = " {} | {} | {} "

# A function that takes in the inputs in each box of the board and displays the board
def display_board(board):
    print (box_part)
    print(value_in_box.format(board[0],board[1],board[2]))
    print (box_part)
    print(line)
    print (box_part)
    print(value_in_box.format(board[3],board[4],board[5]))
    print (box_part)
    print(line)
    print (box_part)
    print(value_in_box.format(board[6],board[7],board[8]))
    print (box_part)

# function that asks player 1 to choose their marker and proceeds to the 'ready to play' phase
def select_marker():
    marker = input("Player1: Do you want to be X or O? ")
    while marker not in ['O','X']:
        print("Ivalid input!")
        marker = input("Player1: Do you want to be X or O? ")
    return marker

#function that asks player to decide whether they are ready or wish to change marker. If ready, game starts.
def ready_to_play():
    rtp = input("Are you ready to play? (Y/N): ")
    while rtp not in ['Y','N']:
        print("Ivalid input!")
        rtp = input("Are you ready to play? (Y/N): ")
    return rtp
    
#function that checks if a position is available on the board
def space_check(board, position):
    return board[position] not in ['X','O']

#function that places the X or O in the specified position
def placement(marker, board, position):
    board[position-1] = marker
    return board

#function that checks if any player has won, given a board
def win_check(board, marker):
    for i in range(3):
         if [board[i], board[i+3], board[i+6]] == [marker]*3:
              return True
    for i in range(0,7,3):
         if [board[i], board[i+1], board[i+2]] == [marker]*3:
              return True
    if [board[0], board[4], board[8]] == [marker]*3 or [board[2],board[4],board[6]] == [marker]*3:
         return True
    else:
         return False

#function that checks if board is full
def check_full(board):
    for i in board:
        if i == ' ':
            return False
    return True

#swap turn or marker
def swap(obj):
    if obj == "X":
        return "O"
    elif obj == "O":
        return "X"
    elif obj == "1":
        return "2"
    else:
        return "1"

print('Welcome to TicTacToe')
while True:
    board = [' ']*9
    number_board = [1,2,3,4,5,6,7,8,9]
    turn = "1"
    marker = select_marker()
    rtp = ready_to_play()
    if rtp == "Y":
        while not check_full(board) and not win_check(board, 'X') and not win_check(board,'O'):
            display_board(number_board)
            print("\n~~~~~~~~~~~\n")
            display_board(board)
            new_move = int(input("Player {}, choose a position: ".format(turn)))
            while new_move not in [1,2,3,4,5,6,7,8,9] or board[new_move-1] in ['X','O']:
                print("Invalid move")
                new_move = input("Player {}, choose a position: ".format(turn))
            board = placement(marker, board, new_move)
            marker = swap(marker)
            turn = swap(turn)
            print(board)
            print(not check_full(board))
        display_board(board)
        if win_check(board, "X") or win_check(board, "O"):
            print("Player {} wins!".format(swap(turn)))
        else:
            print("It's a tie!!")
    again = input("Would you like to play again? (Y/N): ")
    while again not in ['Y','N']:
        print("Invalid input!")
        again = input("Would you like to play again? (Y/N): ")
    if again == 'N':
        print("Thanks for playing")
        break

