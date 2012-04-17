from copy import deepcopy

def new_board():
    board = []
    row = ['.',]*8
    [board.append(deepcopy(row)) for i in xrange(8)]
    return board

def setup_board(board):
    board[3][3] = 'B'
    board[3][4] = 'W'
    board[4][3] = 'W'
    board[4][4] = 'B'
    return board

def calulate_moves(board, turn):
    oppenent_positions = []
    pos_match = 'B' if turn == 'W' else 'W'
    for r,row in enumerate(board):
        for p,pos in enumerate(board):
            if pos == pos_match:
                oppenent_positions.append([r,p])

    for r,p in oppenent_positions:
        if r == 0 or r == 7:
            for i in xrange(p+1,8):
                pass
            for i in xrange(p-1,p):
                pass
        if p == 0 or p == 7:
            pass

_all__ = ['new_board', 'setup_board', 'calulate_moves',]
