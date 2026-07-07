import random

def main(): 
    board = new_board()
    current_player = 1 # dita o jogador

    #LOOP WHILE PRINCIPAL
    jogo_ativo = True
    while jogo_ativo:
        if current_player == 1:
            print("VEZ DO PLAYER: ")
            render(board) # printa o novo quadro
        
        if current_player == 2:
            print("VEZ DO BOT: ")
            render(board)

        move = None # inicializa o while
        while move == None:
            if current_player == 1:
                move = get_move(board) # pede novamente até receber uma jogada valida
                if move == None:
                    print("Movimento inválido! Tente novamente.")
            else:
                move = get_ai_move(board)
                                # move armazena em forma de lista

        make_move(board, move, current_player)

        winner = get_winner(board)
        if winner is not None:
            render(board)
            print("O VENCEDOR É:", winner) 
            jogo_ativo = False

        if board_full(board):
            render(board)
            print("EMPATE!")
            jogo_ativo = False

        current_player = 2 if current_player == 1 else 1  # dita o jogador
               


def new_board():
    empty_board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    return empty_board


def render(board):
    #LOOP in LOOP: print the 3x3 matrix none values in principle
    counter = 0

    print("    0 1 2")
    print("   -------")

    for line in board:
        print(counter, end=" ")

        print("|", end=" ") # formatação
        for col in line:
            print(col, end=" ")
        print("|")

        counter += 1

    print("   -------")


def get_move(board):
    #LOOP: get condinate x and then y
    try:
        x = int(input("X: "))
        y = int(input("Y: "))
    except ValueError:
        return None
    
    #check if the coordinates is available
    if (2>= x >= 0) and (2>= y >= 0) and (board[x][y] == " "): # TODO: MELHORAR PFV
        return [x,y] 
    else:
        return None
    #return None if is a invalid move

def make_move(board, move, current_player):
    #LOOP in LOOP: change the value none in the (x,y)
    if current_player == 1:
        board[move[0]][move[1]] = 'O'
    else:
        board[move[0]][move[1]] = 'X'
        
    #to the sign of the current player "x" or "o"
    #update the current board

def get_winner(board): # TODO: REVISAR LOGICA
    #check the conditions to win
    for i in range(3): # checa a horizontal
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
        
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ") or\
       (board[0][2] == board[1][1] == board[2][0] and board[0][2] != " "):
        return board[1][1]
    
    return None
    # if the conditions are met: return the value of the winner
    # else: return none

def board_full(board):
    for i in board:
        for j in i:
            if j == " ":
                return False
    return True
    #lOOP in LOOP: if there is no "None" in the board, then the board is full


def get_ai_move(board):
    #LOOP: get condinate x and then y
    best_score = -100
    best_move = []

    for x, line in enumerate(board):
        for y, cell in enumerate(line):
            if cell == " ": # VERIFICA UMA POSSÍVEL JOGADA
                board[x][y] = "X" # TESTA ESSA JOGADA
                score = minimax(board, False )
                board[x][y] = " " # RETORNA PARA NONE

                # CHECA SE O SCORE DESSA JOGADA É O MEIOR
                if score > best_score:
                    best_score = score
                    best_move = [x,y]# ATUALIZA O MELHOR MOVIMENTO
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
                if cell == " ": # VERIFICA UMA POSSÍVEL JOGADA
                    board[x][y] = "X" # TESTA ESSA JOGADA
                    score = minimax(board, False )
                    board[x][y] = " " # RETORNA PARA NONE

                    # CHECA SE O SCORE DESSA JOGADA É O MEIOR
                    if score > best_score:
                        best_score = score
        return best_score
    
    
    else:
        best_score = 100

        for x, line in enumerate(board):
            for y, cell in enumerate(line):
                if cell == " ": # VERIFICA UMA POSSÍVEL JOGADA
                    board[x][y] = "O" # TESTA ESSA JOGADA
                    score = minimax(board, True )
                    board[x][y] = " " # RETORNA PARA NONE

                    # CHECA SE O SCORE DESSA JOGADA É O MEIOR
                    if score < best_score:
                        best_score = score
        
        return best_score
     
                
if __name__ == "__main__":
    main()
