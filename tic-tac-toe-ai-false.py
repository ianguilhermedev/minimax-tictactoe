import random

def main(): 
    board = new_board()
    current_player = 1 

    while True:
        if current_player == 1:
            print("VEZ DO PLAYER: ")
            render(board) 
        
        if current_player == 2:
            print("VEZ DO BOT: ")
            render(board)

        move = None
        while move == None:
            if current_player == 1:
                move = get_move(board) 
                if move == None:
                    print("Movimento inválido! Tente novamente.")
            else:
                move = get_ai_move(board)

        make_move(board, move, current_player)

        winner = get_winner(board)
        if winner is not None:
            render(board)
            print("O VENCEDOR É:", winner) 
            break

        if board_full(board):
            render(board)
            print("EMPATE!")
            break 

        current_player = 2 if current_player == 1 else 1  


def new_board():
    empty_board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    return empty_board


def render(board): 
    counter = 0

    print("    0 1 2")
    print("   -------")

    for line in board:
        print(counter, end=" ")

        print("|", end=" ") 
        for col in line:
            print(col, end=" ")
        print("|")

        counter += 1

    print("   -------")


def get_move(board):
    try:
        x = int(input("X: "))
        y = int(input("Y: "))
    except ValueError:
        return None
    

    if (2>= x >= 0) and (2>= y >= 0) and (board[x][y] == " "):
        return [x,y] 
    else:
        return None

def make_move(board, move, current_player):
    if current_player == 1:
        board[move[0]][move[1]] = 'O'
    else:
        board[move[0]][move[1]] = 'X'

def get_winner(board): 

    for i in range(3): 
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
        
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ") or\
       (board[0][2] == board[1][1] == board[2][0] and board[0][2] != " "):
        return board[1][1]
    
    return None

def board_full(board):
    for i in board:
        for j in i:
            if j == " ":
                return False
    return True


def get_ai_move(board):
    best_score = -100
    best_move = []

    for x, line in enumerate(board):
        for y, cell in enumerate(line):
            if cell == " ": 
                board[x][y] = "X"
                score = minimax(board, False )
                board[x][y] = " "

                if score > best_score:
                    best_score = score
                    best_move = [x,y]
    return best_move

def minimax(board, maximize):

    winner = get_winner(board)
    if winner == "X":
        return 1

    elif winner == "O":
        return -1

    elif board_full(board):
        return 0

    if maximize:
        best_score = -100

        for x, line in enumerate(board):
            for y, cell in enumerate(line):
                if cell == " ": 
                    board[x][y] = "X"
                    score = minimax(board, False )
                    board[x][y] = " "

                    if score > best_score:
                        best_score = score
        return best_score
    
    
    else:
        best_score = 100

        for x, line in enumerate(board):
            for y, cell in enumerate(line):
                if cell == " ": 
                    board[x][y] = "O"
                    score = minimax(board, True )
                    board[x][y] = " " 

                    if score < best_score:
                        best_score = score
        
        return best_score
     
                
if __name__ == "__main__":
    main()
