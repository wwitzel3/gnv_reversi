import unittest
import reversi


class TestBorad(unittest.TestCase):
    def setUp(self):
        self.game = reversi.Reversi()
    def tearDown(self):
        pass

    def test_board_size(self):
        self.assertEquals(len(self.game.board),8)
        for row in self.game.board:
            self.assertEquals(len(row),8)

    def test_board_starting(self):
        for r,row in enumerate(self.game.board):
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
        moves = self.game.valid_moves(turn='B')
        assert False

