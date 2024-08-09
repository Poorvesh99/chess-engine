from chess import *


# Moves that can be performed by rook

def rook_actions(chess_board, initial_position):
    moves= set()
    
    i = initial_position[0]
    j = initial_position[1]
    
    if chess_board.player_turn == White:
        pieces= white_pieces
    else:
        pieces = black_pieces
    
    i -= 1
    while i > -1:
        position = chess_board.board[i][j]
        if position != Empty:
            if position not in pieces:
                moves.add((initial_position, (i,j)))
            break
        moves.add((initial_position, (i,j)))
        i -= 1
              
    i = initial_position[0]+1

    while i < 8:
        position = chess_board.board[i][j]
        if position != Empty:
            if position not in pieces:
                moves.add((initial_position, (i,j)))
            break
        moves.add((initial_position,(i,j) ))
        i +=1

    i = initial_position[0]
    j -= 1
    while j > -1:
        position = chess_board.board[i][j]
        if position != Empty:
            if position not in pieces:
                moves.add((initial_position, (i,j)))
            break
        moves.add((initial_position,(i,j)))
        j -= 1

    j = initial_position[1]+1

    while j < 8:
        position = chess_board.board[i][j]
        if position != Empty:
            if position not in pieces:
                moves.add((initial_position, (i,j)))
            break
        moves.add((initial_position,(i,j) ))
        j +=1 
        
    return moves



# return the valid moves for dishop at postion (i, j)
def bishop_actions(chess_board, initial_position):
    i = initial_position[0]
    j = initial_position[1]

    # if not bishop return empty set
    #if chess_board.board[i][j] not in [b, B]:
        #return set()

    # defining player pieces
    if chess_board.player_turn == White:
        pieces= white_pieces
    else:
        pieces = black_pieces

    moves = set()

    # iterate board to find empty
    # iterate diagonally down-right side
    i += 1
    j += 1
    while i < 8 and j < 8:
        position = chess_board.board[i][j]
        if position != Empty:
            if position not in pieces:
                moves.add((initial_position, (i, j)))
            break
        moves.add((initial_position,(i, j)))
        i += 1
        j += 1
    
    i = initial_position[0]
    j = initial_position[1]

    # iterate diagonally down-left side
    i += 1
    j -= 1
    while i < 8 and j > -1:
        position = chess_board.board[i][j]
        if position != Empty:
            if position not in pieces:
                moves.add((initial_position, (i, j)))
            break
        moves.add((initial_position,(i, j)))
        i += 1
        j -= 1
    
    i = initial_position[0]
    j = initial_position[1]

    # iterate diagonally up-left side
    i-=1
    j-=1
    while i > -1 and j > -1:
        position = chess_board.board[i][j]
        if position != Empty:
            if position not in pieces:
                moves.add((initial_position, (i, j)))
            break
        moves.add((initial_position,(i, j)))
        i -= 1
        j -= 1

    i = initial_position[0]
    j = initial_position[1]

    # iterate diagonally up-right side
    i -= 1
    j += 1
    while i > -1 and j < 8:
        position = chess_board.board[i][j]
        if position != Empty:
            if position not in pieces:
                moves.add((initial_position, (i, j)))
            break
        moves.add((initial_position,(i, j)))

        i -= 1
        j += 1

    return moves



# return valid moves for knight at position(i, j)
def knight_actions(chess_board, initial_position):
    i = initial_position[0]
    j = initial_position[1]

    moves = set()

    # definig player pieces
    if chess_board.player_turn == White:
        pieces= white_pieces
    else:
        pieces = black_pieces

    # valid postions 
    valid_positions = [
        (i+2, j+1), (i+2, j -1),
        (i-2, j+1), (i-2, j-1),
        (i+1, j+2), (i+1, j-2),
        (i-1, j+2), (i-1, j-2)
    ]
    
    for position in valid_positions:
        row = position[0]
        column = position[1]
        if -1 < row < 8 and -1 < column < 8:
            move = chess_board.board[row][column]
            if move == Empty or move not in pieces:
                moves.add((initial_position,position))
        
    
    return moves


#return valid_moves for queen
def queen_actions(chess_board, initial_position):
    moves = set()
    # vertical and horizontal moves
    moves.update(rook_actions(chess_board, initial_position))
    # diagonal moves
    moves.update(bishop_actions(chess_board, initial_position))
    
    return moves


def pawn_actions(chess_board, initial_position):
    moves = set()
    i, j = initial_position
    if chess_board.player_turn == White:
        if chess_board.board[i][j] != p:
            return set()
        pieces = black_pieces
        if -1 < i < 8 and -1 < j < 8:
            if i == 6 and chess_board.board[i-2][j] == Empty:
                moves.add((initial_position,(i-2, j)))
            if chess_board.board[i-1][j] == Empty:
                moves.add((initial_position, (i-1, j)))
            if j+1 < 8 and chess_board.board[i-1][j+1] in pieces:
                moves.add((initial_position, (i-1, j+1)))
            if j-1 > -1 and chess_board.board[i-1][j-1] in pieces:
                moves.add((initial_position, (i-1, j-1)))
    else:
        if chess_board.board[i][j] != P:
            return set()
        pieces = white_pieces
        if -1 < i < 8 and -1 < j < 8:
            if i == 1 and chess_board.board[i+2][j] == Empty:
                moves.add((initial_position,(i+2, j)))
            if chess_board.board[i+1][j] == Empty:
                moves.add((initial_position, (i+1, j)))
            if j+1 < 8 and chess_board.board[i+1][j+1] in pieces:
                moves.add((initial_position, (i+1, j+1)))
            if j-1 > -1 and chess_board.board[i+1][j-1] in pieces:
                moves.add((initial_position, (i+1, j-1)))

    return moves

# Kings valid moves
def king_actions(chess_board, initial_position):
    moves = set()
    i, j = initial_position

    # definig player pieces
    if chess_board.player_turn == White:
        pieces= white_pieces
    else:
        pieces = black_pieces

    cells  = [
        (i-1, j-1), (i-1, j), (i-1, j+1),
        (i, j-1), (i, j+1),
        (i+1, j-1), (i+1, j),(i+1, j+1)
    ]

    for cell in cells:
        row , column = cell
        if -1 < row < 8 and -1 < column < 8:
            piece = chess_board.board[row][column]
            if piece == Empty or piece not in pieces:
                moves.add((initial_position, cell))
    
    # check for castling moves
    
    # check if the moves are under attack
    
    return moves


def actions(chess_board):
        moves = set()
        board = chess_board.board
        if chess_board.player_turn == White:
            pieces = white_pieces
        else:
            pieces = black_pieces
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece == None or piece not in pieces:
                    pass
                else:#implement
                    if piece in [p, P]:
                        moves.update(pawn_actions(chess_board, (i, j)))
                    elif piece in [N, n]:
                        moves.update(knight_actions(chess_board, (i, j)))
                    elif piece in [B,b]:
                        moves.update(bishop_actions(chess_board, (i, j)))
                    elif piece in [R, r]:
                        moves.update(rook_actions(chess_board, (i, j)))
                    elif piece in [q, Q]:
                        moves.update(queen_actions(chess_board, (i, j)))
                    else:
                        moves.update(king_actions(chess_board, (i, j)))
        return moves
                                     
#  castling and el palacant implementation is remaining                  
                
board =  chess_board(test_board(),"White", True)
print(actions(board))



