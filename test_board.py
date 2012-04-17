import unittest
import reversi


class TestBorad(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_board_blank(self):
        board = reversi.new_board()
        for row in board:
            for pos in row:
                self.assertEquals(pos,'.')

    def test_board_size(self):
        board = reversi.new_board()
        self.assertEquals(len(board),8)
        for row in board:
            self.assertEquals(len(row),8)

    def test_board_starting(self):
        board = reversi.new_board()
        board = reversi.setup_board(board)
        print board
        for r,row in enumerate(board):
            for c,pos in enumerate(row):
                print r,c
                if r == 3 and c == 3:
                    self.assertEquals(pos, 'B')
                elif r == 3 and c == 4:
                    self.assertEquals(pos, 'W')
                elif r == 4 and c == 3:
                    self.assertEquals(pos, 'W')
                elif r == 4 and c == 4:
                    self.assertEquals(pos, 'B')
                else:
                    self.assertEquals(pos, '.')

    def test_available_moves(self):
        board = reversi.new_board()
        board = reversi.setup_board(board)
        possible_moves = reversi.calculate_moves(board,'B')
        for r,row in enumerate(possible_moves):
            for p,pos in enumerate(row):
                if r == 2 and p == 4:
                    self.assertEquals(pos, '0')
                elif r == 3 and p == 5:
                    self.assertEquals(pos, '0')
                elif r == 4 and p == 2:
                    self.assertEquals(pos, '0')
                elif r == 5 and p == 3:
                    self.assertEquals(pos, '0')



