from copy import deepcopy
from collections import namedtuple

class Reversi(object):
    empty = '.'
    position = namedtuple('position', 'row, col, color')
    start_positions = (
        position._make([3,3,'B']),
        position._make([3,4,'W']),
        position._make([4,3,'W']),
        position._make([4,4,'B']),
    )

    def __init__(self):
        self.board = self._new_board()

    def _new_board(self):
        row = [Reversi.empty,] * 8
        board = [deepcopy(row) for i in xrange(8)]
        for pos in Reversi.start_positions:
            board[pos.row][pos.col] = pos.color
        return board

    def reset(self):
        self.board = self._new_board()

    def valid_moves(self, turn):
        opp = 'B' if turn == 'W' else 'B'

        for r,row in enumerate(self.board):
            for c,col in enumerate(row):
                if col == turn:
                    for i in xrange(c+1,8):
                        if self.board[r][i] == Reversi.empty:
                            break
                        else:
                            print self.board[r][i]
                    for i in xrange(c-1,c):
                        print self.board[r][i]

_all__ = ['Reversi',]
