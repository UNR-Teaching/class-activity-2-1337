import unittest
from tictactoe import *


class TestTicTacToeIntegration(unittest.TestCase):

    def test_game(self):
        player1 = Player(1)
        player2 = Player(2)
        board = Board()
        game = Game(board, player1, player2)
        player1.send_move(board, '0,0,X')
        player2.send_move(board, '0,1,0')
        player1.send_move(board, '1,1,X')
        player2.send_move(board, '0,2,O')
        player1.send_move(board, '2,2,X')
        winner = game.check_over()
        self.assertEqual(1, winner)


if __name__ == '__main__':
    unittest.main()
