


# Creating pieces
Empty = None
P = "Black Pawn"
p = "White Pawn"
K = "Black King"
k = "White King"
Q = "Black Queen"
q = "White Queen"
B = "Black Bishop"
b = "White Bishop"
N = "Black Knight"
n = "White Knight"
R = "Black Rook"
r = "White Rook"

# Pieces
white_pieces = [p, k, q, b, n, r]
black_pieces = [P, K, Q, B, N, R]

# palyer_turn
White = "White"
Black = "Black"

# Representing the board
class chess_board():
    def __init__(self, board, player_turn, king_moved = False):
        self.board = board
        self.player_turn = player_turn
        self.king_moved = king_moved
    

def test_board():
    # Return Intial Board
    board = [[R, N, B, Q, K, B, N, R],
             [P, P, P, P, Empty ,P, P, P],
             [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
             [Empty, Empty, Empty, Empty, P, Empty, Empty, Empty],
             [Empty, Empty, Empty, Empty, Empty, b, Empty, Empty],
             [Empty, Empty, Empty, Empty, p, Empty, Empty, Empty],
             [p, p, p, Empty, p, p, p, p],
             [r, n, Empty, q, k, b, n, r]]

    return board

def intial_board():
    board = [[R, N, B, K, Q, B, N, R],
             [P, P, P, P, P, P, P, P],
             [Empty for i in range(8)],
             [Empty for i in range(8)],
             [Empty for i in range(8)],
             [Empty for i in range(8)],
             [p, p, p, p, p, p, p, p],
             [r, n, b, k, q, b, n, r]]
    return board
 




    

