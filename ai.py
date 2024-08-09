from chess import *
from valid_moves import *
import copy
import sys

#Constatnts
DEPTH = 4


def result(chess_board, action):
    new_chess_board = copy.deepcopy(chess_board)
    # performing action we havn't deal with castling and other
    new_chess_board.board[action[0][0]][action[0][1]] = Empty
    new_chess_board.board[action[1][0]][action[1][1]] = chess_board.board[action[0][0]][action[0][1]]
    # changing player_turn 
    if new_chess_board.player_turn == White:
        new_chess_board.player_turn = Black
    else:
        new_chess_board.player_turn = White
    # if it is king move
        # change king_moved state of board
    return new_chess_board
 
def piece_wt(piece):
    '''return the piece wt''' # if don't found use discard this function
    if piece in [P,p]:
        return 1
    if piece in [B,b, N, n]:
        return 3
    if piece in [R, r]:
        return 5
    if piece in [Q, q]:
        return 9
    if piece in [K, k]:
        return 200

def material_score(board):
    nk = 0
    nq = 0 
    nb = 0
    nr = 0 
    nn = 0
    np = 0
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece == Empty:
                pass
            else:
                if piece == p:
                    np += 1
                elif piece == P:
                    np -= 1
                elif piece == b:
                    nb += 1
                elif piece == B:
                    nb -= 1
                elif piece == n:
                    nn += 1
                elif piece == N:
                    nn -= 1
                elif piece == r:
                    nr += 1
                elif piece == R:
                    nr -= 1
                elif piece == q:
                    nq += 1
                elif piece == Q:
                    nq -= 1
                elif piece == k:
                    nk += 1
                elif piece == K:
                    nk -= 1
        score = (200*nk)+(9*nq)+(5*nr)+(3*nb)+(3*nn)+(np)
        return score

def mobility_score(chess_board):
    '''Return mobility score'''
    chess_board.player_turn = White
    white_mobility = len(actions(chess_board))
    chess_board.player_turn = Black
    black_mobility = len(actions(chess_board))
    mobility = 0.1 * (white_mobility - black_mobility)
    return mobility

    
def utility(chess_board):
    '''implement'''
    '''rules would be like this:
        1.mobility
        2.piecewt 
    '''
    mat_score = material_score(chess_board.board)
    mob_score = mobility_score(copy.deepcopy(chess_board))
    if chess_board.player_turn == White:
        return mat_score + mob_score
    else:
        return (mat_score + mob_score) * -1
    
def eval(chess_board):
    # main function for execution of ai
    if chess_board.player_turn == White:
        maxi = float('-inf')
        ans = tuple()
        for action in actions(chess_board):
            changed_board = result(chess_board, action) 
            score = alphabetamin(changed_board,float('-inf'), float('inf'), DEPTH)
            if score >  maxi:
                maxi = score
                ans = action
    else:
        mini = float('inf')
        ans = tuple()
        for action in actions(chess_board):
            changed_board = result(chess_board, action) 
            score = alphabetamax(changed_board, float('-inf'), float('inf'), DEPTH)
            if score < mini:
                mini = score
                ans = action
    return ans

def maximizing(chess_board, d):
    if d == 0:
        return utility(chess_board)
    maxi = float('-inf')
    for action in actions(chess_board):
        changed_board = result(chess_board, action) 
        score = minimizing(changed_board,d-1)
        maxi = max(score, maxi)
    return maxi

def minimizing(chess_board, d):
    if d == 0:
        return utility(chess_board)
    mini = float('inf')
    for action in actions(chess_board):
        changed_board = result(chess_board, action) 
        score = maximizing(changed_board,d-1)
        mini = min(mini, score)
    return mini


def alphabetamax(chess_board, alpha, beta, d):
    if d == 0:
        return utility(chess_board)
    for action in actions(chess_board):
        changed_board = result(chess_board, action) 
        score = alphabetamin(changed_board,alpha, beta, d-1)
        if score >= beta:
            return beta
        if score > alpha:
            alpha = score
    return alpha

def alphabetamin(chess_board, alpha, beta, d):
    if d == 0:
        return utility(chess_board)
    for action in actions(chess_board):
        changed_board = result(chess_board, action) 
        score = alphabetamax(changed_board,alpha, beta, d-1)
        if score <= alpha:
            return alpha
        if score < beta:
            beta = score
    return beta

import time
print()
start = time.time()

board =  chess_board(test_board(),"White", True)
print(eval(board))

end = time.time()
print(end-start)



    

    

